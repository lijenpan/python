import sys
import traceback
import glob
import os
import itertools

def help():
    print
    print "Program used to 10 minute create trade area for given store layer."
    print "e.g. [python create_trade_areas.py store_layer output_layer]\n"
    print "\t-store_layer: the layer we'll use to gather center points from, must have a column labeled 'id'"
    print "\t-output_layer: the directory and filename of the generated trade layer"
    print

try:
  if len(sys.argv) != 3:
    help()
    sys.exit(1)

  store_layer = sys.argv[1]
  output_layer = sys.argv[2]
  id_field = 'Id'

  drive_time_distance = 10

  print "Importing arcview and arcpy."
  import arcview
  import arcpy
  print "Checking out extension and toolbox."
  arcpy.ImportToolbox(r"d:\ArcGIS\Desktop10.0\ArcToolbox\Toolboxes\Business Analyst Tools.tbx")
  arcpy.CheckOutExtension("Business")
  arcpy.CheckOutExtension("Network")

  print "Creating %s Minute Trade Areas @ [%s]" % (drive_time_distance, output_layer)
  arcpy.ba.DriveTime(store_layer, id_field, "ALL", "10", "Minutes", output_layer)

  print "Checking in extension."
  arcpy.CheckInExtension("Business")

except Exception as e:
  print e
  raise e

exit(0)
