#-------------------------------------------------------------------------------
# Name:        gc_arcsde_create_copy
# Purpose:     creates
#
# Author:      tbu
#
# Created:     05.03.2016
# Modified:
# Copyright:   (c) GEOCOM Informatik AG 2016
# Licence:     no license
#-------------------------------------------------------------------------------

import gc_arcsde_createsde_roles_users_mssql
import gc_gdbcopy_gdb2gdb
import gc_arcsde_set_permissions
import gc_arcsde_register_as_versioned
import gc_arcsde_set_sp_indexes_geometry_mssql

def main(instance,database,dbms_admin_pwd,gdb_admin_pwd,dbsize,dbgrowth,dblogsize,dbloggrowth,recoverymodel,dbowner_pwd,dbeditor_pwd,dbviewer_pwd,license,out_folder_path,spatial_type,ingdb,xmin,ymin,xmax,ymax,l1,l2,l3,l4,cells):

    ownerconnfile = gc_arcsde_createsde_roles_users_mssql.main(instance,database,dbms_admin_pwd,gdb_admin_pwd,dbsize,dbgrowth,dblogsize,dbloggrowth,recoverymodel,dbowner_pwd,dbeditor_pwd,dbviewer_pwd,license,out_folder_path,spatial_type)

    gc_gdbcopy_gdb2gdb.main(ingdb,ownerconnfile)

    gc_arcsde_set_permissions.main(ownerconnfile,"R_SDE_VIEWER","R_SDE_EDITOR")

    gc_arcsde_register_as_versioned.main(ownerconnfile,"WITH TABLES","GN")

    if spatial_type == "GEOMETRY":
        gc_arcsde_set_sp_indexes_geometry_mssql.main(ownerconnfile,dbms_admin_pwd,fc,xmin,ymin,xmax,ymax,l1,l2,l3,l4,cells)


if __name__ == '__main__':
    # Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    main(*argv)
