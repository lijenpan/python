import sys
import traceback
import glob
import os
import itertools

print "Importing arcview and arcpy."
import arcview
import arcpy

def help():
    print
    print "Used to generate locator reports between a company and it's competitors."
    print "e.g. [python trade_area.shp output_directory report_type]\n"
    print "\t-trade_aray.shp: layer file with appropriate trade area information"
    print "\t-output_directory: directory to store generated report to"
    print "\t-report_type: e.g. 'Demographic and Income Report' or 'Age by Sex Profile'"
    print

try:
  if len(sys.argv) != 5:
    help()
    sys.exit(1)

  company = sys.argv[1]
  competitor = sys.argv[2]
  report_path = sys.argv[3]
  report_name = sys.argv[4]

  drive_time_distance = 10
  drive_time_miles = "%s miles" % (drive_time_distance)
  report_format = 's.xml'

  # check out any necessary licenses
  print "Checking out extension and toolbox."
  arcpy.ImportToolbox(r"d:\ArcGIS\Desktop10.0\ArcToolbox\Toolboxes\Business Analyst Tools.tbx")
  arcpy.CheckOutExtension("Business")
  arcpy.CheckOutExtension("Network")

  flds = "Name:id;Address:address;City:city;State:state;ZIP:zip_code;State:state"

  print "Running report " + report_name
  arcpy.ba.LocatorReport(company, "id", "id", competitor, flds, "PORTRAIT", "ALL", "", "", "LIMIT_WITHIN_DISTANCE", drive_time_miles, "", "DRIVE_TIME", "DONT_ADD_DISTANCE", "USE_EXISTING", "", "CREATE_REPORT", report_name, report_path, "DONT_CREATE_OUT_FEATURECLASS", "", "", report_format)

  print "Checking in extension."
  arcpy.CheckInExtension("Business")

except Exception as e:
  print e
  raise e

exit(0)
