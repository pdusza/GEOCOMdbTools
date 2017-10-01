﻿#-*- coding: utf-8 -*-
'''
Allgemeine Indexierung der Spatial Indexe

@author: Daniel Zinniker

@note: 



'''



# Variabeln

def_array=[]



def_array.append(['/DIV/KONSTRUKTION_FLA' , 'Polygon' , [500]])
def_array.append(['/DIV/KONSTRUKTION_PKT' , 'Point' , [500]])
def_array.append(['/DIV/KONSTRUKTION_LIN' , 'Polyline' , [500]])
def_array.append(['/DIV/MESSPUNKT' , 'Point' , [500]])
def_array.append(['/DIV/DIMENSION' , 'Polyline' , [500]])


def_array.append(['/GAS/GAS_BAUMASSNAHMEN' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_BMN_FLA' , 'Polygon' , [500]])
def_array.append(['/GAS/GAS_BMN_LIN' , 'Polyline' , [250]])
def_array.append(['/GAS/GAS_BMN_PKT' , 'Point' , [250]])
def_array.append(['/GAS/GAS_KABEL_PKT' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_ARMATUR' , 'Point' , [250]])
def_array.append(['/GAS/GAS_KABEL' , 'Polyline' , [250]])
def_array.append(['/GAS/GAS_HYDRAULIK_KNOTEN_PKT' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_HYDRAULIK_STRANG_LIN' , 'Polyline' , [1000]])
def_array.append(['/GAS/GAS_KKS' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_LEITUNG' , 'Polyline' , [200]])
def_array.append(['/GAS/GAS_LEITUNGSPUNKT' , 'Point' , [250]])
def_array.append(['/GAS/GAS_ROHRLEITUNGSTEIL' , 'Point' , [250]])
def_array.append(['/GAS/GAS_LINIE' , 'Polyline' , [500]])
def_array.append(['/GAS/GAS_SBW_FLA' , 'Polygon' , [500]])
def_array.append(['/GAS/GAS_SBW_LIN' , 'Polyline' , [500]])
def_array.append(['/GAS/GAS_SBW_PKT' , 'Point' , [500]])
def_array.append(['/GAS/GAS_TOPO_LIN' , 'Polyline' , [250]])
def_array.append(['/GAS/GAS_SCHADEN' , 'Point' , [500]])
def_array.append(['/GAS/GAS_SIPHON' , 'Point' , [500]])
def_array.append(['/GAS/GAS_SPEZIALBAUWERK' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_UEBRIGE_PKT' , 'Point' , [250]])
def_array.append(['/GAS/GAS_HAUSANSCHLUSS' , 'Point' , [250]])
def_array.append(['/GAS/U_GAS_MUTPUNKT' , 'Point' , [1000]])
def_array.append(['/GAS/GAS_NET_Junctions' , 'Point' , [200]])
def_array.append(['/GAS/GAS_DETAILPUNKT' , 'Point' , [500]])
def_array.append(['/GAS/GAS_EINSTIEG' , 'Point' , [500]])

def_array.append(['/GAS_LABEL/GAST_BEMERKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_UEBERDECKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_MATTYPMESS_BMN' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NUMMER_SIPHON' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NUMMER_HYD_STRANG' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NAME_HYD_KNOTEN' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_SCHALT_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_TEXT_KABEL' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NUMMER_HAUSAN' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_NUMMER_ROHRT' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_TEXT' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_TEXT_KABEL_PKT' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/GAST_MATDURCH_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_BEMERK_RLTG' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_DETAIL_UP_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_DETAIL_UP_MATDURCH' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_DETAIL_UP_SBW_NAME' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_DETAIL_UP_SBW_NUMMER' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_DETAIL_UP_SIPHON' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_NUMMER_SBW' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_UEBERDECK_BAUMASSN' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_UEBERDECK_LTGPKT' , 'Polyline' , [500]])
def_array.append(['/GAS_LABEL/U_GAST_UEBERDECK_ROHRLTGTEIL' , 'Polyline' , [500]])

def_array.append(['/GAS_PW2/gas_pw2_armatur' , 'Point' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_leitung' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_rohrleitungsteil' , 'Point' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_siphon' , 'Point' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_hausanschluss' , 'Point' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_spezialbauwerk' , 'Point' , [500]])
def_array.append(['/GAS_PW2/gas_pw2_topo_lin' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/GAS_PW2_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PW2/GAS_PW2_KKS' , 'Point' , [500]])
def_array.append(['/GAS_PW2/GAS_PW2_KABEL' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/GAS_PW2_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PW2/GAST_PW2_DURCHM_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/GAST_PW2_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/GAST_PW2_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_PW2/GAST_PW2_NUMMER_SIPHON' , 'Polyline' , [500]])

def_array.append(['/GAS_PW3/gas_pw3_topo_lin' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAST_PW3_DURCHM_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAST_PW3_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAST_PW3_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAST_PW3_NUMMER_SIPHON' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_KABEL' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_KKS' , 'Point' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_HAUSANSCHLUSS' , 'Point' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_ROHRLEITUNGSTEIL' , 'Point' , [500]])
def_array.append(['/GAS_PW3/GAS_PW3_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PW3/U_GAST_PW3_NUMMER_SBW' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/gas_pw3_armatur' , 'Point' , [500]])
def_array.append(['/GAS_PW3/gas_pw3_siphon' , 'Point' , [1000]])
def_array.append(['/GAS_PW3/gas_pw3_spezialbauwerk' , 'Point' , [1000]])
def_array.append(['/GAS_PW3/gas_pw3_leitung' , 'Polyline' , [250]])
def_array.append(['/GAS_PW3/GAS_PW3_NET_Junctions' , 'Point' , [200]])
def_array.append(['/GAS_PW3/U_GAS_PW3_DETAILLINIE' , 'Polyline' , [500]])
def_array.append(['/GAS_PW3/U_GAS_PW3_ZUSATZSYMBOL' , 'Point' , [2000]])
def_array.append(['/GAS_PW3/U_GAST_PW3_UP_TEXT' , 'Polyline' , [500]])

def_array.append(['/GAS_PWD/GAS_PWD_ARMATUR' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_HAUSANSCHLUSS' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_SIPHON' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_KABEL' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_KABEL_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_KKS' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_ROHRLEITUNGSTEIL' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_SPEZIALBAUWERK' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_UEBRIGE_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_BEMERKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_MATDURCH_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NAME_SPEZIALBW' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_SCHALT_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_UEBERDECKUNG_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NUMMER_SIPHON' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NAME_ABBILD' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NAME_URSPRUNG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GNPWD_URSPRUNG' , 'Polygon' , [500]])
def_array.append(['/GAS_PWD/GNPWD_ABBILD' , 'Polygon' , [500]])
def_array.append(['/GAS_PWD/GNPWD_VERBINDUNG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_SBW_PKT' , 'Point' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_SBW_LTG' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAS_PWD_SBW_FLA' , 'Polygon' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NUMMER_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NUMMER_HAUSAN' , 'Polyline' , [500]])
def_array.append(['/GAS_PWD/GAST_PWD_NUMMER_ROHRT' , 'Polyline' , [500]])


