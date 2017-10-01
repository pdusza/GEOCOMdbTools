# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        gc_egdb_unreg_as_ver
# Purpose:     This script register all FeatureClasses and Tables in a given SDE as versioned.
#              Defined exceptions are not registered as versioned (for example GN-tables)
#
# Author:      tbu
#
# Created:     15.12.2015
# Modified:    05.03.2016
# Copyright:   (c) GEOCOM Informatik AG
# Licence:     no license
#-------------------------------------------------------------------------------

import os, sys, arcpy
from arcpy import env
import re

def message(messageText, severity=0):
        '''zur Ausgabe auf der Konsole'''
        #print messageText
        '''zur Ausgabe in ArcGIS'''
        if severity == 0:
            arcpy.AddMessage(messageText)
        if severity == 1:
            arcpy.AddWarning(messageText)
        if severity == 2:
            arcpy.AddError(messageText)


def main(workspace):

    env.workspace = workspace

    dsList = []
    datasetlist = arcpy.ListDatasets("*", "Feature")
    for dataset in datasetlist:
        dsList.append(dataset)
    fcList = arcpy.ListFeatureClasses()
    for fc in fcList:
        dsList.append(fc)
    tableList = arcpy.ListTables()
    for table in tableList:
        dsList.append(table)

    #message(dsList)

    for ds in dsList:
        desc = arcpy.Describe(ds)
        if desc.isVersioned:
            try:
                message(("unregistering as versioned: " + "\"" + ds + "\""),0)
                arcpy.UnregisterAsVersioned_management(ds, "NO_KEEP_EDIT", "COMPRESS_DEFAULT")
            except:
                message(("problem with unregistering: " + "\"" + ds + "\"" + '\n' + arcpy.GetMessages(2)),2)
        else:
            message(("--- already unregistered as versioned: " + "\"" + ds + "\""),0)


# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE,
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':
    # Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    main(*argv)
