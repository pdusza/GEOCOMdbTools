#-*- coding: utf-8 -*-
'''
Allgemeine Indexierung der Spatial Indexe

@author: Daniel Zinniker

@note: 



'''



# Variabeln

def_array=[]

def_array.append(['/FWA/FWA_STGLTG_ARMATUR' , 'Point' , [250]])
def_array.append(['/FWA/FWA_STGLTG_LEITUNG' , 'Polyline' , [200]])
def_array.append(['/FWA/FWA_DEHNZONE' , 'Polygon' , [200]])
def_array.append(['/FWA/FWA_MESSPUNKT' , 'Point' , [1000]])
def_array.append(['/FWA/FWA_MESSLEITUNG' , 'Polyline' , [200]])
def_array.append(['/FWA/FWA_KABELPUNKT' , 'Point' , [200]])
def_array.append(['/FWA/FWA_KABEL' , 'Polyline' , [250]])
def_array.append(['/FWA/FWA_BAUWERK_LIN' , 'Polyline' , [500]])
def_array.append(['/FWA/FWA_BAUWERK_FLA' , 'Polygon' , [500]])
def_array.append(['/FWA/FWA_BAUWERK' , 'Point' , [500]])
def_array.append(['/FWA/FWAT_ART_SCHUTZMASSNAHME' , 'Polyline' , [1000]])
def_array.append(['/FWA/FWA_SCHUTZMASSNAHME' , 'Polygon' , [1000]])
def_array.append(['/FWA/FWAT_UEBERD_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_BEM_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_LK_DURCH_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_MAT_DURCH_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_VERL_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWA_LEITUNG' , 'Polyline' , [200]])
def_array.append(['/FWA/FWAT_NR_UEBERGABEPUNKT' , 'Polyline' , [1000]])
def_array.append(['/FWA/FWA_UEBERGABEPUNKT' , 'Point' , [1000]])
def_array.append(['/FWA/FWA_LEITUNGSPUNKT' , 'Point' , [1000]])
def_array.append(['/FWA/FWA_EINBAUTE' , 'Point' , [1000]])
def_array.append(['/FWA/FWAT_ABD_ABGANG' , 'Polyline' , [1000]])
def_array.append(['/FWA/FWA_ABGANG' , 'Point' , [1000]])
def_array.append(['/FWA/FWA_FORMSTUECK' , 'Point' , [250]])
def_array.append(['/FWA/FWAT_STELLUNG_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/FWA/FWA_ARMATUR' , 'Point' , [250]])
def_array.append(['/FWA/FWA_STATIKPUNKT' , 'Point' , [500]])
def_array.append(['/FWA/FWA_TRASSEPUNKT' , 'Point' , [500]])
def_array.append(['/FWA/FWA_TRASSE' , 'Polyline' , [250]])
def_array.append(['/FWA/FWA_TOPO_LIN' , 'Polyline' , [250]])
def_array.append(['/FWA/FWAT_GESBESCHR_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_BEM_BAUWERK' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_TYP_ABGANG' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_HOEHE_ABGANG' , 'Polyline' , [0]])
def_array.append(['/FWA/FWAT_HOEHE_ARMATUR' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_HOEHE_UEBERGABEPUNKT' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_HOEHE_FORMSTUECK' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_HOEHE_STATIKPUNKT' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_HOEHE_LEITUNGSPUNKT' , 'Polyline' , [500]])
def_array.append(['/FWA/FWA_SCHADEN' , 'Point' , [500]])
def_array.append(['/FWA/FWA_NET_Junctions' , 'Point' , [200]])
def_array.append(['/FWA/U_FWAT_UEBERDECK_LTGPKT' , 'Polyline' , [500]])
def_array.append(['/FWA/U_FWAT_UEBERDECK_RLTG' , 'Polyline' , [500]])
def_array.append(['/FWA/U_FWAT_NUMMER_ARMATUR' , 'Polyline' , [250]])
def_array.append(['/FWA/U_FWA_SCHUTZMASSNAHME_LIN' , 'Polyline' , [500]])
def_array.append(['/FWA/FWA_LINIE' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_NAME_BAUWERK' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_TEXT' , 'Polyline' , [500]])
def_array.append(['/FWA/FWAT_TXT_TRASSE' , 'Polyline' , [500]])
def_array.append(['/FWA/U_FWA_MUTPUNKT' , 'Point' , [250]])
def_array.append(['/FWA/U_FWA_ROHRLEITUNGSTEIL' , 'Point' , [250]])
def_array.append(['/FWA/U_FWAT_MAT_DURCH_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA/U_FWAT_UP_NAME_BAUWERK' , 'Polyline' , [500]])

def_array.append(['/FWA_PW2/FWA_PW2_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA_PW2/FWA_PW2_BAUWERK' , 'Point' , [500]])
def_array.append(['/FWA_PW2/FWAT_PW2_NENNWEITE_LEITUNG' , 'Polyline' , [500]])
def_array.append(['/FWA_PW2/FWAT_PW2_BAUWERK' , 'Polyline' , [500]])

def_array.append(['/FWA_PW3/FWA_PW3_TRASSE' , 'Polyline' , [500]])

def_array.append(['/FWA_PROFIL/METRIERUNG' , 'Polyline' , [500]])
def_array.append(['/FWA_PROFIL/PRF_PROFILBASIS' , 'Polyline' , [500]])
def_array.append(['/FWA_PROFIL/PRF_PROFILLINIE' , 'Polyline' , [500]])
def_array.append(['/FWA_PROFIL/PRF_PROFILTEXT' , 'Polyline' , [500]])
def_array.append(['/FWA_PROFIL/PRF_PROFILPUNKT' , 'Point' , [500]])
def_array.append(['/FWA_PROFIL/PRF_PROFILFLAECHE' , 'Polygon' , [500]])


def_array.append(['/DIV/KONSTRUKTION_FLA' , 'Polygon' , [500]])
def_array.append(['/DIV/KONSTRUKTION_PKT' , 'Point' , [500]])
def_array.append(['/DIV/KONSTRUKTION_LIN' , 'Polyline' , [500]])
def_array.append(['/DIV/VERMESSUNGSPUNKT' , 'Point' , [500]])



