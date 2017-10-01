# Name: UnregisterAsVersioned_Example.py
# Description: Registers data as versioned unless it is listed in the exclude list
# Author: Markus Schenardi
# Date: 25.07.2012
# tested with ArcGIS 10 SP4
#


# Import system modules
import arcpy
import sys
from arcpy import env
import re


def checkexception(inputobject):
    exceptionlist=[]
    
    #regexausdruecke verwenden fuer den hinteren Teil nach dem Qualifier
    #.+ bedeutet: beliebige Zahl an Zeichen oder _

    #exceptionlist.append("DBMS.+")
    #exceptionlist.append("WLM.+")
    #exceptionlist.append("UM.+")
    exceptionlist.append("GN.+")
    #exceptionlist.append("AVS.+")

  

    register = 1


    #Teile vollstaendigen Namen in seine Teile
    #SQL Server: DB-Name, Owner, Name
    #Oracle: Owner, Name

    nameList=inputobject.split(".")

    #Name ohne Qualifier
    featurename=nameList[len(nameList)-1]

    #Pruefe, ob das Inputobjekt versioniert werden soll oder nicht

    for exception in exceptionlist:
        if re.match(exception ,featurename,re.IGNORECASE):
              register = 0
    return register


def createmessage(messagetext):
    #Writes messages to the Toolbox-Window and the console
    arcpy.AddMessage(messagetext)
    print(messagetext)



# ==============================================================================
#Main Script

#set path and filename to database-connectionfile for SDE 

#sourcedb=r"D:\temp\labat.scm_sandbox.OWNER.sde"

sourcedb=sys.argv[1]

env.workspace = sourcedb


createmessage("Register Datasets as versioned")

datasetlist = arcpy.ListDatasets("*", "Feature")
for dataset in datasetlist:

    # Set local variables
    datasetName = (env.workspace  + "/" + dataset)
    createmessage(dataset)
    


    #Pruefe auf Exception
    registerdataset=checkexception(dataset)


    # Execute RegisterAsVersioned
    if registerdataset==1:


        # get description of the Dataset
        desc = arcpy.Describe(datasetName)
        
        #run only, if dataset is versioned 
        if not desc.isversioned:
        
            createmessage("register " + datasetName)
            try:
                arcpy.RegisterAsVersioned_management( datasetName, "NO_EDITS_TO_BASE")
                createmessage(dataset + " registered")
            except:
                createmessage("not able to register: " + dataset)
        else:
            createmessage(dataset + " already registered as versioned")
    else:
        createmessage("exception-Rule. Do no register " + datasetName)


createmessage("Register featureclasses as versioned")
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    # Set local variables
    fcName = (env.workspace  + "/" + fc)

    #Pruefe auf Exception
    registerfc=checkexception(fc)

    # Execute RegisterAsVersioned
    if registerfc==1:

        # get description of the Dataset
        desc = arcpy.Describe(fcName)
        #run only, if Featureclass is versioned 
        if not desc.isversioned:
            
            createmessage("register " + fc)
            try:
                arcpy.RegisterAsVersioned_management( fcName, "NO_EDITS_TO_BASE")
                createmessage(fc + " registered")
            except:
                createmessage("not able to register: " + fc)
        else:
            createmessage(fc + " already registered as versioned")
    else:
        createmessage("exception-Rule. Do no register " + fc)

createmessage("Register tables as versioned")
tableList = arcpy.ListTables()
for table in tableList:
    # Set local variables
    tableName = (env.workspace  + "/" + table)

    #Pruefe auf Exception
    registertable=checkexception(table)

    # Execute RegisterAsVersioned
    if registertable==1:

        # get description of the Table
        desc = arcpy.Describe(tableName)
        
        #run only, if dataset is versioned 
        if not desc.isversioned:
        
            createmessage("register " + table)
            try:
                arcpy.RegisterAsVersioned_management( tableName, "NO_EDITS_TO_BASE")
                createmessage(table + " registered")
            except:
                createmessage("not able to register: " + table)
        else:
            createmessage(table + " already registered as versioned")
    else:
        createmessage("exception-rule. Do no register " + table)


createmessage("end of script.")


