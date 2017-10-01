# Name: UnregisterAsVersioned_Example.py
# Description: removes all spatial indizes from feature classes
# Author: Markus Schenardi
# Date: 22.11.2012
# tested with ArcGIS 10 SP4
#


# Import system modules
import arcpy
import sys
from arcpy import env
import re

##inputworkspace="d:/GEONIS/av_lux_V5_0_1_ArcGIS10TEST IMPORT.mdb"
inputworkspace=sys.argv[1]

env.workspace = inputworkspace


datasetlist = arcpy.ListDatasets("*", "Feature")
for dataset in datasetlist:
    

    fcList = arcpy.ListFeatureClasses("","",dataset)

    for fc in fcList:

        try:
            arcpy.RemoveSpatialIndex_management(fc)
            arcpy.AddMessage(fc + ": Index removed")
        except: 
            arcpy.AddMessage(fc + " does not have a spatial index")
        


#import standalone Featureclasses
fcList = arcpy.ListFeatureClasses("","","")

for fc in fcList:
  
    try:
        arcpy.RemoveSpatialIndex_management(fc)
        arcpy.AddMessage(fc + ": Index removed")
    except:
        arcpy.AddMessage(fc + " does not have a spatial index")






arcpy.AddMessage("end of script.")

