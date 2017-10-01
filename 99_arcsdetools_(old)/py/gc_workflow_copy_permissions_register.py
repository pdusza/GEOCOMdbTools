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

import gc_gdbcopy_gdb2gdb
import gc_arcsde_set_permissions
import gc_arcsde_register_as_versioned


def main(ingdb,outgdb):

    gc_gdbcopy_gdb2gdb.main(ingdb,outgdb)

    gc_arcsde_set_permissions.main(outgdb,"R_SDE_VIEWER","R_SDE_EDITOR")

    gc_arcsde_register_as_versioned.main(outgdb,"WITH TABLES","GN")


if __name__ == '__main__':
    # Arguments are optional
    argv = tuple(arcpy.GetParameterAsText(i)
        for i in range(arcpy.GetArgumentCount()))
    main(*argv)
