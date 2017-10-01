# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Copyright:    (c) GEOCOM Informatik AG
# Created:      2015-11-14 by tbu
# Modified:     2015-12-04 by tbu (changed input arguments to command line options)
# Description:  This script compresses an enterprise geodatabase. It will then rebuild indexes
#               and gather statistics on the data in the geodatabase and send an email report.
#
# Parameters:   see help:
#               compress.py --help
#
# Example:      compress.py -a "D:\scripts\sde\admin_connections" -o "D:\scripts\sde\owner_connections" -s "SDE_SCHEMA" -p "d:\scripts\compress\log\compress.log" -l "DEBUG" -m "mail.company.ch" -e "user@company.ch"
#
# Usage:        1. create a bat-file with the line above (adapt the parameters)
#               2. start the bat-file from a TaskScheduler
#
# Limitation:   Only for connections with database authentication!!!
# ---------------------------------------------------------------------------

import os, sys, arcpy, logging, logging.handlers, smtplib, argparse
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define usage and version
parser = argparse.ArgumentParser(description='This script compresses an enterprise geodatabase. It will then rebuild indexes and gather statistics on the data in the geodatabase and send an email report.', usage='%(prog)s [options]', version='%(prog)s 1.0' + arcpy.GetInstallInfo()['Version'])
#Define help and options
parser.add_argument('-s', dest='schema', choices=['SDE_SCHEMA', 'DBO_SCHEMA'], default='SDE_SCHEMA', help='Type SDE_SCHEMA if you have a SDE schema or type DBO_SCHEMA to for use with a DBO schema (i.e.: workgroup geodatabase). Default=SDE_SCHEMA')
parser.add_argument('-a', dest='adminConns', help='Provide a folder (full-path) with all the admin connection SDE-files. This means the connection files with the SDE-user.')
parser.add_argument('-o', dest='ownerConns', help='Provide a folder (full-path) with all the owner connection SDE-files. This means the connection files with the dataowner,ie. schemaowner.')
parser.add_argument('-p', dest='logpath', help='Provide a file name (full-path) - i.e. "d:\scripts\compress\log\compress.log"')
parser.add_argument('-l', dest='loglevel', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG', help='For more information see: https://docs.python.org/2/howto/logging.html')
parser.add_argument('-m', dest='mailServer', help='Mailserver to send emails. The mailserver must be configured to be able to send mails without authentification.')
parser.add_argument('-e', dest='email', help='Email of the administrator. He will get all the emails.')


def configureLogging(logpath,loglevel):
    # Set up a specific logger with the desired output loglevel
    logger = logging.getLogger()
    logger.setLevel(loglevel)
    # Set the output logfile name and location
    handler = logging.handlers.RotatingFileHandler(logpath, maxBytes=10485760, backupCount=5)
    logger.addHandler(handler)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)


def sendEmail(mailserver,tomail,subject,emailmessage):
    frommail = 'db.maintenance@script.com'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = frommail
    msg['To'] = tomail
    # Prepare actual message
    text = emailmessage
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    #Connect to the server
    server = smtplib.SMTP(mailserver)
    # Send the mail
    server.sendmail(frommail, tomail, msg.as_string())
    #Disconnect from the server.
    server.quit()


def compress(conn):
    try:
        # block all connections to the database during the compress
        logging.debug('Disable to accept new connections')
        arcpy.AcceptConnections(conn, False)
        # disconnect any connected users
        logging.debug('Disconnecting all users')
        arcpy.DisconnectUser(conn, 'ALL')
        # Run the compress tool.
        try:
            logging.debug("Running compress")
            arcpy.Compress_management(conn)
            #if the compress is successful add a message.
            compressMsg = 'Compress was successful.\n'
            logging.info(compressMsg)
        except:
            #If the compress failed, add a message.
            compressMsg = 'Compress failed:\n' + arcpy.GetMessages(2)
            logging.error(compressMsg)
        # Allow connections again.
        logging.debug('Allow users to connect to the database again')
        arcpy.AcceptConnections(conn, True)
        pass
    except arcpy.ExecuteError:
        generalCompressMsg = arcpy.GetMessages(2)
        logging.error(generalCompressMsg)
    except Exception as e:
        logging.error(e.args[0])
    return compressMsg


def rebuildIndexes(conn,target,dataList):
    #Update indexes for the system tables
    # Note: to use the "SYSTEM" option the user must be an geodatabase or database administrator.
    try:
        logging.debug('Start rebuilding indexes on the {0} tables'.format(target))
        arcpy.RebuildIndexes_management(conn, target, dataList, "ALL")
        rebuildMsg = 'Rebuilding of {0} table indexes successful.\n'.format(target)
        logging.info(rebuildMsg)
        pass
    except arcpy.ExecuteError:
        rebuildMsg = 'Rebuild indexes on {0} tables failed:\n'.format(target) + arcpy.GetMessages(2)
        logging.error(rebuildMsg)
    except Exception as e:
        logging.error(e.args[0])
    return rebuildMsg


def analyzeData(conn,target,dataList,base,delta,archive):
    try:
        logging.debug('Start updating statistics on the {0} tables.'.format(target))
        arcpy.AnalyzeDatasets_management(conn, target, dataList, base, delta, archive)
        analyzeMsg = 'Analyzing of {0} tables successful.\n'.format(target)
        logging.info(analyzeMsg)
        pass
    except arcpy.ExecuteError:
        analyzeMsg = 'Analyze {0} tables failed:\n'.format(target) + arcpy.GetMessages(2)
        logging.error(analyzeMsg)
    except Exception as e:
        logging.error(e.args[0])
    return analyzeMsg


def getDataList(conn,schema):
    # Set a few environment variables
    arcpy.env.workspace = conn
    arcpy.env.overwriteOutput = True

    if schema == "DBO_SCHEMA":
        userName = "DBO"
    else:
        # Get the user name for the workspace
        # this assumes you are using database authentication.
        # OS authentication connection files do not have a 'user' property.
        logging.debug('Using Describe function to get the connected user name property from the connection file')
        desc = arcpy.Describe(conn)
        connProps = desc.connectionProperties
        userName = connProps.user

    logging.debug("Connected as user {0}".format(userName))
    # Get a list of all the datasets the user has access to.
    # First, get all the stand alone tables and feature classes.
    logging.debug("Compiling a list of data owned by the {0} user".format(userName))
    dataList = arcpy.ListTables('*.' + userName + '.*') \
             + arcpy.ListFeatureClasses('*.' + userName + '.*')
    # Next, for feature datasets get all of the featureclasses
    # from the list and add them to the master list.
    for dataset in arcpy.ListDatasets('*.' + userName + '.*'):
        dataList += arcpy.ListFeatureClasses(feature_dataset=dataset)
    return dataList


def main(adminConns,ownerConns,schema,mailserver,tomail):
    try:
        # Set directory to the SDE admin connection files
        arcpy.env.workspace = adminConns
        workspaces = arcpy.ListWorkspaces("*", "SDE")
        for workspace in workspaces:
            try:
                logging.info('Processing: ' + workspace)
                compressMsg = compress(workspace)
                logging.info('----------------------------------------------------')
                rebuildMsg = rebuildIndexes(workspace,"SYSTEM","")
                logging.info('----------------------------------------------------')
                analyzeMsg = analyzeData(workspace,"SYSTEM","","","","")
            except:
                import traceback
                logging.critical('\n**SCRIPT FAILURE**\nMost recent GP messages below.\n'+arcpy.GetMessages()+'\nTraceback messages below.\n'+traceback.format_exc().splitlines()[-1])
        logging.info('----------------------------------------------------')
        # Set directory to the SDE owner connection files
        arcpy.env.workspace = ownerConns
        workspaces = arcpy.ListWorkspaces("*", "SDE")
        for workspace in workspaces:
            try:
                logging.info('Processing: ' + workspace)
                # Don't rebuild the indexes for SDEBINARY. Otherwise they are reset to the default.
                #rebuildIndexes(workspace,"NO_SYSTEM",getDataList(workspace,schema))
                #logging.info('----------------------------------------------------')
                analyzeMsg = analyzeData(workspace,"NO_SYSTEM",getDataList(workspace,schema),"ANALYZE_BASE","ANALYZE_DELTA","ANALYZE_ARCHIVE")
                logging.info('Script finished')
            except:
                import traceback
                logging.critical('\n**SCRIPT FAILURE**\nMost recent GP messages below.\n'+arcpy.GetMessages()+'\nTraceback messages below.\n'+traceback.format_exc().splitlines()[-1])
        logging.info('*****************************************************')
        #Set a flag to indicate that the script has finished executing its required tasks.
        scriptSuccess = True
    except:
        import traceback
        scriptSuccess = False
        failMsg = '\n**SCRIPT FAILURE**\n'
        failMsg += 'Most recent GP messages below.\n'
        failMsg += arcpy.GetMessages() +'\n'
        failMsg += '\nTraceback messages below.\n'
        failMsg += traceback.format_exc().splitlines()[-1]

    #Send a summary using the send email function and the messages that have been created.
    if scriptSuccess == True:
        subject = 'Geodatabase maintenance script summary.'
        msg = compressMsg + rebuildMsg + analyzeMsg
    else:
        subject = 'Geodatabase maintenance script failed.'
        msg = failMsg
    sendEmail(mailserver,tomail,subject,msg)

# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE,
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':

    try:
        options = parser.parse_args()

        #Check if no system arguments (options) entered
        if len(sys.argv) == 1:
            print "%s: error: %s\n" % (sys.argv[0], "No command options given")
            parser.print_help()
            sys.exit(3)

        #Usage paramters for main function
        adminConns = options.adminConns
        ownerConns = options.ownerConns
        schema = options.schema.upper()
        logpath = options.logpath
        loglevel = options.loglevel
        mailserver = options.mailServer
        tomail = options.email

        #Set up Logging
        configureLogging(logpath,loglevel)

        #Main function goes here
        main(adminConns,ownerConns,schema,mailserver,tomail)

    #Check if no value entered for option
    except SystemExit as e:
        if e.code == 2:
            parser.usage = ""
            print("\n")
            parser.print_help()
            parser.exit(2)
