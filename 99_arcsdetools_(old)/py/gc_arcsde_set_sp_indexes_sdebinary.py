'''
Created on 24.04.2015

@author: zid
'''

import arcpy

import gc_arcsde_set_sp_indexes_sdebinary_conf_av
import gc_arcsde_set_sp_indexes_sdebinary_conf_fwa
import gc_arcsde_set_sp_indexes_sdebinary_conf_ele
import gc_arcsde_set_sp_indexes_sdebinary_conf_gas
import gc_arcsde_set_sp_indexes_sdebinary_conf_was

import gc_arcsde_set_sp_indexes_sdebinary_utils

currentParam =[]
qualif=""

spUtil = gc_arcsde_set_sp_indexes_sdebinary_utils.Spatial_Idx_Util("MyObject")



if __name__ == '__main__':
    ws = arcpy.GetParameterAsText(0)
    model = arcpy.GetParameterAsText(1)
    qualif = spUtil.GetQualifier(ws)

    if str(model).startswith("AV"):
        currentParam= gc_arcsde_set_sp_indexes_sdebinary_conf_av.def_array
    if str(model).startswith("ELE"):
        currentParam=gc_arcsde_set_sp_indexes_sdebinary_conf_ele.def_array
    if str(model).startswith("FWA"):
        currentParam=gc_arcsde_set_sp_indexes_sdebinary_conf_fwa.def_array
    if str(model).startswith("GAS"):
        currentParam=gc_arcsde_set_sp_indexes_sdebinary_conf_gas.def_array
    if str(model).startswith("WAS"):
        currentParam=gc_arcsde_set_sp_indexes_sdebinary_conf_was.def_array

    if len(currentParam)>0:
        spUtil.SetSpatialIndexDefArray(ws, currentParam, qualif)
    else:
        spUtil.SetDefaultSpatialIndex(ws)
    arcpy.AddMessage("Fertig")


