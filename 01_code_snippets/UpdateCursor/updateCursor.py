# -*- coding: utf-8 -*- 
""" 
Beschreibung 
""" 
import arcpy 

featureClass = r"c:\temp\sample.gdb\muster" 
whereCond = "" 
targetFieldName = "resultat" 
newValue = None

rows = arcpy.UpdateCursor(featureClass, whereCond) 
row = rows.next() 
while row: 
    curValue = row.getValue(targetFieldName) 
    #Formel für die Berechnung oder Zuweisung des neuen Werts 
    # 
    #newValue="TEST" 
    if curValue != newValue: 
        if newValue is None: 
            row.setNull(targetFieldName) 
        else: 
            row.setValue(targetFieldName, newValue) 
        rows.updateRow(row) 
    row = rows.next() 
del row, rows
