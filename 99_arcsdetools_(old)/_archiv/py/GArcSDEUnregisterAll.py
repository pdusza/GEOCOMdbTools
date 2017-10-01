# Name: UnregisterAsVersioned_Example.py
# Description: Unregisters a dataset as versioned
# Author: Markus Schenardi
# Date: 18.02.2011
# tested with ArcGIS 10 SP1
#
# Script "unregisters as versioned" all Featuredatasets and tables inside the SDE Geodatabase

# Import system modules
import arcpy
from arcpy import env
import sys

#set path and filename to database-connectionfile for SDE 
#env.workspace = "D:\\GEONIS\\datasources\\NAILA_PCN_OWNER\\db\\naila_db_web.naila_pcn_OWNER.sde"
env.workspace=sys.argv[1]

arcpy.AddMessage("Unregister Datasets")

datasetlist = arcpy.ListDatasets("*", "Feature")
for dataset in datasetlist:
    
    # Set local variables
    datasetName = (env.workspace  + "/" + dataset)
    arcpy.AddMessage("Dataset: " + datasetName)

    # get description of the table
    desc = arcpy.Describe(datasetName)
    
    #run only, if dataset is versioned 
    if desc.isversioned:
        # Execute UnregisterAsVersioned
        arcpy.UnregisterAsVersioned_management( datasetName, "NO_KEEP_EDIT", "COMPRESS_DEFAULT")
        arcpy.AddMessage(dataset + " unregistered")

print "Unregister Featureclasses outside dataset"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    arcpy.AddMessage(fc)

    # Set local variables
    FCName = (env.workspace  + "/" + fc)

    try:
        # get description of the table
        desc = arcpy.Describe(FCName)
        
        #run only, if dataset is versioned 
        if desc.isversioned:
            # Execute UnregisterAsVersioned
            arcpy.UnregisterAsVersioned_management( FCName, "NO_KEEP_EDIT", "COMPRESS_DEFAULT")
            arcpy.AddMessage(fc + " unregistered")


    except:
        arcpy.AddMessage("cannot handle: " + fc)


print "Unregister tables"
tableList = arcpy.ListTables()
for table in tableList:
    arcpy.AddMessage(table)

    # Set local variables
    datasetName = (env.workspace  + "/" + table)

    try:
        # get description of the table
        desc = arcpy.Describe(datasetName)
        
        #run only, if dataset is versioned 
        if desc.isversioned:
            # Execute UnregisterAsVersioned
            arcpy.UnregisterAsVersioned_management( datasetName, "NO_KEEP_EDIT", "COMPRESS_DEFAULT")
            arcpy.AddMessage(table + " unregistered")


    except:
        arcpy.AddMessage("cannot handle: " + table)

print "end of script."

