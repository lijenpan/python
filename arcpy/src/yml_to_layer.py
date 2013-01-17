import sys
import os
import yaml
import arcview
import arcpy

def create_store_layer(layer_path, store_list):
  print "Creating %s" % (layer_path)

  path, layer_name = os.path.split(layer_path)
  arcpy.env.workspace = path #arcpy fickleness
  arcpy.env.outputCoordinateSystem = r'D:\ArcGIS\Desktop10.0\Coordinate Systems\Geographic Coordinate Systems\North America\NAD 1983.prj'

  arcpy.management.CreateFeatureclass(arcpy.env.workspace, layer_name, "POINT")
  arcpy.management.AddField(layer_name, 'address', 'TEXT')
  arcpy.management.AddField(layer_name, 'city', 'TEXT')
  arcpy.management.AddField(layer_name, 'state', 'TEXT')
  arcpy.management.AddField(layer_name, 'zip_code', 'TEXT')

  point = arcpy.CreateObject("POINT")
  rows = arcpy.InsertCursor(layer_name)

  for store in store_list:
    if verbose:
      print "Loading store id: %s" % (repr(store['id']))

    addr = store['address']
    point.X = addr['longitude']
    point.Y = addr['latitude']

    r = rows.newRow()
    r.Shape = point
    r.Id = store['id']

    #the following information is needed for the proximity report to operate correctly
    #an esri bug requires it, but we leave the data blank so that there isn't confusion
    #concerning the fact that the geocoding is coming from the lat and long values
    r.city = "%s" % (addr['municipality'])
    r.address = "%s %s" % (addr['street_number'], addr['street'])
    r.state = "%s" % (addr['governing_district'])
    r.zip_code = "%s" % (addr['postal_area'])

    rows.insertRow(r)
    del r

  del rows
  arcpy.management.AddXY(layer_name)

  return 1

########################################ENTRY POINT######################################
if len(sys.argv) < 2:
  sys.exit("Must provide yml file to translate to table")

path, file_name = os.path.split(sys.argv[1])
verbose = False
if len(sys.argv) >= 3:
  verbose = True

company, stores = yaml.load_all(open(os.path.join(path, file_name)))

company_id = company['id']

root = os.path.join(path, repr(company_id))
dir_company = os.path.join(root, 'company')
dir_competition = os.path.join(root, 'competition')

#make directories to hold created layers
for d in [root, dir_company, dir_competition]:
  if not os.path.exists(d):
    print "Creating directory %s" % (d)
    os.makedirs(d)

#derived shape file names
company_shape_file = os.path.join(dir_company, "layer.shp")
competition_shape_file = os.path.join(dir_competition, "layer.shp")

#create layers
create_store_layer(company_shape_file, company['stores'])
create_store_layer(competition_shape_file, stores)
