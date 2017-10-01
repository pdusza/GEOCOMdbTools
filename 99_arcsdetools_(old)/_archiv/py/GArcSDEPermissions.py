# ==============================================================================
# Aufruf: VersionSDE.py   <...>
# Zweck:  Kopiert GDB
# GEOCOM Informatik AG
# ==============================================================================
# datum       wer       anpassungen
# --------------------------------------
# 2012-02-11, wap       erstellt
# 2012-02-12, wap       angepasst und getestet
# 2012-02-20, spc       adjusted for toolbox use
# ==============================================================================
# Import system modules
import sys, time, os, arcpy
from arcpy import env

# ==============================================================================
# wrapper functions
def ChangePrivileges_wrapper(in_dataset, user, View, Edit):
    try:
        arcpy.ChangePrivileges_management (in_dataset, user, View, Edit)
        return None
    except:
        print sys.exc_info()[1]
        return in_dataset

def deleteDoublesFromList(objlist):
    try:
#   Python 2.5 or later
        return list(set(objlist))
    except:
        return objlist

# ==============================================================================
# Check commandline-parameters


# ==============================================================================
sourcedb = sys.argv[1]

extension = os.path.splitext(sourcedb)[1].lower()
if extension == ".sde":
    sourcewstype = "SDE"
else:
    arcpy.AddError("Error:  Inputfile-Endung \"" + extension + "\" nicht unterstuetzt, Abbruch.")
    exit

# Set workspace to folder containing geodatabases
#env.workspace = os.path.dirname(sourcedb)

# Set workspace to current geodatabase
env.workspace = sourcedb
errList = []

# Setting Rights to GDB, tables, feature classes, datasets
arcpy.AddMessage("Setting privileges for data from \"" + sourcedb + "\"")

# Identify feature classes
for fcTabDatset in arcpy.ListFeatureClasses():
    arcpy.AddMessage("Setting privileges for feature class \"" + fcTabDatset + "\"")
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "REVOKE", "REVOKE")
    if tmp <> None:
        errList.append(tmp)
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_EDITOR", "GRANT", "GRANT")
    if tmp <> None:
        errList.append(tmp)
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "GRANT", "AS_IS")
    if tmp <> None:
        errList.append(tmp)

# Identify tables
for fcTabDatset in arcpy.ListTables():
    arcpy.AddMessage("Setting privileges for table \"" + fcTabDatset + "\"")
    fcTabDatsetList = fcTabDatset.split(".",100)
    fcTabDatsetShort = fcTabDatsetList[len(fcTabDatsetList)-1]
    if fcTabDatsetShort.upper() in ('GN_WORKPACKET'):
        tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_EDITOR", "GRANT", "GRANT")
        if tmp <> None:
            errList.append(tmp)
        tmp = ChangePrivileges_wrapper(fcTabDatset, "A_USER", "GRANT", "GRANT")
        if tmp <> None:
            errList.append(tmp)
    else:
        tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "REVOKE", "REVOKE")
        if tmp <> None:
            errList.append(tmp)
        tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_EDITOR", "GRANT", "GRANT")
        if tmp <> None:
            errList.append(tmp)
        tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "GRANT", "AS_IS")
        if tmp <> None:
            errList.append(tmp)

# Identify datasets, will include contents of datasets
for fcTabDatset in arcpy.ListDatasets():
    arcpy.AddMessage("Setting privileges for dataset \"" + fcTabDatset + "\"")
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "REVOKE", "REVOKE")
    if tmp <> None:
        errList.append(tmp)
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_EDITOR", "GRANT", "GRANT")
    if tmp <> None:
        errList.append(tmp)
    tmp = ChangePrivileges_wrapper(fcTabDatset, "R_SDE_VIEWER", "GRANT", "AS_IS")
    if tmp <> None:
        errList.append(tmp)

# ==============================================================================
if len(errList) > 0:
    errList = deleteDoublesFromList(errList)
    arcpy.AddError("Errorsummary: ", len(errList), " errors")
    for fcTabDatset in errList:
        arcpy.AddError("  Error: Could not set Permission \"" + fcTabDatset + "\"")
