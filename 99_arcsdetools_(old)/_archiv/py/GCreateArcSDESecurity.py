import arcpy
from arcpy import env
import sys
import GArcSDEUtilities

try:
    # 1. the workspace of the database for which the roles, user and permissions should be created
    inWorkspace = sys.argv[1]
    newDataowner = sys.argv[2]
    loginDataowner = sys.argv[3]
    
    env.workspace = inWorkspace
    sdeConn = arcpy.ArcSDESQLExecute(inWorkspace)
    
    assert (len(newDataowner) > 0 or len(loginDataowner) > 0)

    useExistingLogin = False
    SQLStatement = ""
    if (len(loginDataowner) == 0 or loginDataowner=="#"):
        useExistingLogin = True
    else:
        newDataowner = loginDataowner

    GArcSDEUtilities.CreateDBUser(sdeConn, "viewer", "viewer")
    GArcSDEUtilities.AssignNewRoleToUser(sdeConn, "viewer", "R_SDE_VIEWER")

    GArcSDEUtilities.CreateDBUser(sdeConn, "editor", "editor")
    GArcSDEUtilities.AssignNewRoleToUser(sdeConn, "editor", "R_SDE_EDITOR")

    GArcSDEUtilities.CreateDBUser(sdeConn, newDataowner, newDataowner)
    GArcSDEUtilities.AssignDataownerRoleToUser(sdeConn, newDataowner)

    #arcpy.CreateArcSDEConnectionFile_management("", "", "", "", "", "DATABASE_AUTH", "", "*****", "SAVE_USERNAME", "sde.DEFAULT", "SAVE_VERSION")

                
except Exception, ErrorDesc:
    arcpy.AddError( ErrorDesc )
except:
    arcpy.AddError( "Problem executing SQL." )
