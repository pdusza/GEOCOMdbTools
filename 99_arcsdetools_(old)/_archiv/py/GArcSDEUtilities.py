'''
Created on 13.02.2012

@author: spc
'''

import arcpy

# executes the list of sql DDL in SQLStatement against the sde connection sdeConn
def ExecuteDDL(sdeConn, SQLStatement):
    SQLStatementList = SQLStatement.split(";")
    
    # For each SQL statement passed in, execute it.
    for sql in SQLStatementList:
        arcpy.AddMessage("Execute SQL Statement: " + sql)
        try:
            # Pass the SQL statement to the database.
            sdeConn.execute(sql)
            arcpy.AddMessage( "SQL statement: " + sql + " ran sucessfully." )
        except Exception, ErrorDesc:
            arcpy.AddWarning( "SQL statement: " + sql + " FAILED.")
            arcpy.AddError( ErrorDesc )
                
# executes a select statements and returns a list of results. If not records
# are found with query an empty list is returned
def ExecuteQuery(sdeConn, SQLStatement):

    try:
        sdeReturn = sdeConn.execute(SQLStatement)
        if isinstance(sdeReturn, bool):
            sdeReturn = True 
        elif not(isinstance(sdeReturn, list)):
            sdeReturn = [sdeReturn]
    except Exception, ErrorDesc:
        arcpy.AddWarning( "SQL statement: " + SQLStatement + " FAILED.")
        arcpy.AddError( ErrorDesc )
        sdeReturn = False
        
    return sdeReturn


def CreateSDEConnectionFile():
    # Local variables:
    whereToSaveIt = "whereToSaveIt"
    serverName = ""
    theDatabase = ""
    userName = ""
    userPwd = ""
    sdeConnectionName = serverName + "_" + theDatabase + "_" + userName
    # Process: Create ArcSDE Connection File
    arcpy.CreateArcSDEConnectionFile_management(whereToSaveIt, sdeConnectionName, serverName, "theService", theDatabase, \
                                                "DATABASE_AUTH", userName, userPwd, "SAVE_USERNAME", "sde.DEFAULT", "SAVE_VERSION")

def AssignNewRoleToUser(sdeConn, user, role):
    SQLStatement = "SELECT name FROM sysusers WHERE (issqlrole = 1 or isapprole = 1) " \
                    "AND name = '{0}'".format(role)
    res = ExecuteQuery(sdeConn, SQLStatement)
    if not(isinstance(res, list)):
        ExecuteDDL(sdeConn, "create role [{0}]".format(role))
        
    ExecuteDDL(sdeConn, "EXEC sp_addrolemember N'{0}', N'{1}'".format(role, user))
    
    
def AssignDataownerRoleToUser(sdeConn, user):
    try:
        AssignNewRoleToUser(sdeConn, user, "r_sde_owner")
        SQLStatement = "GRANT CREATE FUNCTION TO [r_sde_owner];" \
            "GRANT CREATE PROCEDURE TO [r_sde_owner];" \
            "GRANT CREATE TABLE TO [r_sde_owner];" \
            "GRANT CREATE VIEW TO [r_sde_owner]"
        ExecuteDDL(sdeConn, SQLStatement)
    except Exception, ErrorDesc:
        arcpy.AddError( ErrorDesc )


def CreateDBUser(sdeConn, user, pwd):
    SQLStatement = "SELECT name FROM master.sys.syslogins WHERE name = '{0}'".format(user)
    res = ExecuteQuery(sdeConn, SQLStatement)
    if not(isinstance(res, list)):
        SQLStatement = "CREATE LOGIN [{0}] WITH PASSWORD=N'{1}', DEFAULT_DATABASE=[master], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF".format(user, pwd)
        ExecuteDDL(sdeConn, SQLStatement)
        
    SQLStatement = "SELECT name FROM sys.sysusers WHERE name = '{0}'".format(user)
    res = ExecuteQuery(sdeConn, SQLStatement)
    if not(isinstance(res, list)):
        SQLStatement = "CREATE USER [{0}] FOR LOGIN [{0}] WITH DEFAULT_SCHEMA=[{0}];".format(user)
        SQLStatement = SQLStatement + "CREATE SCHEMA [{0}] AUTHORIZATION [{0}]".format(user)
        ExecuteDDL(sdeConn, SQLStatement)
    

# returns a list of logins for a sql server instance, defined by sde connection sdeConn
def GetInstanceUsersSQLServer(sdeConn):
    sqlStatement = "select name from master.sys.syslogins where name not in ('sa','sde') " \
              "and name not like '##%' and password is not null " \
              "order by name"
    
    logins = []
    try:
        # Pass the SQL statement to the database.
        sdeReturn = sdeConn.execute(sqlStatement)
    except Exception, ErrorDesc:
        arcpy.AddError( ErrorDesc )
    
    for row in sdeReturn:
        logins.append(row[0])

    return logins