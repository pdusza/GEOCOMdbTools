def Message(messageText, severity=0): 
    """ 
    Minimales Messaging, mit Zeit und den Text als Ausgabe. 
    @param messageText: Meldung welche ausgebene werden soll 
    @param severity: 0: Message, 1: Warnung, 2: Error 
    """ 
    if severity == 0: 
        arcpy.AddMessage(" %s :   %s" % (str(datetime.datetime.now()), messageText)) 
    if severity == 1: 
        arcpy.AddWarning(" %s :   %s" % (str(datetime.datetime.now()), messageText)) 
    if severity == 2: 
        arcpy.AddError(" %s :   %s" % (str(datetime.datetime.now()), messageText)) 
 
try: 
    print 1/0 
except: 
    messageText = "Generel Error..." 
    Message(messageText, 2) 
    exc_type, exc_value, exc_traceback = sys.exc_info() 
 
    for msg in traceback.extract_tb(exc_traceback): 
        Message(msg, 2) 
finally: 
    messageText = "Script finished" 
    Message(messageText)