Hallo 
# Geocom Data Management Tools
[![gcDMT](https://img.shields.io/badge/release-0.9-yellow.svg)](https://geocom.ch/ "geocom") [![gcDMT](https://img.shields.io/badge/modified_by-dupr-green.svg)](https://git01.eggits.net/users/dupr/ "dupr")

------
## Requirements

- Installation of ArcGIS Desktop (minimum version 10.2). 
- Installation of a database client software, if you plan working with RDBMS.

------
## Installation und running the scripts

1. Download the *Geocom_database_management_tools* ZIP file.
2. Extract the ZIP file to desired location.
3. Open ArcCatalog.
4. Navigate to *Catalog Tree*.
5. Create a new connection to the folder with the scripts.
6. Depending on your ArcGIS Dekstop version choose appropriate toolbox (only when you use ArcGIS 10.2.x you need to use dedicated toolbox).
7. Before runnig the scripts read *Known issues and bugs* and *Help*.

------
## Workflows

In the example below you will find a sample workflow how to set up a complete enterprise geodatabase.

First you need create a new enterprise geodatabase and copy the data into it. Next step is to set permissions for roles and users. After that, feature classes and tables need to registerred as versioned. Geocom recommends to set up new spatial index values in order to keep high data performance. 

1. Create enterprise geodatabase (MSSQL).
2. Copy geodatabase to geodatabase.
3. Set permissions.
4. Register data as versioned.
5. Set spatial index geometry (MSSQL) or Set Spatial index sdebinary.

**IMPORTANT**: Always follow the steps in exactly the same order.

> Some workflows are already predefined in the Toolbox (see Toolgroup *workflows*).
>
> You can also create your own workflows and add them as a Tool or use them as a standalone python script or batch-workflow.

------
## Help

Detailed description of each tool can be found in the "Tool Help" or in the "Despription Page" in ArcMap or ArcCatalog.

#### Tool Help

1. To open "Tool help" navigate in ArcCatalog or in ArcMap to "Catalog Tree" and open the desired tool.
2. After the tools window opens click the button "Show Help >>". 
3. A new side panel will open with a description for the whole tool and for each field.

#### Despription Page

1. To open "Despription Page" navigate in ArcCatalog to "Catalog Tree" and select the desired tool.
2. In the right ArcCatalog window click on the bookmark "Description".
3. In the "Despription Page" you will find the complete tool description presented in the standard ESRI template. 

**IMPORTANT**: Both options provide exactly the same information about the tools.

------
## Known issues and bugs

- The tools do not support Oracle database. An upgrade in the scripts will be done in the coming weeks.
- The tool "Set spatial index sdebinary" supports only standard Geocom databases. All the customer extensions will be ignored.
- The tool "Set spatial index sdebinary" supports only german database model.

------
## License

Copyright 2017 Geocom Informatik AG
