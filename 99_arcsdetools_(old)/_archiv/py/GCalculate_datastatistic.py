# -*- coding: cp1252 -*-

# Description: Parse all Featureclasses and table of one database and write
# information in a file:
# Number of Features, Spatial Reference Info, Versioning, Attributive index etc.

# Author: Markus Schenardi
# Date: May 2013
#


# Import system modules
import arcpy
from arcpy import env
import csv
import string

#set path and filename to database-connectionfile for SDE

#workspace= "D:/arcproj/GEONISServer60/datasources/sew_industry/labat_industry_sew_sde.sde"
workspace = r"\\vsdev4003\c$\temp\vsdev4015_TEST_H_2_TEST_H_2_OWNER.sde"

#for use with Toolbox: uncomment the next line and configure parameter "workspace" in the tool
#workspace = sys.argv[1]


resultfile= "c:/temp/test.csv"
#resultfile = sys.argv[2]


#DO NOT CHANGE FROM HERE
########################

#Dictionary um die Anzahl Objekte zu speichern
#zwei spalten: "input",featureclassname. Wert = count
TableObjectCount={}

def DescribeFCTable(inputname,inputobject,inputtype):
#inputname: will be in the log as 1st value
#inputobject: featureclass or table object
#inputtype: "featureclass" or "table"


#Featureclassname ohne Qualifier
    nameList=inputobject.split(".")
    inputobjectname=nameList[len(nameList)-1]


    try:
        #Describe Info
        desc = arcpy.Describe(inputobject)

        print desc.dataType

        #nur fuer Featureclassen mit Typ FeatureClass oder Annotation
        if desc.dataType=="FeatureClass" or desc.dataType=="Annotation" or desc.dataType=="Table":

            #Count features
            try:
                arcpy.Delete_management("inputselect", "")
            except:
                pass

            try:
                if inputtype=="featureclass":
                    arcpy.MakeFeatureLayer_management(inputobject,"inputselect")
                else:
                    arcpy.MakeTableView_management(inputobject,"inputselect")

                objectcount = str(arcpy.GetCount_management("inputselect"))
            except:
                #Falls makeFeatureLayer oder TableView nicht funktioniert
                #z.B. wegen GRID
                objectcount = -99
            #speichere in Dictionary
            TableObjectCount[inputobjectname]=objectcount

            #collect information for featureclass
            #Spatial Reference, Versionierung
            if inputtype=="featureclass":
                srname=desc.SpatialReference.name
                srxyresolution=desc.SpatialReference.XYResolution
                srxytolerance=desc.SpatialReference.XYTolerance
                srisHighPrecision = str(desc.SpatialReference.isHighPrecision)
                try:
                    hasspatialindex = str(desc.hasSpatialIndex)
                except:
                    hasspatialindex = "not available"
            else:
                srname=""
                srxyresolution=""
                srxytolerance=""
                srisHighPrecision = ""
                hasspatialindex = ""


            isversioned = str(desc.isVersioned)

            outputstring=inputname + ";" + inputobject + ";" + inputobjectname + ";" + objectcount + ";" + srname + ";" + str(srxyresolution) + ";" + str(srxytolerance) + ";" + srisHighPrecision
            outputstring = outputstring + ";" + isversioned + ";" + hasspatialindex


            #Attributive Indizes
            inputobjectIndixes=arcpy.ListIndexes(inputobject)

            indexstring=""
            for index in inputobjectIndixes:
                indexstring=indexstring + index.name + "("

                for field in index.fields:
                    indexstring=indexstring + field.name + ","


                indexstring = indexstring.rstrip(",") + "),"

            outputstring=outputstring + ";" + indexstring.rstrip(",")

        else:

            outputstring=inputobject

    except:
        outputstring=inputobject

    return outputstring


def calcstatistics(sdeworkspace,resultfile):
#Funktion liefert diverse Informationen zu Featureclass oder Tabelle
#Resultat ist ein String der dann in ein File geschrieben werden kann: Parameter resultfile

    f = open(resultfile,'w')

    headerline = "type,dataset;fcnameQualified;fcname;objectcount;spatialreference;xyresolution;xytolerance;isHighPrecision;isversioned;hasspatialindex;attributeindexes"
    f.write(headerline + "\n")


    #wstype = original oder target

    env.workspace=sdeworkspace
    tableList = arcpy.ListTables()
    #for table in tableList:
        #desc = arcpy.Describe(table)

        #arcpy.MakeTableView_management(infeatureclass, "inputselect", "[DATE_MODIFIED] > " + datestamp + " OR [DATE_MODIFIED] IS NULL")


    #Fuer Datasets
    datasetlist = arcpy.ListDatasets("*", "Feature")
    for dataset in datasetlist:

        #Fuer Featureclasses im Dataset
        fcList = arcpy.ListFeatureClasses("","",dataset)

        for fc in fcList:
            print fc
            arcpy.AddMessage(fc)

            describeresult=DescribeFCTable("dataset:" + dataset,fc,"featureclass")
            f.write(describeresult+ "\n")
            print describeresult

    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        print fc
        arcpy.AddMessage(fc)
        describeresult=DescribeFCTable("featureclass",fc,"featureclass")
        f.write(describeresult+ "\n")
        print describeresult
    tablelist = arcpy.ListTables()
    for table in tablelist:
        print table
        arcpy.AddMessage(table)
        describeresult=DescribeFCTable("table",table,"table")
        f.write(describeresult+ "\n")
        print describeresult


    #Resultatfile schliessen
    f.close()



#MAINscript
#---------------------------------

#Analyse
calcstatistics(workspace,resultfile)

