#-------------------------------------------------------------------------------
# Name:        
# Purpose:
#
# Author:      GEOCOM Informatik AG
#
# Created:     11.12.2015
# Modified:    01.05.2017
# Copyright:   (c) GEOCOM Informatik AG 2016
# Licence:     no license
#-------------------------------------------------------------------------------




# Variables

def_array=[]

def_array.append(['/DIV/DIMENSION' , 'Polygon' , [1000]])
def_array.append(['/DIV/KONSTRUKTION_FLA' , 'Polygon' , [1000]])
def_array.append(['/DIV/KONSTRUKTION_LIN' , 'Polyline' , [1000]])
def_array.append(['/DIV/KONSTRUKTION_PKT' , 'Point' , [500]])
def_array.append(['/DIV/MESSPUNKT' , 'Point' , [1000]])

def_array.append(['/HYDR/AWHT_EINZUGSGEBIET' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_FLAECHE_RW' , 'Polygon' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_FLAECHE_SW' , 'Polygon' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_NUMMER_RW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_NUMMER_SW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_PSI_RW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_PSI_SW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_SYMBOL_RW' , 'Point' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_SYMBOL_SW' , 'Point' , [500]]) 
def_array.append(['/HYDR/AWH_EINZUG_ZENTR2' , 'Point' , [500]]) 
def_array.append(['/HYDR/AWH_GEFAHRENQUELLE' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_UNFALL' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_BADESTELLE' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_GEWABSCHNITT_BIS' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_GEWABSCHNITT_VON' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_GEWAESSERSEKTOR' , 'Polyline' , [1000]]) 
def_array.append(['/HYDR/AWH_GEWAESSERVERBAUUNG' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_GRUNDWASSERLEITER' , 'Polygon' , [1000]]) 
def_array.append(['/HYDR/AWH_SEE' , 'Polygon' , [1000]]) 
def_array.append(['/HYDR/AWH_WASSERFASSUNG' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_MESSSTELLE' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWHT_EZGZ_SYMBOL_MW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_NUMMER_MW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_FLAECHE_MW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWHT_EZGZ_PSI_MW' , 'Polyline' , [500]]) 
def_array.append(['/HYDR/AWH_EINZUG_KANTE' , 'Polyline' , [250]]) 
def_array.append(['/HYDR/AWH_EINZUG_ZENTR' , 'Point' , [250]]) 
def_array.append(['/HYDR/AWH_EINZUGSGEBIET' , 'Polygon' , [500]]) 
def_array.append(['/HYDR/AWH_BODENKENNWERT' , 'Point' , [1000]]) 
def_array.append(['/HYDR/AWH_ANSCHLUSSPUNKT_FLA' , 'Polygon' , [1000]])
def_array.append(['/HYDR/AWHA_0f9fe7cdb9313b5f9d2a7d02' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_8f0d1568b0957fb9ca3482ff' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_3b6488b2e0d773a24d1f3153' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_4787c7664006ebf860de97ea' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_73f71baeaab6c3b568ae081a' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_abc6289fb32b1490a31c376b' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_d2ba1094b3295b00bc3fb809' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_88a303f57d568b359562e370' , 'Annotation' , [500]])
def_array.append(['/HYDR/AWHA_af326d30f81566e61a0fe01b' , 'Annotation' , [500]])
 

def_array.append(['/INSP/AWZ_ZUSTAND_HALTUNG' , 'Point' , [250]]) 
def_array.append(['/INSP/AWZ_ZUSTAND_HALTUNG_LIN' , 'Polyline' , [250]]) 
def_array.append(['/INSP/AWZT_ZUSTAND' , 'Polyline' , [250]]) 
def_array.append(['/INSP/AWZT_ZUSTAND_LIN' , 'Polyline' , [250]]) 
def_array.append(['/INSP/AWZA_261852db5fa16525eb899712' , 'Annotation' , [250]]) 

def_array.append(['/SEW/AWKT_VSA_ABWASSERBAUWERK' , 'Polyline' , [500]]) 
def_array.append(['/SEW/AWKT_VP_HALTUNG' , 'Polyline' , [500]]) 
def_array.append(['/SEW/AWKT_BEMERKUNG_HALTUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_DECKEL' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_NUMMER_DECKEL' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_NP_HALTUNG' , 'Polyline' , [500]]) 
def_array.append(['/SEW/AWKT_FLIESSPFEIL_HALTUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_VSA_HALTUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_SCHACHT' , 'Polyline' , [250]]) 
def_array.append(['/SEW/AWKT_BAUWERK' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_VSA_LK_HALTUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_BEZEICHNUNG_BAUWERK' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_BEZEICHNUNG_HALTUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_BEZEICHNUNG_SCHACHT' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_HALTUNG' , 'Polyline' , [250]]) 
def_array.append(['/SEW/AWKT_TEXT' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWK_ABWASSERBAUWERK' , 'Polygon' , [250]]) 
def_array.append(['/SEW/AWK_ABWASSERKNOTEN' , 'Point' , [250]]) 
def_array.append(['/SEW/AWK_BAUWERK_LIN' , 'Polyline' , [500]]) 
def_array.append(['/SEW/AWK_BAUWERK_PKT' , 'Point' , [500]]) 
def_array.append(['/SEW/AWK_DECKEL' , 'Point' , [250]]) 
def_array.append(['/SEW/AWK_HALTUNG' , 'Polyline' , [250]]) 
def_array.append(['/SEW/AWK_HALTUNGSPUNKT' , 'Point' , [500]]) 
def_array.append(['/SEW/AWK_KABELLEITUNG' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWK_KABELPUNKT' , 'Point' , [1000]]) 
def_array.append(['/SEW/AWK_KANAL' , 'Polygon' , [250]]) 
def_array.append(['/SEW/AWK_LINIE' , 'Polyline' , [1000]])
def_array.append(['/SEW/AWK_SCHUTZROHR' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWK_SCHUTZROHR_FLA' , 'Polygon' , [1000]]) 
def_array.append(['/SEW/AWK_TOPO_LIN' , 'Polyline' , [250]]) 
def_array.append(['/SEW/AWO_ORGANISATION' , 'Polygon' , [1000]]) 
def_array.append(['/SEW/AWO_ZONE' , 'Polygon' , [1000]]) 
def_array.append(['/SEW/AWK_VSA_STEUERUNGSZENTRALE' , 'Point' , [1000]]) 
def_array.append(['/SEW/AWK_LEITUNGSHILFSPUNKT' , 'Point' , [1000]]) 
def_array.append(['/SEW/AWK_VSA_HALTUNGSPUNKT' , 'Point' , [500]]) 
def_array.append(['/SEW/AWKT_ABWASSERKNOTEN' , 'Polyline' , [1000]]) 
def_array.append(['/SEW/AWKT_BEMERKUNG_KNOTEN' , 'Polyline' , [1000]])
def_array.append(['/SEW/AWKA_4ce4939988f26c75a9671664' , 'Annotation' , [250]]) 
def_array.append(['/SEW/AWKA_83bcbc6c939f1775c0951a15' , 'Annotation' , [1000]]) 
def_array.append(['/SEW/AWKA_5983967e0e76a4d11ab5de9e' , 'Annotation' , [500]]) 
def_array.append(['/SEW/AWKA_920a765a59c2c7bc65dfc434' , 'Annotation' , [1000]]) 
def_array.append(['/SEW/AWKA_48dd00f85d1eef868cddea1b' , 'Annotation' , [500]]) 
def_array.append(['/SEW/AWKA_878d7a72598fb2400a3773b7' , 'Annotation' , [500]]) 
def_array.append(['/SEW/AWKA_d47964e4c842b5de0e8e4a73' , 'Annotation' , [250]]) 
def_array.append(['/SEW/AWKA_29033d5e15091979500406c2' , 'Annotation' , [1000]])  

def_array.append(['/SEW_PW2/AWK_PW2_HALTUNG' , 'Polyline' , [500]]) 
def_array.append(['/SEW_PW2/AWK_PW2_ABWASSERBAUWERK' , 'Polygon' , [500]])
def_array.append(['/SEW_PW2/AWK_PW2_ABWASSERKNOTEN' , 'Point' , [500]]) 
def_array.append(['/SEW_PW2/AWKT_PW2_ABWASSERKNOTEN' , 'Polyline' , [500]]) 
def_array.append(['/SEW_PW2/AWKT_PW2_HALTUNG' , 'Polyline' , [500]])

def_array.append(['/SEW_PW3/AWK_PW3_HALTUNG' , 'Polyline' , [500]]) 
def_array.append(['/SEW_PW3/AWK_PW3_ABWASSERBAUWERK' , 'Polygon' , [500]]) 
def_array.append(['/SEW_PW3/AWK_PW3_ABWASSERKNOTEN' , 'Point' , [500]]) 
def_array.append(['/SEW_PW3/AWKT_PW3_ABWASSERKNOTEN' , 'Polyline' , [500]]) 
def_array.append(['/SEW_PW3/AWKT_PW3_HALTUNG' , 'Polyline' , [500]]) 