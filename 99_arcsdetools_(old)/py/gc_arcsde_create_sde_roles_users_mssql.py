#-------------------------------------------------------------------------------
# Name:        gc_arcsde_mssql_create_sde_roles_users
# Purpose:     creates
#
# Author:      tbu
#
# Created:     07.02.2015
# Modified:    10.10.2016 (tbu)
# Copyright:   (c) GEOCOM Informatik AG 2016
# Licence:     no license
#-------------------------------------------------------------------------------

import os, sys, pypyodbc, arcpy, datetime
import gc_sql_utils
sys.path.append("/py")

'''-------------------------------------------------------------------------------
# Simple messaging
-------------------------------------------------------------------------------'''
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
'''-------------------------------------------------------------------------------
# Create Connection to MSSQL-Server with pypyodbc
-------------------------------------------------------------------------------'''
def createConn(instance,dbms_admin,dbms_admin_pwd):
    try:
        if dbms_admin_pwd != '':
            cnnctnstring = 'DRIVER={0};SERVER={1};DATABASE=master;UID={2};PWD={3}'.format('SQL Server',instance,dbms_admin,dbms_admin_pwd)
        else:
            cnnctnstring = 'DRIVER={0};SERVER={1};DATABASE=master;Trusted_Connection=Yes'.format('SQL Server',instance)
        cnnctn = pypyodbc.connect(cnnctnstring, autocommit=True)
        cursor = cnnctn.cursor()
        return cursor
    except pypyodbc.Error, msg:
        arcpy.AddError(msg)
    except Exception as e:
        print e.args[0]
        arcpy.AddError(e.args[0])
'''-------------------------------------------------------------------------------
# Execute T-SQL
-------------------------------------------------------------------------------'''
def executeSQL(sql,instance,dbms_admin,dbms_admin_pwd):
    cursor = createConn(instance,dbms_admin,dbms_admin_pwd)
    try:
        arcpy.AddMessage(sql)
        cursor.execute(sql)
    except pypyodbc.Error, msg:
        arcpy.AddError(msg)
	pass
'''-------------------------------------------------------------------------------
# Execute Select Statements with result
-------------------------------------------------------------------------------'''
def select(sql,instance,dbms_admin,dbms_admin_pwd):
    cursor = createConn(instance,dbms_admin,dbms_admin_pwd)
    try:
        cursor.execute(sql)
    except pypyodbc.Error, msg:
        arcpy.AddError(msg)
    return cursor.fetchone()
'''-------------------------------------------------------------------------------
# Create SDE User Login
-------------------------------------------------------------------------------'''
def createSDELogin(instance,dbms_admin,dbms_admin_pwd,gdb_admin_pwd):
    if (select(gc_sql_utils.selSDEuserExists,instance,dbms_admin,dbms_admin_pwd)) > 0:
        arcpy.AddWarning('Login '"'sde'"' already exists')
    else:
        arcpy.AddMessage('Create login '"'sde'"'')
        sql = gc_sql_utils.createSDELogin.format(gdb_admin_pwd=gdb_admin_pwd)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
'''-------------------------------------------------------------------------------
# Create Database
-------------------------------------------------------------------------------'''
def createDB(instance,database,dbms_admin,dbms_admin_pwd,dbsize,dbgrowth,dblogsize,dbloggrowth,recoverymodel):
    sql = gc_sql_utils.selDefaultDataPath
    datapath = select(sql,instance,dbms_admin,dbms_admin_pwd)
    arcpy.AddMessage('The DB-Datafile will be stored under the default DATA-path: ' + datapath[0])
    arcpy.AddMessage("++++++++++++++++++")

    sql = gc_sql_utils.selDefaultLogPath
    logpath = select(sql,instance,dbms_admin,dbms_admin_pwd)
    arcpy.AddMessage('The DB-Logfile will be stored under the default LOG-path: ' + logpath[0])
    arcpy.AddMessage("++++++++++++++++++")

    if (select(gc_sql_utils.selDbExists.format(dbName=database),instance,dbms_admin,dbms_admin_pwd)) > 0:
        arcpy.AddWarning('Database ' + "'" + database + "'"+ ' already exists')
    else:
        arcpy.AddMessage('Create Database ' + database)
        sql = gc_sql_utils.createDB.format(dbName=database,dbSize=dbsize,dbGrowth=dbgrowth,logSize=dblogsize,logGrowth=dbloggrowth,recoveryModel=recoverymodel,dbDataPath=datapath[0],dbLogPath=logpath[0])
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
'''-------------------------------------------------------------------------------
# Create Database Connection File
-------------------------------------------------------------------------------'''
def createDBConnectionFile(instance,database_type,database,account_authentication,dbms_admin,dbms_admin_pwd):
    # Local variables
    instance_temp = instance.replace("\\","_")
    instance_temp = instance_temp.replace("/","_")
    instance_temp = instance_temp.replace(":","_")
    Conn_File_NameT = instance_temp + "_" + database + "_" + dbms_admin

    if os.environ.get("TEMP") == None:
        temp = "c:\\temp"
    else:
        temp = os.environ.get("TEMP")

    if os.environ.get("TMP") == None:
        temp = "/usr/tmp"
    else:
        temp = os.environ.get("TMP")

    Connection_File_Name = Conn_File_NameT + ".sde"
    Connection_File_Name_full_path = temp + os.sep + Conn_File_NameT + ".sde"

    # Check for the .sde file and delete it if present
    arcpy.env.overwriteOutput=True
    if os.path.exists(Connection_File_Name_full_path):
        os.remove(Connection_File_Name_full_path)

    try:
        arcpy.AddMessage("Creating Database Connection File...")
        # Process: Create Database Connection File...
        # Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, account_authentication, username, password, database, save_username_password(must be true)
        arcpy.CreateDatabaseConnection_management(out_folder_path=temp, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbms_admin, password=dbms_admin_pwd, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
            if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
                arcpy.AddReturnMessage(i)
                arcpy.AddMessage("++++++++++++++++++")
                arcpy.AddMessage("Exiting!!")
                arcpy.AddMessage("++++++++++++++++++")
                sys.exit(3)
            else:
                arcpy.AddReturnMessage(i)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
    connection = Connection_File_Name_full_path
    return connection
'''-------------------------------------------------------------------------------
# Create Database Roles
-------------------------------------------------------------------------------'''
def createDBRole(connection,role):
    try:
        arcpy.AddMessage('Creating database role ' + role)
        arcpy.CreateRole_management(input_database=connection, grant_revoke='GRANT', role=role,  user_name='')
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
'''-------------------------------------------------------------------------------
# Create Database Roles SQL (FIX for 10.4 because of a BUG)
-------------------------------------------------------------------------------'''
def createDBRoleSQL(instance,database,dbms_admin,dbms_admin_pwd,role):
    try:
        arcpy.AddMessage('Creating database role ' + role)
        sql = gc_sql_utils.createRole.format(database=database, role=role)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
'''-------------------------------------------------------------------------------
# Create Database User
-------------------------------------------------------------------------------'''
def createDBUser(database,connection,dbuser_pwd,role):
    #if dbuser_pwd != '':
    #    dbuser_pwd = database.lower() + '_' + role.upper() + '_' + str(datetime.datetime.now().year)
    #   arcpy.AddWarning('No password specified. Setting the password to: ' + dbuser_pwd)
    try:
        dbuser = (database + '_' + role).upper()
        role = 'R_SDE_' + role.upper()
        arcpy.AddMessage('Creating database user ' + dbuser)
        arcpy.CreateDatabaseUser_management(input_database=connection, user_authentication_type='DATABASE_USER', user_name=dbuser, user_password=dbuser_pwd, role=role, tablespace_name='')
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
'''-------------------------------------------------------------------------------
# Change Permissions
-------------------------------------------------------------------------------'''
def changePermissions(instance,database,dbms_admin,dbms_admin_pwd):
    try:
        dbeditor = database + '_EDITOR'
        dbviewer = database + '_VIEWER'
        sql = gc_sql_utils.changePermissions.format(database=database,dbEditor=dbeditor,dbViewer=dbviewer)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
        sql = gc_sql_utils.grantRolePermissions.format(database=database)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
    except Exception as e:
        arcpy.AddError(e)
'''-------------------------------------------------------------------------------
# Change Default Schema of EDITOR and VIEWER
-------------------------------------------------------------------------------'''
def changeDefaultSchema(instance,database,dbms_admin,dbms_admin_pwd):
    try:
        dbeditor = database.upper() + '_EDITOR'
        dbviewer = database.upper() + '_VIEWER'
        dbowner = database.upper() + '_OWNER'
        sql = gc_sql_utils.changeDefaultSchema.format(database=database,dbEditor=dbeditor,dbViewer=dbviewer,dbOwner=dbowner)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
    except Exception as e:
        arcpy.AddError(e)
'''-------------------------------------------------------------------------------
# Change Spatial Data Type
-------------------------------------------------------------------------------'''
def changeSpatialType(instance,database,dbms_admin,dbms_admin_pwd):
    try:
        sql = gc_sql_utils.changeSpatialType.format(database=database)
        executeSQL(sql,instance,dbms_admin,dbms_admin_pwd)
        arcpy.AddMessage("++++++++++++++++++")
    except Exception as e:
        arcpy.AddError(e)
        arcpy.AddMessage("++++++++++++++++++")
'''-------------------------------------------------------------------------------
# Create SDE
-------------------------------------------------------------------------------'''
def createSDE(database_type,instance,database,account_authentication,dbms_admin,dbms_admin_pwd,schema_type,gdb_admin,gdb_admin_pwd,tablespace,license):
    # Get the current product license
    product_license=arcpy.ProductInfo()
    # Checks required license level
    if product_license.upper() == "ARCVIEW" or product_license.upper() == 'ENGINE':
        print("\n" + product_license + " license found!" + " Creating an enterprise geodatabase requires an ArcGIS for Desktop Standard or Advanced, ArcGIS Engine with the Geodatabase Update extension, or ArcGIS for Server license.")
        sys.exit("Re-authorize ArcGIS before creating enterprise geodatabase.")
    else:
        print("\n" + product_license + " license available!  Continuing to create...")
        arcpy.AddMessage("++++++++++++++++++")

    try:
        arcpy.AddMessage("Creating enterprise geodatabase...")
        arcpy.CreateEnterpriseGeodatabase_management(database_platform=database_type,instance_name=instance,database_name=database,account_authentication=account_authentication,database_admin=dbms_admin,database_admin_password=dbms_admin_pwd,sde_schema=schema_type, gdb_admin_name=gdb_admin,gdb_admin_password=gdb_admin_pwd,tablespace_name=tablespace,authorization_file=license)
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
'''-------------------------------------------------------------------------------
# Create User Connection Files
-------------------------------------------------------------------------------'''
def createUserConnectionFiles(instance,database_type,database,account_authentication,role,dbuser_pwd,out_folder_path):
    # Local variables
    if role == 'sde':
        dbuser_name = 'SDE'
    else:
        dbuser_name = database.upper() + '_' + role.upper()

    #if dbuser_pwd != '#':
    #    dbuser_pwd = database.lower() + '_' + role.upper() + '_' + str(datetime.datetime.now().year)
    #    arcpy.AddMessage(dbuser_pwd)

    instance_temp = instance.replace("\\","_")
    instance_temp = instance_temp.replace("/","_")
    instance_temp = instance_temp.replace(":","_")
    Conn_File_NameT = instance_temp + "." + database + "." + dbuser_name
    Connection_File_Name = Conn_File_NameT + ".sde"
    Connection_File_Name_full_path = out_folder_path + os.sep + Conn_File_NameT + ".sde"

    # Check for the .sde file and delete it if present
    arcpy.env.overwriteOutput=True
    if os.path.exists(Connection_File_Name_full_path):
        os.remove(Connection_File_Name_full_path)

    try:
        arcpy.AddMessage("Creating Database Connection File...")
        # Process: Create Database Connection File...
        # Usage:  out_file_location, out_file_name, DBMS_TYPE, instnace, account_authentication, username, password, database, save_username_password(must be true)
        arcpy.CreateDatabaseConnection_management(out_folder_path=out_folder_path, out_name=Connection_File_Name, database_platform=database_type, instance=instance, database=database, account_authentication=account_authentication, username=dbuser_name, password=dbuser_pwd, save_user_pass="TRUE")
        for i in range(arcpy.GetMessageCount()):
            if "000565" in arcpy.GetMessage(i):   #Check if database connection was successful
                arcpy.AddReturnMessage(i)
                arcpy.AddMessage("++++++++++++++++++")
                arcpy.AddMessage("Exiting!!")
                arcpy.AddMessage("++++++++++++++++++")
                sys.exit(3)
            else:
                arcpy.AddReturnMessage(i)
        arcpy.AddMessage("++++++++++++++++++")
    except:
        for i in range(arcpy.GetMessageCount()):
            arcpy.AddReturnMessage(i)
    return Connection_File_Name_full_path
'''-------------------------------------------------------------------------------
# MAIN
-------------------------------------------------------------------------------'''
def main(instance,database,dbms_admin_pwd,gdb_admin_pwd,dbsize,dbgrowth,dblogsize,dbloggrowth,recoverymodel,dbowner_pwd,dbeditor_pwd,dbviewer_pwd,license,out_folder_path,spatial_type):

    # Set local variables
    connection = ''
    database_type = 'SQL_SERVER'
    dbms_admin = 'sa'
    schema_type = 'SDE_SCHEMA'
    gdb_admin = 'sde'
    tablespace = ''

    # End local variables

    # Check SQL Server version
    sql = gc_sql_utils.getServerProperty.format(property='ProductVersion')
    mssqlversion = select(sql,instance,dbms_admin,dbms_admin_pwd)[0].split('.')[0]
    if int(mssqlversion) < 11:
        message('SQL Server 2008 or less are no longer supported!',2)
        sys.exit(1)
##    else:
##        message('you are using: {}'.format(mssqlversion))
##        sys.exit(0)

    createDB(instance,database,dbms_admin,dbms_admin_pwd,dbsize,dbgrowth,dblogsize,dbloggrowth,recoverymodel)

    if dbms_admin_pwd != '':
        account_authentication = 'DATABASE_AUTH'
    else:
        account_authentication = 'OPERATING_SYSTEM_AUTH'
    connection = createDBConnectionFile(instance,database_type,database,account_authentication,dbms_admin,dbms_admin_pwd)

    # Fix for 10.4 (see readme)
    # Instead of using the Esri arcpy-function using T-SQL

    # arcpy-functions
    '''
    createDBRole(connection,'R_SDE_OWNER')
    createDBRole(connection,'R_SDE_EDITOR')
    createDBRole(connection,'R_SDE_VIEWER')
    '''
    # using T-SQL statements instead
    createDBRoleSQL(instance,database,dbms_admin,dbms_admin_pwd,'R_SDE_OWNER')
    createDBRoleSQL(instance,database,dbms_admin,dbms_admin_pwd,'R_SDE_EDITOR')
    createDBRoleSQL(instance,database,dbms_admin,dbms_admin_pwd,'R_SDE_VIEWER')
    # End of fix

    createDBUser(database,connection,dbowner_pwd,'owner')
    createDBUser(database,connection,dbeditor_pwd,'editor')
    createDBUser(database,connection,dbviewer_pwd,'viewer')

    changePermissions(instance,database,dbms_admin,dbms_admin_pwd)

    changeDefaultSchema(instance,database,dbms_admin,dbms_admin_pwd)

    #createSDELogin(instance,dbms_admin,dbms_admin_pwd,gdb_admin_pwd)

    createSDE(database_type,instance,database,account_authentication,dbms_admin,dbms_admin_pwd,schema_type,gdb_admin,gdb_admin_pwd,tablespace,license)

    if spatial_type == 'SDEBINARY':
        changeSpatialType(instance,database,dbms_admin,dbms_admin_pwd)

    account_authentication = 'DATABASE_AUTH'

    ownerconnfile = createUserConnectionFiles(instance,database_type,database,account_authentication,'owner',dbowner_pwd,out_folder_path)
    createUserConnectionFiles(instance,database_type,database,account_authentication,'editor',dbeditor_pwd,out_folder_path)
    createUserConnectionFiles(instance,database_type,database,account_authentication,'viewer',dbviewer_pwd,out_folder_path)
    createUserConnectionFiles(instance,database_type,database,account_authentication,'sde',gdb_admin_pwd,out_folder_path)

    return str(ownerconnfile)
'''-------------------------------------------------------------------------------
# START script
-------------------------------------------------------------------------------'''
# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE,
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':
    # Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    main(*argv)
