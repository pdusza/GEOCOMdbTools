#-*- coding: utf-8 -*-
'''
Created on 19.09.2011

@author: zid
@attention: Beta
'''
import arcpy
from arcpy import env
import os
from string import upper

env.workspace = arcpy.GetParameterAsText(0)  #"K:/ESRI/Arcproj/datasources/Wacker_Kanal_SDE_SQL/db/DC_kanal_10.sde"

arcpy.AddMessage("Register tables")
tableList = arcpy.ListTables()
for table in tableList:
	try:
		arcpy.RegisterAsVersioned_management( table, "NO_EDITS_TO_BASE")
		arcpy.AddMessage(table + " registered")
	except Exception, ErrorDesc:
		arcpy.AddError( ErrorDesc )	

arcpy.AddMessage("Register Datasets")
datasetlist = arcpy.ListDatasets("*", "Feature")
for dataset in datasetlist:
	try:
		arcpy.RegisterAsVersioned_management( dataset, "NO_EDITS_TO_BASE")
		arcpy.AddMessage(dataset + " registered")
	except Exception, ErrorDesc:
		arcpy.AddError( ErrorDesc )

arcpy.AddMessage("Register Featureclasses")
featureclassList = arcpy.ListFeatureClasses("*")
for featureclass in featureclassList:
	try:
		arcpy.RegisterAsVersioned_management( featureclass, "NO_EDITS_TO_BASE")
		arcpy.AddMessage( featureclass + " registered")
	except Exception, ErrorDesc:
		arcpy.AddError( ErrorDesc )
	
arcpy.AddMessage("end of script.")
