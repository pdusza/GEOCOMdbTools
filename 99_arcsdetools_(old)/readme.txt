----------------------------------------
  __ _  ___  ___   ___ ___  _ __ ___  
 / _` |/ _ \/ _ \ / __/ _ \| '_ ` _ \ 
| (_| |  __/ (_) | (_| (_) | | | | | |
 \__, |\___|\___/ \___\___/|_| |_| |_|
  __/ |                               
 |___/  
----------------------------------------
version: 1.0.2
modified: 10.10.2016 (tbu)
----------------------------------------
known issues, bugs:
- Teilweise erscheint eine Meldung "SQL Statement could not be prepared" --> Problem mit ODBC-Connection, noch nicht gelöst
- Versionierung: jeweils das erste FeatureDataset pro DB kann nicht als versioniert registriert werden (Register as versioned is not supported for a dataset in feature dataset containing....)
- gelöst: ArcGIS 10.4 noch nicht unterstützt: wegen eines Bugs (siehe: https://geonet.esri.com/thread/177066) können per arcpy keine Rollen im SQL Server angelegt werden. Workaround: Rollen händisch anlegen (Skripts ausführen, Rollen anlegen, Skript nochmals ausführen)
----------------------------------------

10.10.2016 (tbu, 1.0.2):
- Fix für Tool "GC ArcSDE create sde roles users MSSQL": Rollen werden nun per T-SQL angelegt.
----------------------------------------
23.09.2016 (tbu):
- Tool "GC ArcSDE set spatial indexes GEOMETRY MSSQL" angepasst: instance name is now beeing considered correctly (i.e.: 'server' or 'server\instance')
----------------------------------------
changes (tbu, 1.0.1):
- Tool hinzugefügt: SDE-Connectionfiles anlegen (Hinweis: am besten als Batch-Skript ausführen, evtl. von Excel her kopieren)
----------------------------------------