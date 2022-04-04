# Irene: wants to check the quadratic behavior of operators

import os, sys 
from array import array
import ROOT
import json
ROOT.gROOT.SetBatch(True)

def getCanvas(name):
 H_ref = 600
 W_ref = 600
 W = W_ref
 H  = H_ref

 iPeriod = 0

 # references for T, B, L, R                                                                                                                                                                                                                  
 T = 0.08*H_ref
 B = 0.12*H_ref
 L = 0.15*W_ref
 R = 0.04*W_ref
 cname = name
 canvas = ROOT.TCanvas(cname,cname,50,50,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx()
 canvas.SetTicky()

 return canvas

def getLegend(x1=0.3,y1=0.6363636,x2=0.6,y2=0.8020979):
  legend = ROOT.TLegend(x1,y1,x2,y2)
  legend.SetTextSize(0.04)
  legend.SetLineColor(0)
  legend.SetShadowColor(0)
  legend.SetLineStyle(1)
  legend.SetLineWidth(1)
  legend.SetFillColor(0)
  legend.SetFillStyle(0)
  legend.SetMargin(0.35)
  legend.SetTextFont(42)
  return legend

filename = "aQGC_WPHADWMLEP_UL2018"
inputfile = ROOT.TFile.Open(filename+".root",'READ')
eventTree = inputfile.Events

operatorsfileshort = 'aQGC_WPHADWMLEP_UL2018/operators_short.json'

jsonoperatorsfile = open(operatorsfileshort)
# returns JSON object as a dictionary
operators = json.load(jsonoperatorsfile)
jsonoperatorsfile.close()


'''
operators["fs0"] = ['m30p00',   'm29p25',   'm28p50',   'm27p75',   'm27p00',   'm26p25',   'm25p50',   'm24p75',   'm24p00',   'm23p25',   'm22p50',   'm21p75',   'm21p00',   'm20p25',   'm19p50',   'm18p75',   'm18p00',   'm17p25',   'm16p50',   'm15p75',   'm15p00',   'm14p25',   'm13p50',   'm12p75',   'm12p00',   'm11p25',   'm10p50',   'm9p75',   'm9p00',   'm8p25',   'm7p50',   'm6p75',   'm6p00',   'm5p25',   'm4p50',   'm3p75',   'm3p00',   'm2p25',   'm1p50',   'm0p75',   '0p00',   '0p75',   '1p50',   '2p25',   '3p00',   '3p75',   '4p50',   '5p25',   '6p00',   '6p75',   '7p50',   '8p25',   '9p00',   '9p75',   '10p50',   '11p25',   '12p00',   '12p75',   '13p50',   '14p25',   '15p00',   '15p75',   '16p50',   '17p25',   '18p00',   '18p75',   '19p50',   '20p25',   '21p00',   '21p75',   '22p50',   '23p25',   '24p00',   '24p75',   '25p50',   '26p25',   '27p00',   '27p75',   '28p50',   '29p25',   '30p00']
operators["fs1"] = ['m30p00','m29p25','m28p50','m27p75','m27p00','m26p25','m25p50','m24p75','m24p00','m23p25','m22p50','m21p75','m21p00','m20p25','m19p50','m18p75','m18p00','m17p25','m16p50','m15p75','m15p00','m14p25','m13p50','m12p75','m12p00','m11p25','m10p50','m9p75','m9p00','m8p25','m7p50','m6p75','m6p00','m5p25','m4p50','m3p75','m3p00','m2p25','m1p50','m0p75','0p00','0p75','1p50','2p25','3p00','3p75','4p50','5p25','6p00','6p75','7p50','8p25','9p00','9p75','10p50','11p25','12p00','12p75','13p50','14p25','15p00','15p75','16p50','17p25','18p00','18p75','19p50','20p25','21p00','21p75','22p50','23p25','24p00','24p75','25p50','26p25','27p00','27p75','28p50','29p25','30p00']
operators["fs2"] = ['m30p00',  'm29p25',  'm28p50',  'm27p75',  'm27p00',  'm26p25',  'm25p50',  'm24p75',  'm24p00',  'm23p25',  'm22p50',  'm21p75',  'm21p00',  'm19p50',  'm18p75',  'm18p00',  'm17p25',  'm16p50',  'm15p75',  'm15p00',  'm14p25',  'm13p50',  'm12p75',  'm12p00',  'm11p25',  'm10p50',  'm9p75',  'm9p00',  'm8p25',  'm7p50',  'm6p75',  'm6p00',  'm5p25',  'm4p50',  'm3p75',  'm3p00',  'm2p25',  'm1p50',  'm0p75',  '0p00',  '0p75',  '1p50',  '2p25',  '3p00',  '3p75',  '4p50',  '5p25',  '6p00',  '6p75',  '7p50',  '8p25',  '9p00',  '9p75',  '10p50',  '11p25',  '12p00',  '12p75',  '13p50',  '14p25',  '15p00',  '15p75',  '16p50',  '17p25',  '18p00',  '18p75',  '19p50',  '20p25',  '21p00',  '21p75',  '22p50',  '23p25',  '24p00',  '24p75',  '25p50',  '26p25',  '27p00',  '27p75',  '28p50',  '29p25',  '30p00']

operators["fm0"] = ['m36p00','m35p10','m34p20','m33p30','m32p40','m31p50','m30p60','m29p70','m28p80','m27p90','m27p00','m26p10','m25p20','m24p30','m23p40','m22p50','m21p60','m20p70','m19p80','m18p90','m18p00','m17p10','m16p20','m15p30','m14p40','m13p50','m12p60','m11p70','m10p80','m9p90','m9p00','m8p10','m7p20','m6p30','m5p40','m4p50','m3p60','m2p70','m1p80','m0p90','0p00','0p90','1p80','2p70','3p60','4p50','5p40','6p30','7p20','8p10','9p00','9p90','10p80','11p70','12p60','13p50','14p40','15p30','16p20','17p10','18p00','18p90','19p80','20p70','21p60','22p50','23p40','24p30','25p20','26p10','27p00','27p90','28p80','29p70','30p60','31p50','32p40','33p30','34p20','35p10','36p00']
operators["fm1"] = ['m28p00','m27p30','m26p60','m25p90','m25p20','m24p50','m23p80','m23p10','m22p40','m21p70','m21p00','m20p30','m19p60','m18p90','m18p20','m17p50','m16p80','m16p10','m15p40','m14p70','m14p00','m13p30','m12p60','m11p90','m11p20','m10p50','m9p80','m9p10','m8p40','m7p70','m7p00','m6p30','m5p60','m4p90','m4p20','m3p50','m2p80','m2p10','m1p40','m0p70','0p00','0p70','1p40','2p10','2p80','3p50','4p20','4p90','5p60','6p30','7p00','7p70','8p40','9p10','9p80','10p50','11p20','11p90','12p60','13p30','14p00','14p70','15p40','16p10','16p80','17p50','18p20','18p90','19p60','20p30','21p00','21p70','22p40','23p10','23p80','24p50','25p20','25p90','26p60','27p30','28p00']
operators["fm2"] = ['m60p00','m58p50','m57p00','m55p50','m54p00','m52p50','m51p00','m49p50','m48p00','m46p50','m45p00','m43p50','m42p00','m40p50','m39p00','m37p50','m36p00','m34p50','m33p00','m31p50','m30p00','m28p50','m27p00','m25p50','m24p00','m22p50','m21p00','m19p50','m18p00','m16p50','m15p00','m13p50','m12p00','m10p50','m9p00','m7p50','m6p00','m4p50','m3p00','m1p50','0p00','1p50','3p00','4p50','6p00','7p50','9p00','10p50','12p00','13p50','15p00','16p50','18p00','19p50','21p00','22p50','24p00','25p50','27p00','28p50','30p00','31p50','33p00','34p50','36p00','37p50','39p00','40p50','42p00','43p50','45p00','46p50','48p00','49p50','51p00','52p50','54p00','55p50','57p00','58p50','60p00']
operators["fm3"] = ['m80p00',   'm78p00',   'm76p00',   'm74p00',   'm72p00',   'm70p00',   'm68p00',   'm66p00',   'm64p00',   'm62p00',   'm60p00',   'm58p00',   'm56p00',   'm54p00',   'm52p00',   'm50p00',   'm48p00',   'm46p00',   'm44p00',   'm42p00',   'm40p00',   'm38p00',   'm36p00',   'm34p00',   'm32p00',   'm30p00',   'm28p00',   'm26p00',   'm24p00',   'm22p00',   'm20p00',   'm18p00',   'm16p00',   'm14p00',   'm12p00',   'm10p00',   'm8p00',   'm6p00',   'm4p00',   'm2p00',   '0p00',   '2p00',   '4p00',   '6p00',   '8p00',   '10p00',   '12p00',   '14p00',   '16p00',   '18p00',   '20p00',   '22p00',   '24p00',   '26p00',   '28p00',   '30p00',   '32p00',   '34p00',   '36p00',   '38p00',   '40p00',   '42p00',   '44p00',   '46p00',   '48p00',   '50p00',   '52p00',   '54p00',   '56p00',   '58p00',   '60p00',   '62p00',   '64p00',   '66p00',   '68p00',   '70p00',   '72p00',   '74p00',   '76p00',   '78p00',   '80p00']
operators["fm4"] = ['m80p00',   'm78p00',   'm76p00',   'm74p00',   'm72p00',   'm70p00',   'm68p00',   'm66p00',   'm64p00',   'm62p00',   'm60p00',   'm58p00',   'm56p00',   'm54p00',   'm52p00',   'm50p00',   'm48p00',   'm46p00',   'm44p00',   'm42p00',   'm40p00',   'm38p00',   'm36p00',   'm34p00',   'm32p00',   'm30p00',   'm28p00',   'm26p00',   'm24p00',   'm22p00',   'm20p00',   'm18p00',   'm16p00',   'm14p00',   'm12p00',   'm10p00',   'm8p00',   'm6p00',   'm4p00',   'm2p00',   '0p00',   '2p00',   '4p00',   '6p00',   '8p00',   '10p00',   '12p00',   '14p00',   '16p00',   '18p00',   '20p00',   '22p00',   '24p00',   '26p00',   '28p00',   '30p00',   '32p00',   '34p00',   '36p00',   '38p00',   '40p00',   '42p00',   '44p00',   '46p00',   '48p00',   '50p00',   '52p00',   '54p00',   '56p00',   '58p00',   '60p00',   '62p00',   '64p00',   '66p00',   '68p00',   '70p00',   '72p00',   '74p00',   '76p00',   '78p00',   '80p00']
operators["fm5"] = ['m160p00',    'm156p00',   'm152p00',   'm148p00',   'm144p00',   'm140p00',   'm136p00',   'm132p00',   'm128p00',   'm124p00',   'm120p00',   'm116p00',   'm112p00',   'm108p00',   'm104p00',   'm100p00',   'm96p00',   'm92p00',   'm88p00',   'm84p00',   'm80p00',   'm76p00',   'm72p00',   'm68p00',   'm64p00',   'm60p00',   'm56p00',   'm52p00',   'm48p00',   'm44p00',   'm40p00',   'm36p00',   'm32p00',   'm28p00',   'm24p00',   'm20p00',   'm16p00',   'm12p00',   'm8p00',   'm4p00',   '0p00',   '4p00',   '8p00',   '12p00',   '16p00',   '20p00',   '24p00',   '28p00',   '32p00',   '36p00',   '40p00',   '44p00',   '48p00',   '52p00',   '56p00',   '60p00',   '64p00',   '68p00',   '72p00',   '76p00',   '80p00',   '84p00',   '88p00',   '92p00',   '96p00',   '100p00',   '104p00',   '108p00',   '112p00',   '116p00',   '120p00',   '124p00',   '128p00',   '132p00',   '136p00',   '140p00',   '144p00',   '148p00',   '152p00',   '156p00',   '160p00']
#fm6 not present
operators["fm7"] = ['m80p00','m78p00','m76p00','m74p00','m72p00','m70p00','m68p00','m66p00','m64p00','m62p00','m60p00','m58p00','m56p00','m54p00','m52p00','m50p00','m48p00','m46p00','m44p00','m42p00','m40p00','m38p00','m36p00','m34p00','m32p00','m30p00','m28p00','m26p00','m24p00','m22p00','m20p00','m18p00','m16p00','m14p00','m12p00','m10p00','m8p00','m6p00','m4p00','m2p00','0p00','2p00','4p00','6p00','8p00','10p00','12p00','14p00','16p00','18p00','20p00','22p00','24p00','26p00','28p00','30p00','32p00','34p00','36p00','38p00','40p00','42p00','44p00','46p00','48p00','50p00','52p00','54p00','56p00','58p00','60p00','62p00','64p00','66p00','68p00','70p00','72p00','74p00','76p00','78p00','80p00']

operators["ft0"] = ['m2p00',   'm1p95',   'm1p90',   'm1p85',   'm1p80',   'm1p75',   'm1p70',   'm1p65',   'm1p60',   'm1p55',   'm1p50',   'm1p45',   'm1p40',   'm1p35',   'm1p30',   'm1p25',   'm1p20',   'm1p15',   'm1p10',   'm1p05',   'm1p00',   'm0p95',   'm0p90',   'm0p85',   'm0p80',   'm0p75',   'm0p70',   'm0p65',   'm0p60',   'm0p55',   'm0p50',   'm0p45',   'm0p40',   'm0p35',   'm0p30',   'm0p25',   'm0p20',   'm0p15',   'm0p10',   'm0p05',   '0p00',   '0p05',   '0p10',   '0p15',   '0p20',   '0p25',   '0p30',   '0p35',   '0p40',   '0p45',   '0p50',   '0p55',   '0p60',   '0p65',   '0p70',   '0p75',   '0p80',   '0p85',   '0p90',   '0p95',   '1p00',   '1p05',   '1p10',   '1p15',   '1p20',   '1p25',   '1p30',   '1p35',   '1p40',   '1p45',   '1p50',   '1p55',   '1p60',   '1p65',   '1p70',   '1p75',   '1p80',   '1p85',   '1p90',   '1p95',   '2p00']
operators["ft1"] = ['m2p00',   'm1p95',   'm1p90',   'm1p85',   'm1p80',   'm1p75',   'm1p70',   'm1p65',   'm1p60',   'm1p55',   'm1p50',   'm1p45',   'm1p40',   'm1p35',   'm1p30',   'm1p25',   'm1p20',   'm1p15',   'm1p10',   'm1p05',   'm1p00',   'm0p95',   'm0p90',   'm0p85',   'm0p80',   'm0p75',   'm0p70',   'm0p65',   'm0p60',   'm0p55',   'm0p50',   'm0p45',   'm0p40',   'm0p35',   'm0p30',   'm0p25',   'm0p20',   'm0p15',   'm0p10',   'm0p05',   '0p00',   '0p05',   '0p10',   '0p15',   '0p20',   '0p25',   '0p30',   '0p35',   '0p40',   '0p45',   '0p50',   '0p55',   '0p60',   '0p65',   '0p70',   '0p75',   '0p80',   '0p85',   '0p90',   '0p95',   '1p00',   '1p05',   '1p10',   '1p15',   '1p20',   '1p25',   '1p30',   '1p35',   '1p40',   '1p45',   '1p50',   '1p55',   '1p60',   '1p65',   '1p70',   '1p75',   '1p80',   '1p85',   '1p90',   '1p95',   '2p00']
operators["ft2"] = ['m4p00',   'm3p90',   'm3p80',   'm3p70',   'm3p60',   'm3p50',   'm3p40',   'm3p30',   'm3p20',   'm3p10',   'm3p00',   'm2p90',   'm2p80',   'm2p70',   'm2p60',   'm2p50',   'm2p40',   'm2p30',   'm2p20',   'm2p10',   'm2p00',   'm1p90',   'm1p80',   'm1p70',   'm1p60',   'm1p50',   'm1p40',   'm1p30',   'm1p20',   'm1p10',   'm1p00',   'm0p90',   'm0p80',   'm0p70',   'm0p60',   'm0p50',   'm0p40',   'm0p30',   'm0p20',   'm0p10',   '0p00',   '0p10',   '0p20',   '0p30',   '0p40',   '0p50',   '0p60',   '0p70',   '0p80',   '0p90',   '1p00',   '1p10',   '1p20',   '1p30',   '1p40',   '1p50',   '1p60',   '1p70',   '1p80',   '1p90',   '2p00',   '2p10',   '2p20',   '2p30',   '2p40',   '2p50',   '2p60',   '2p70',   '2p80',   '2p90',   '3p00',   '3p10',   '3p20',   '3p30',   '3p40',   '3p50',   '3p60',   '3p70',   '3p80',   '3p90',   '4p00']
operators["ft3"] = ['m4p00','m3p90','m3p80','m3p70','m3p60','m3p50','m3p40','m3p30','m3p20','m3p10','m3p00','m2p90','m2p80','m2p70','m2p60','m2p50','m2p40','m2p30','m2p20','m2p10','m2p00','m1p90','m1p80','m1p70','m1p60','m1p50','m1p40','m1p30','m1p20','m1p10','m1p00','m0p90','m0p80','m0p70','m0p60','m0p50','m0p40','m0p30','m0p20','m0p10','0p00','0p10','0p20','0p30','0p40','0p50','0p60','0p70','0p80','0p90','1p00','1p10','1p20','1p30','1p40','1p50','1p60','1p70','1p80','1p90','2p00','2p10','2p20','2p30','2p40','2p50','2p60','2p70','2p80','2p90','3p00','3p10','3p20','3p30','3p40','3p50','3p60','3p70','3p80','3p90','4p00']
operators["ft4"] = ['m4p00','m3p90','m3p80','m3p70','m3p60','m3p50','m3p40','m3p30','m3p20','m3p10','m3p00','m2p90','m2p80','m2p70','m2p60','m2p50','m2p40','m2p30','m2p20','m2p10','m2p00','m1p90','m1p80','m1p70','m1p60','m1p50','m1p40','m1p30','m1p20','m1p10','m1p00','m0p90','m0p80','m0p70','m0p60','m0p50','m0p40','m0p30','m0p20','m0p10','0p00','0p10','0p20','0p30','0p40','0p50','0p60','0p70','0p80','0p90','1p00','1p10','1p20','1p30','1p40','1p50','1p60','1p70','1p80','1p90','2p00','2p10','2p20','2p30','2p40','2p50','2p60','2p70','2p80','2p90','3p00','3p10','3p20','3p30','3p40','3p50','3p60','3p70','3p80','3p90','4p00']
operators["ft5"] = ['m8p00','m7p80','m7p60','m7p40','m7p20','m7p00','m6p80','m6p60','m6p40','m6p20','m6p00','m5p80','m5p60','m5p40','m5p20','m5p00','m4p80','m4p60','m4p40','m4p20','m4p00','m3p80','m3p60','m3p40','m3p20','m3p00','m2p80','m2p60','m2p40','m2p20','m2p00','m1p80','m1p60','m1p40','m1p20','m1p00','m0p80','m0p60','m0p40','m0p20','0p00','0p20','0p40','0p60','0p80','1p00','1p20','1p40','1p60','1p80','2p00','2p20','2p40','2p60','2p80','3p00','3p20','3p40','3p60','3p80','4p00','4p20','4p40','4p60','4p80','5p00','5p20','5p40','5p60','5p80','6p00','6p20','6p40','6p60','6p80','7p00','7p20','7p40','7p60','7p80','8p00']
operators["ft6"] = ['m8p00','m7p80','m7p60','m7p40','m7p20','m7p00','m6p80','m6p60','m6p40','m6p20','m6p00','m5p80','m5p60','m5p40','m5p20','m5p00','m4p80','m4p60','m4p40','m4p20','m4p00','m3p80','m3p60','m3p40','m3p20','m3p00','m2p80','m2p60','m2p40','m2p20','m2p00','m1p80','m1p60','m1p40','m1p20','m1p00','m0p80','m0p60','m0p40','m0p20','0p00','0p20','0p40','0p60','0p80','1p00','1p20','1p40','1p60','1p80','2p00','2p20','2p40','2p60','2p80','3p00','3p20','3p40','3p60','3p80','4p00','4p20','4p40','4p60','4p80','5p00','5p20','5p40','5p60','5p80','6p00','6p20','6p40','6p60','6p80','7p00','7p20','7p40','7p60','7p80','8p00']
operators["ft7"] = ['m16p00','m15p60','m15p20','m14p80','m14p40','m14p00','m13p60','m13p20','m12p80','m12p40','m12p00','m11p60','m11p20','m10p80','m10p40','m10p00','m9p60','m9p20','m8p80','m8p40','m8p00','m7p60','m7p20','m6p80','m6p40','m6p00','m5p60','m5p20','m4p80','m4p40','m4p00','m3p60','m3p20','m2p80','m2p40','m2p00','m1p60','m1p20','m0p80','m0p40','0p00','0p40','0p80','1p20','1p60','2p00','2p40','2p80','3p20','3p60','4p00','4p40','4p80','5p20','5p60','6p00','6p40','6p80','7p20','7p60','8p00','8p40','8p80','9p20','9p60','10p00','10p40','10p80','11p20','11p60','12p00','12p40','12p80','13p20','13p60','14p00','14p40','14p80','15p20','15p60','16p00']
operators["ft8"] = ['m20p00','m19p50','m19p00','m18p50','m18p00','m17p50','m17p00','m16p50','m16p00','m15p50','m15p00','m14p50','m14p00','m13p50','m13p00','m12p50','m12p00','m11p50','m11p00','m10p50','m10p00','m9p50','m9p00','m8p50','m8p00','m7p50','m7p00','m6p50','m6p00','m5p50','m5p00','m4p50','m4p00','m3p50','m3p00','m2p50','m2p00','m1p50','m1p00','m0p50','0p00','0p50','1p00','1p50','2p00','2p50','3p00','3p50','4p00','4p50','5p00','5p50','6p00','6p50','7p00','7p50','8p00','8p50','9p00','9p50','10p00','10p50','11p00','11p50','12p00','12p50','13p00','13p50','14p00','14p50','15p00','15p50','16p00','16p50','17p00','17p50','18p00','18p50','19p00','19p50','20p00']
operators["ft9"] = ['m20p00','m19p50','m19p00','m18p50','m18p00','m17p50','m17p00','m16p50','m16p00','m15p50','m15p00','m14p50','m14p00','m13p50','m13p00','m12p50','m12p00','m11p50','m11p00','m10p50','m10p00','m9p50','m9p00','m8p50','m8p00','m7p50','m7p00','m6p50','m6p00','m5p50','m5p00','m4p50','m4p00','m3p50','m3p00','m2p50','m2p00','m1p50','m1p00','m0p50','0p00','0p50','1p00','1p50','2p00','2p50','3p00','3p50','4p00','4p50','5p00','5p50','6p00','6p50','7p00','7p50','8p00','8p50','9p00','9p50','10p00','10p50','11p00','11p50','12p00','12p50','13p00','13p50','14p00','14p50','15p00','15p50','16p00','16p50','17p00','17p50','18p00','18p50','19p00','19p50','20p00']
'''

colors = ["#4292c6","#41ab5d","#ef3b2c","#17202A","#fdae61","#abd9e9","#2c7bb6"]
linestyle = [1,2,3,4,5,6,7,8,9]
markerstyle = [4,25,31,21,8]
ROOT.gStyle.SetOptStat(0)

try:
  os.mkdir(filename)
except:
  print 
h = {}
for operator in operators:
  print( " operator ", operator)
  canvas = getCanvas(operator)
  h[operator] = {}
  legend = getLegend()
  for i,coupling in enumerate(operators[operator]):
    print("coupling ",coupling)
    #hist = ROOT.gROOT.FindObject('hist')
    #if hist: hist.Delete() 
    rescaledoperator = operator+"_"+coupling
    hist = ROOT.TH1F('hist','hist',36,0,1.2)
    eventTree.Draw(rescaledoperator+"/LHEWeight_originalXWGTUP>>hist","","goff")
    hist = ROOT.gROOT.FindObject("hist")
    h[operator][i] = hist
    print(hist.GetMean())
    h[operator][i].SetTitle(operator)
    h[operator][i].SetLineColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
    h[operator][i].SetLineWidth(2)
    h[operator][i].GetXaxis().SetTitle(operator+"/LHEWeight_originalXWGTUP")
    h[operator][i].SetLineStyle(linestyle[i])
    h[operator][i].GetYaxis().SetRangeUser(0.8,1000)
    h[operator][i].SetMarkerColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
    h[operator][i].SetMarkerStyle(markerstyle[i])
    legend.AddEntry(h[operator][i],coupling.replace("m","-").replace("p","."))
    if  i == 0: 
      print ("i ",i," color ",colors[i])
      print(h[operator][i].GetMean())
      h[operator][i].Draw("P")
    else: 
      print ("i ",i," color ",colors[i])
      print(h[operator][i].GetMean())
      h[operator][i].Draw("Psame")   
    print("drawn")
  legend.Draw("same") 
  canvas.SetLogy() 
  canvas.SaveAs(filename+"/"+operator+".png")
  canvas.SaveAs(filename+"/"+operator+".C")
  print("done with canvas ",operator)
  canvas.Delete()