import sys
import os
import subprocess
import yaml
import glob
import shutil
from ftplib import FTP
from datetime import datetime
import threading
import logging
import time
import re
import optparse
import pyodbc

def log_to_db(step_id, company_id, company_store_count, comment):
  cursor = db_connection.cursor()
  cursor.execute("insert into retail_loader_log (step_id, company_id, company_store_count, comment) values (?, ?, ?, ?)", step_id, company_id, company_store_count, comment)
  db_connection.commit()
  cursor.close()

def spawn(*args):
  cmd = " ".join(args)
  logging.info("Running [%s]." % (cmd))
  proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = proc.communicate()
  logging.info(stdout)
  
  if(proc.returncode != 0):
    logging.info(stderr)
    raise Exception("Previous call to 'spawn()' returned %d\n\t parameters: %s" % (proc.returncode, cmd))

  return 1

def ftp_binary_pull(ftp, filename, outfile=None):
  suffix = datetime.now().strftime("%Y%m%d%H%M%S")

  if outfile is None:
    outfile = sys.stdout

  ftp.retrbinary("RETR " + filename, outfile.write)
  ftp.rename(filename, filename + "." + suffix)

def ftp_binary_put(ftp, filename, infile=None):
  if infile is None:
    infile = sys.stdin

  # save file like object as to the ftp path \\pub\\cms\\textfiles
  ftp.storbinary("STOR " + filename, infile) 
  
def get_sub_directories(dir):
  return [name for name in os.listdir(dir)
      if os.path.isdir(os.path.join(dir, name))]

def move_directory(src, dest):
  logging.info("Moving [%s] to [%s]" % (src, dest))
  shutil.move(src, dest)

def unixify(full_path):
  path, leaf = os.path.split(full_path) 
  unix_leaf = leaf 
  if(re.search('[A-Z -]', unix_leaf)):
    unix_leaf = re.sub('[ -]', '_', unix_leaf.lower())
    unix_leaf = re.sub('_+', '_', unix_leaf)

  return (os.path.join(path, leaf), os.path.join(path, unix_leaf))

############################################################

def pull():
  server = config['ftp']['server']
  user = config['ftp']['user'] 
  password = config['ftp']['password'] 
  remote_directory = config['ftp']['remote_store_directory']
  local_directory = config['ftp']['local_store_directory']

  logging.info("Connecting to ftp server " + server)
  ftp = FTP(server)

  logging.info("Logging in to " + server)
  ftp.login(user, password)
  
  logging.info("Changing to directory " + remote_directory)
  ftp.cwd(remote_directory)
  files = ftp.nlst("*.zip")

  for f in files:
    logging.info("Fetching file " + f + " to " + local_directory + f)
    fh = open(local_directory + f, 'wb')
    ftp_binary_pull(ftp, f, fh)
    fh.close()
    log_to_db(1, 0, 0, f)
    src = local_directory + f
    dest = config['working']['unzip_dir'] + f

    shutil.copyfile(src, dest)
  
  ftp.close()

  return 1

def unzip():
  zipped_file_dir = config['working']['unzip_dir']
  layers_directory = config['working']['create_layers_dir']

  for zip_file in glob.glob(os.path.join(zipped_file_dir, '*.zip')):
    logging.info("Extracting %s" % (zip_file))
    path, filename = os.path.split(zip_file) 

    cmd = ["unzip", zip_file, "-d", os.path.join(layers_directory, filename)] 
    log_to_db(2, 0, 0, zip_file)
    spawn(*cmd)
    os.remove(zip_file)
  
  return 1

def create_store_layers():
  current_dir = config['working']['create_layers_dir']
  next_dir = config['working']['create_ta_layers_dir']

  for d in glob.glob(os.path.join(current_dir, '*zip')):
    for yml in glob.glob(os.path.join(d, '*yml')):
      logging.info("Creating store layer for %s" % (yml))
      path, leaf = os.path.split(d) 

      cmd = ["python", config['source']['create_store_layers'], yml]

      company, stores = yaml.load_all(open(yml))
      batch.append((company['id'], len(stores)))
      log_to_db(3, company['id'], len(stores), None)
      spawn(*cmd)

    move_directory(d, next_dir)

  return 1

def create_trade_areas():
  current_dir = config['working']['create_ta_layers_dir']
  next_dir = config['working']['run_proximity_dir']
  count = 0
  for d in glob.glob(os.path.join(current_dir, '*zip')):
    path, leaf = os.path.split(d) 

    for sub in get_sub_directories(d): 
      store_layer = os.path.join(d, sub, 'company', 'layer.shp')
      trade_area_layer = os.path.join(d, sub, 'trade_areas', 'layer.shp')

      prog = config['source']['create_trade_areas']
      cmd = ["python", prog, store_layer, trade_area_layer]
      company_id, store_count = batch[count]
      log_to_db(4, company_id, store_count, sub)
      count = count + 1
      spawn(*cmd)
 
    move_directory(d, next_dir + leaf)

def run_proximity_report():
  old_cwd = os.getcwd()

  current_dir = config['working']['run_proximity_dir']
  next_dir = config['working']['run_demographics_dir']

  count = 0
  for d in glob.glob(os.path.join(current_dir, '*zip')):
    path, leaf = os.path.split(d) 

    for sub in get_sub_directories(d): 
      logging.info("Generating proximity report for %s\\%s\\" % (d, sub))
      company_layer = os.path.join(d, sub, 'company', 'layer.shp')
      competitor_layer = os.path.join(d, sub, 'competition', 'layer.shp')
      output_path = os.path.join(d, sub, 'reports', 'proximity')

      prog = config['source']['create_locator_report']
      cmd = ["python", prog,  company_layer, competitor_layer, output_path, "%s_vs_competitors" % sub]
      company_id, store_count = batch[count]
      log_to_db(5, company_id, store_count, sub)
      count = count + 1
      spawn(*cmd)

    move_directory(d, next_dir + leaf)

  return 1

def run_demographics_report():
  current_dir = config['working']['run_demographics_dir']
  next_dir = config['working']['transform_names_dir']

  count = 0
  for d in glob.glob(os.path.join(current_dir, '*zip')):
    path, leaf = os.path.split(d) 

    for sub in get_sub_directories(d): 
      logging.info("Generating demographics report for %s\\%s\\" % (d, sub))

      trade_areas_layer = os.path.join(d, sub, 'trade_areas', 'layer.shp')
      output_path = os.path.join(d, sub, 'reports')
      
      prog = config['source']['create_demographics_report']

      #demographic report
      cmd = ["python", prog, trade_areas_layer, output_path, '"Demographic and Income Report"']
      company_id, store_count = batch[count]
      log_to_db(6, company_id, store_count, sub)
      spawn(*cmd)

      cmd = ["python", prog, trade_areas_layer, output_path, '"Age by Sex Profile"']
      log_to_db(7, company_id, store_count, sub)
      spawn(*cmd)
      count = count + 1

    move_directory(d, next_dir + leaf)

  return 1

def transform_names():
  current_dir = config['working']['transform_names_dir']
  next_dir = config['working']['zip_dir']

  count = 0
  for d in glob.glob(os.path.join(current_dir, '*.zip')):
    path, leaf = os.path.split(d) 
    changes = [] 
    company_id, store_count = batch[count]
    log_to_db(8, company_id, store_count, None)
    for dirname, dirnames, filenames in os.walk(d):
      for filename in filenames:
        changes.append(unixify(os.path.join(dirname, filename)))
      for subdirname in dirnames:
        changes.append(unixify(os.path.join(dirname, subdirname)))

    changes.reverse()
    for i, tup in enumerate(changes):
      logging.info("Rename [%s] to [%s]" % (tup[0], tup[1]))
      os.rename(tup[0], tup[1])

    move_directory(d, next_dir + leaf)

  return 1

def zip_reports():
  cwd = os.getcwd()

  current_dir = config['working']['zip_dir']
  next_dir = config['working']['ftp_put']

  for zip_file in glob.glob(os.path.join(current_dir, '*.zip')):
    logging.info("Packaging %s" % (zip_file))
    path, leaf = os.path.split(zip_file) 

    target = os.path.join(next_dir, leaf)
    os.chdir(zip_file) 

    cmd = ['zip', '-r', '-ll', target, '*']
    log_to_db(9, 0, 0, zip_file)
    spawn(*cmd)
    os.chdir(cwd)
    shutil.rmtree(zip_file)

  return 1

def put():
  server = config['ftp']['server']
  user = config['ftp']['user'] 
  password = config['ftp']['password'] 
  
  current_dir = config['working']['ftp_put']
  next_dir = config['archive']['outputs']
  remote_directory = config['ftp']['remote_report_directory']

  logging.info("Connecting to ftp server " + server)
  ftp = FTP(server)

  logging.info("Logging in to " + server)
  ftp.login(user, password)
  
  logging.info("Changing to directory " + remote_directory)
  ftp.cwd(remote_directory)

  for zip_file in glob.glob(os.path.join(current_dir, '*.zip')):
    path, file_name = os.path.split(zip_file) 
    logging.info("Pushing file " + zip_file + " to " + remote_directory + "\\" + file_name) 
    log_to_db(10, 0, 0, zip_file)
    fh = open(zip_file, 'rb')
    ftp_binary_put(ftp, file_name + ".tmp", fh)
    ftp.rename(file_name + ".tmp", file_name)
    fh.close()

    move_directory(zip_file, next_dir + file_name)  
  
  ftp.close()
  return 1

############################################################
#                      ENTRY POINT                         #
############################################################
if __name__ == "__main__":
  batch = []
  usage = "usage: %prog --[c]onfig=CONFIG [--label=LABEL] [--single]"
  parser = optparse.OptionParser(usage=usage)
  parser.add_option('-c', '--config', dest='config', help='configuration file used to specify data and src paths')
  parser.add_option('-l', '--label', dest='label', help='label to begin the program at')
  parser.add_option('-s', '--single', action="store_false", dest='single', help='when specified it runs only one section/label from the program')

  (options, args) = parser.parse_args(sys.argv)

  if(options.config == None):
    parser.error("--config option, IS NOT OPTIONAL, ironic eh?")

  #mandatory parameter
  yml = open(options.config)
  config = yaml.load(yml)
  yml.close()

  db_connection = pyodbc.connect(('DRIVER={SQL SERVER};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (config['logging_db']['db_server'], config['logging_db']['database'], config['logging_db']['user'], config['logging_db']['password'])))
  
  label = options.label or 'pull'
  fall = options.single or True

  logging.basicConfig(level=logging.INFO,
                      format='[%(asctime)s](%(threadName)-10s) %(message)s',
                      datefmt='%m%d%Y %H%M%S')

  labels = ["pull", 
            "unzip", 
            "create_store_layers",
            "create_trade_areas",
            "run_proximity_report",
            "run_demographics_report",
            "transform_names",
            "zip_reports",
            "put"]

  for key in labels[labels.index(label):]:
    logging.info("")
    logging.info("=============Starting [%s]================" % (key))
    locals()[key]()
    if(not fall):
      break
