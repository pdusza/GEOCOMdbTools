﻿#-*- coding: utf-8 -*-
'''
Indexierung der Spatial Indexe

@author: Daniel Zinniker

@note: 



'''



# Variabeln

def_array=[]


# DATASET AV
#TEXTE / LABELS

def_array.append(['/av/avt_bbgebaeudenummer' , 'Polyline' , [500]])
def_array.append(['/av/avt_bbobjektname' , 'Polyline' , [500]])
def_array.append(['/av/avt_einzelpunkt' , 'Polyline' , [500]])
def_array.append(['/av/avt_eobjektname' , 'Polyline' , [500]])
def_array.append(['/av/avt_eobjektnummer' , 'Polyline' , [500]])
def_array.append(['/av/avt_flurname' , 'Polyline' , [1000]])
def_array.append(['/av/avt_gebaeudeeingang' , 'Polyline' , [500]])
def_array.append(['/av/avt_gebaeudeeingangname' , 'Polyline' ,[500]])
def_array.append(['/av/avt_gelaendename' , 'Polyline' , [1000]])
def_array.append(['/av/avt_hfp' , 'Polyline' , [1000]])
def_array.append(['/av/avt_hhgrenzpunkt' , 'Polyline' , [1000]])
def_array.append(['/av/avt_hoehenpunkt' , 'Polyline' , [1000]])
def_array.append(['/av/avt_koordinatenanschrift' , 'Polyline' , [500]])
def_array.append(['/av/avt_leitungsobjekt' , 'Polyline' , [500]])
def_array.append(['/av/avt_lfp' , 'Polyline' , [1000]])
def_array.append(['/av/avt_liegenschaft' , 'Polyline' , [250]])
def_array.append(['/av/avt_liegenschaft_flaeche' , 'Polyline' , [250]])
def_array.append(['/av/avt_ligrenzpunkt' , 'Polyline' , [250]])
def_array.append(['/av/avt_mu_liegenschaft' , 'Polyline' , [500]])
def_array.append(['/av/avt_mu_liegenschaft_flaeche' , 'Polyline' , [500]])
def_array.append(['/av/avt_mu_liverschnitt' , 'Polyline' ,[500]])
def_array.append(['/av/avt_mu_sr_bw' , 'Polyline' , [500]])
def_array.append(['/av/avt_mu_sr_bw_flaeche' , 'Polyline' ,[500]])
def_array.append(['/av/avt_nummerierungsbereich' , 'Polyline' , [1000]])
def_array.append(['/av/avt_ortschaftsname' , 'Polyline' , [1000]])
def_array.append(['/av/avt_ortsname' , 'Polyline' , [1000]])
def_array.append(['/av/avt_plan' , 'Polyline' ,[500]])
def_array.append(['/av/avt_planbeschriftung' , 'Polyline' ,[1000]])
def_array.append(['/av/avt_projbbgebaeudenummer' , 'Polyline' , [500]])
def_array.append(['/av/avt_projbbobjektname' , 'Polyline' ,[250]])
def_array.append(['/av/avt_rutschung' , 'Polyline' , [1000]])
def_array.append(['/av/avt_signalpunkt' , 'Polyline' , [1000]])
def_array.append(['/av/avt_sr_bw' , 'Polyline' , [500]])
def_array.append(['/av/avt_sr_bw_flaeche' , 'Polyline' , [1000]])
def_array.append(['/av/avt_strassenbezname' , 'Polyline' , [1000]])
def_array.append(['/av/avt_toleranzstufe' , 'Polyline' , [1500]])


#POINT
def_array.append(['/av/av_bbflaechesymbol' , 'Point' , [500]])
def_array.append(['/av/av_bbzentroid' , 'Point' , [500]])
def_array.append(['/av/av_einzelpunkt' , 'Point' , [500]])
def_array.append(['/av/av_eoflaechenelementsymbol' , 'Point' , [500]])
def_array.append(['/av/av_eolinienelementsymbol' , 'Point' , [500]])
def_array.append(['/av/av_eopunktelement' , 'Point' , [1000]])
def_array.append(['/av/av_gebaeudeeingang' , 'Point' , [500]])
def_array.append(['/av/av_hfp' , 'Point' , [1000]])
def_array.append(['/av/av_hhgrenzpunkt' , 'Point' , [1000]])
def_array.append(['/av/av_hoehenpunkt' , 'Point' , [1000]])
def_array.append(['/av/av_lfp' , 'Point' , [1000]])
def_array.append(['/av/av_liegzentroid' , 'Point' , [500]])
def_array.append(['/av/av_ligrenzpunkt' , 'Point' , [500]])
def_array.append(['/av/av_mu_liegzentroid' , 'Point' , [500]])
def_array.append(['/av/av_netzkreuz' , 'Point' , [500]])
def_array.append(['/av/av_planlayout' , 'Point' , [1000]])
def_array.append(['/av/av_planlayoutsymbol' , 'Point' , [1000]])
def_array.append(['/av/av_projbbflaechesymbol' , 'Point' , [500]])
def_array.append(['/av/av_ropunktelement' , 'Point' , [250]])
def_array.append(['/av/av_signalpunkt' , 'Point' , [500]])
def_array.append(['/av/av_uebersicht' , 'Point' , [1000]])
def_array.append(['/av/konstruktion_pkt' , 'Point' , [250]])
def_array.append(['/av/av_flurname_zentroid' , 'Point' , [500]])
def_array.append(['/av/av_plan_zentroid' , 'Point' , [1000]])
def_array.append(['/av/av_toleranzstufe_zentroid' , 'Point' , [1000]])
def_array.append(['/av/av_gemeindegrenze_zentroid' , 'Point' , [5000]])
def_array.append(['/AV/U_AV_WEBADRESSE' , 'Point' , [500]])

#LINIEN
def_array.append(['/av/av_bbkante' , 'Polyline' , [500]])
def_array.append(['/av/av_eoflaechenelement_lin' , 'Polyline' , [250]])
def_array.append(['/av/av_eolinienelement' , 'Polyline' , [250]])
def_array.append(['/av/av_flurname_kante' , 'Polyline' , [500]])
def_array.append(['/av/av_gebaeudeeingangname_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_gelaendekante' , 'Polyline' , [500]])
def_array.append(['/av/av_gemeindegrenze_kante' , 'Polyline' , [1000]])
def_array.append(['/av/av_grenzabschnitt' , 'Polyline' , [2000]])
def_array.append(['/av/av_koordinatenlinie' , 'Polyline' , [500]])
def_array.append(['/av/av_liegenschaft_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_liegkante' , 'Polyline' , [250,2000]])
def_array.append(['/av/av_mu_kanten' , 'Polyline' , [250]])
def_array.append(['/av/av_mu_liegenschaft_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_mu_sr_bw_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_ortsname_kante' , 'Polyline' , [2000]])
def_array.append(['/av/av_plan_kante' , 'Polyline' , [2000]])
def_array.append(['/av/av_prlinienobjekt' , 'Polyline' , [1000]])
def_array.append(['/av/av_projgemeindegrenze' , 'Polyline' , [1000]])
def_array.append(['/av/av_rolinienelement' , 'Polyline' , [1000]])
def_array.append(['/av/av_sr_bw_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_sr_bw_lin' , 'Polyline' , [500]])
def_array.append(['/av/av_strassenbezname_hlin' , 'Polyline' , [500]])
def_array.append(['/av/av_strassenstueck' , 'Polyline' , [500]])
def_array.append(['/av/av_toleranzstufe_kante' , 'Polyline' , [1000]])
def_array.append(['/av/DIMENSION' , 'Polyline' , [250]])
def_array.append(['/av/konstruktion_lin' , 'Polyline' , [500]])



#POLYGON
def_array.append(['/av/av_aussparung' , 'Polygon' , [1000]])
def_array.append(['/av/av_bbflaeche' , 'Polygon' , [500]])
def_array.append(['/av/av_benanntesgebiet' , 'Polygon' , [2000]])
def_array.append(['/av/av_darstellungsflaeche' , 'Polygon' , [2000]])
def_array.append(['/av/AV_DIMENSION_200' , 'Polygon' , [500]])
def_array.append(['/av/AV_DIMENSION_500' , 'Polygon' , [500]])
def_array.append(['/av/av_eoflaechenelement' , 'Polygon' , [250]])
def_array.append(['/av/av_flurname' , 'Polygon' , [1000]])
def_array.append(['/av/av_gemeindegrenze' , 'Polygon' , [5000]])
def_array.append(['/av/av_liegenschaft' , 'Polygon' , [500]])
def_array.append(['/av/av_liegenschaft_archiv' , 'Polygon' , [500]])
def_array.append(['/av/av_mu_liegenschaft' , 'Polygon' , [500]])
def_array.append(['/av/av_mu_liverschnitt' , 'Polygon' , [500]])
def_array.append(['/av/av_mu_sr_bw' , 'Polygon' , [500]])
def_array.append(['/av/av_nachfuehrung' , 'Polygon' , [5000]])
def_array.append(['/av/av_nummerierungsbereich' , 'Polygon' , [5000]])
def_array.append(['/av/av_ort' , 'Polygon' , [10000]])
def_array.append(['/av/av_ortsname' , 'Polygon' , [5000]])
def_array.append(['/av/av_plan' , 'Polygon' , [2000]])
def_array.append(['/av/av_planclip' , 'Polygon' , [2000]])
def_array.append(['/av/av_plz6' , 'Polygon' , [2000]])
def_array.append(['/av/av_projbbflaeche' , 'Polygon' , [500]])
def_array.append(['/av/av_roflaechenelement' , 'Polygon' , [500]])
def_array.append(['/av/av_rutschung' , 'Polygon' , [2000]])
def_array.append(['/av/av_sr_bw' , 'Polygon' , [500]])
def_array.append(['/av/av_toleranzstufe' , 'Polygon' , [2000]])
def_array.append(['/av/konstruktion_fla' , 'Polygon' , [1000]])



                    
