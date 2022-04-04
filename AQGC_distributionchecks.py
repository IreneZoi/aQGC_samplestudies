# Irene's code inspired by Jay's code:  takes a text list of input files, an output root file, and an input cross section (see run.sh)
# makes histograms of a given variable (currently maximum m_{jj} per event for different working points of various operators and saves to the output           file
# currently setup for about the limits from SMP-18-006 (taken from figures 6,7,8 here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSMPaTGC           )
import ROOT, json
import sys,os
from coffea.nanoevents import NanoEventsFactory, NanoAODSchema
#import coffea.hist as hist
from matplotlib import pyplot as plt
import awkward as ak
import numpy as np

def getVBShists(fname,xsec_times_BR,var,operator,opweight):
  print(" VBF hists ")
  hists = {}
  hists[var]= ROOT.TH1F(var+"_"+operator+"_"+opweight,var+"_"+operator+"_"+opweight,variables[var]['nbins'],variables[var]['xmin'],variables[var]['xmax'])
  hists[var].GetXaxis().SetTitle(variables[var]['xaxistitle'])
  for vbfvar in additionalvbfvariables:
      hists[vbfvar] = ROOT.TH1F(vbfvar+"_"+operator+"_"+opweight,vbfvar+"_"+operator+"_"+opweight,additionalvbfvariables[vbfvar]['nbins'],additionalvbfvariables[vbfvar]['xmin'],additionalvbfvariables[vbfvar]['xmax'])
      hists[vbfvar].GetXaxis().SetTitle(additionalvbfvariables[vbfvar]['xaxistitle'])
  
  events = NanoEventsFactory.from_root(fname, schemaclass=NanoAODSchema).events()
  for i in range(0,len(events)):
    mjj = 0
    #print( "event ",i)
    for j in range(0,ak.num(events.GenJet)[i]):
      for  k in range( j + 1, ak.num(events.GenJet)[i]):
        tmp1 = ROOT.TLorentzVector(0, 0, 0, 0)
        tmp1.SetPtEtaPhiM(events.GenJet.pt[i,j],events.GenJet.eta[i,j],events.GenJet.phi[i,j],events.GenJet.mass[i,j])

        tmp2 = ROOT.TLorentzVector(0, 0, 0, 0)
        tmp2.SetPtEtaPhiM(events.GenJet.pt[i,k],events.GenJet.eta[i,k],events.GenJet.phi[i,k],events.GenJet.mass[i,k])
        tempVBF = tmp1 + tmp2
        #considering as vbs jets the two with the higher mjj 
        if (tempVBF.M() < mjj):
          continue
        mjj = tempVBF.M()
        deltaeta = events.GenJet.eta[i,j]-events.GenJet.eta[i,k]
    #print(" mjj ", mjj)
    hists[var].Fill(mjj,xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    hists["deltaetaVBF"].Fill(deltaeta,xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    hists["eta1VBF"].Fill(events.GenJet.eta[i,j],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    hists["eta2VBF"].Fill(events.GenJet.eta[i,k],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    hists["pt1VBF"].Fill(events.GenJet.pt[i,j],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    hists["pt2VBF"].Fill(events.GenJet.pt[i,k],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])

  
  return hists[var],hists["deltaetaVBF"],hists["eta1VBF"],hists["eta2VBF"],hists["pt1VBF"],hists["pt2VBF"]

def getHists(fname,xsec_times_BR,var,operator,opweight):
  hists = {}
  hists[var]= ROOT.TH1F(var+"_"+operator+"_"+opweight,var+"_"+operator+"_"+opweight,variables[var]['nbins'],variables[var]['xmin'],variables[var]['xmax'])
  hists[var].GetXaxis().SetTitle(variables[var]['xaxistitle'])
  events = NanoEventsFactory.from_root(fname, schemaclass=NanoAODSchema).events()
  for i in range(0,len(events)):
    if var == 'etaJ' and ak.num(events.GenJetAK8)[i]>0:
      #print("ak.num(events.GenJetAK8) ",ak.num(events.GenJetAK8)[i])        
      hists[var].Fill(events.GenJetAK8.eta[i,0],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'ptJ' and ak.num(events.GenJetAK8)[i]>0:            
      hists[var].Fill(events.GenJetAK8.pt[i,0],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'massJ' and ak.num(events.GenJetAK8)[i]>0:            
      hists[var].Fill(events.GenJetAK8.mass[i,0],xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'ptEl'  and  ak.num(events.Electron.matched_gen)[i]>0:
      #print("ak.num(events.Electron.matched_gen) ",ak.num(events.Electron.matched_gen)[i])
      #print("ak.num(events.Electron.matched_gen) pt", events.Electron[i,0].matched_gen.pt)
      hists[var].Fill(events.Electron[i,0].matched_gen.pt*xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'ptMu' and  ak.num(events.Muon.matched_gen)[i]>0:
      hists[var].Fill(events.Muon[i,0].matched_gen.pt*xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'm_VVgenpart':
      Vs = events.GenPart[i][(events.GenPart[i].status == 22) &
                            ((abs(events.GenPart[i].pdgId) == 23) |
                            (abs(events.GenPart[i].pdgId) == 24) )
                            ]
      print(" number Vs ", len(Vs))
      VV = Vs[0] + Vs[1]
      hists[var].Fill(VV.mass,xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'm_Jel' and ak.num(events.GenJetAK8)[i]>0 and ak.num(events.Electron.matched_gen)[i]>0 :
      J = events.GenJetAK8[i][0]
      el = events.Electron[i,0].matched_gen
      Jel = J+el
      hists[var].Fill(Jel.mass,xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])
    elif var == 'm_Jmu' and ak.num(events.GenJetAK8)[i]>0 and ak.num(events.Muon.matched_gen)[i]>0:
      J = events.GenJetAK8[i][0]
      mu = events.Muon[i,0].matched_gen
      Jmu = J+mu
      hists[var].Fill(Jmu.mass,xsec_times_BR*events[operator][opweight][i]/events.LHEWeight.originalXWGTUP[i])

  return hists[var]

inputfile = "aQGC_WMLEPWMHADjj_UL2018_input_2files.txt"
#inputfile = "aQGC_WMLEPWMHADjj_UL2018_input_10files.txt"
xsecfile = 'AQGC_xsec_times_BR.json'
#operatorsfile = 'aQGC_WPHADWMLEP_UL2018/operators.json'
operatorsfile = 'aQGC_WPHADWMLEP_UL2018/operators_test.json'

lines = []
with open(inputfile) as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print('line %s: %s'%(count,line))    

filetype = lines[0].split("/")[8]
print( "filetype ",filetype)
fileversion = lines[0].split("/")[9]


jsonxsecfile = open(xsecfile)
# returns JSON object as a dictionary
jsonxsecdata = json.load(jsonxsecfile)
xsec_times_BR = jsonxsecdata[filetype]
print("xsec_times_BR ",xsec_times_BR)
jsonxsecfile.close()

jsonoperatorsfile = open(operatorsfile)
# returns JSON object as a dictionary
jsonoperatorsdata = json.load(jsonoperatorsfile)
jsonoperatorsfile.close()

# to do this check, we want to consider only a few sample points for each operator. 
# If the weights are between -A and A, we consider -A, -A/2, 0 (=SM), A/2, A
# these selected values are saved in the dict below
shortoperatorsdata = {}
for operator in jsonoperatorsdata:
  #print("operator ",operator)
  length = len(jsonoperatorsdata[operator])
  smposition = int((length -1)/2)
  middle=int((length -1)/4)
  last = jsonoperatorsdata[operator][-1]
  middle_plus = jsonoperatorsdata[operator][-middle-1]
  sm = jsonoperatorsdata[operator][smposition]
  first = jsonoperatorsdata[operator][0]
  middle_minus = jsonoperatorsdata[operator][middle]
  shortoperatorsdata[operator] = [first,middle_minus,sm,middle_plus,last]
  #print(shortoperatorsdata[operator])

outfile = ROOT.TFile(filetype+"_"+fileversion+"_2files.root","RECREATE")


variables = {}

#variables["m_jj"]={'nbins':42,'xmin':800,'xmax':5000,'xaxistitle':'m_jj [GeV]'}
variables["m_VVgenpart"]={'nbins':42,'xmin':800,'xmax':5000,'xaxistitle':'m_{VV} [GeV]'}
variables["m_Jel"]={'nbins':42,'xmin':800,'xmax':5000,'xaxistitle':'m_{Je^{-}} [GeV]'}
variables["m_Jmu"]={'nbins':42,'xmin':800,'xmax':5000,'xaxistitle':'m_{J#mu} [GeV]'}
'''
variables["massJ"]={'nbins':40,'xmin':0,'xmax':200,'xaxistitle':'m_{J} [GeV]'}
variables["etaJ"] = {'nbins':20,'xmin':-5,'xmax':5,'xaxistitle':'#eta_{J}'}
variables["ptJ"] = {'nbins':100,'xmin':0,'xmax':1000,'xaxistitle':'pt_{J} [GeV]'}
variables["ptEl"] = {'nbins':10,'xmin':0,'xmax':50,'xaxistitle':'pt_{El} [GeV]'}
variables["ptMu"] = {'nbins':50,'xmin':0,'xmax':100,'xaxistitle':'pt_{Mu} [GeV]'}
'''
additionalvbfvariables = {}
additionalvbfvariables["deltaetaVBF"] = {'nbins':20,'xmin':-5,'xmax':5,'xaxistitle':'#Delta#eta_{jj}^{VBF}'}
additionalvbfvariables["eta1VBF"] = {'nbins':20,'xmin':-5,'xmax':5,'xaxistitle':'#eta_{1}^{VBF}'}
additionalvbfvariables["eta2VBF"] = {'nbins':20,'xmin':-5,'xmax':5,'xaxistitle':'#eta_{2}^{VBF}'}
additionalvbfvariables["pt1VBF"] = {'nbins':100,'xmin':0,'xmax':1000,'xaxistitle':'pt_{1}^{VBF} [GeV]'}
additionalvbfvariables["pt2VBF"] = {'nbins':100,'xmin':0,'xmax':1000,'xaxistitle':'pt_{2}^{VBF} [GeV]'}


hists = {}

for var in variables:
  print("var ", var)
  hists[var] = {}
  

  if var == 'm_jj':
    for vbfvar in additionalvbfvariables:
      hists[vbfvar] = {}
  for operator in shortoperatorsdata:
    print(" operator ",operator)
    hists[var][operator]={}
    if var == 'm_jj':
      for vbfvar in additionalvbfvariables:
        hists[vbfvar][operator] = {}
    for opweight in shortoperatorsdata[operator]:
      print(" opweight ",opweight)
      hists[var][operator][opweight] = None
      if var == 'm_jj':
        for vbfvar in additionalvbfvariables:
          hists[vbfvar][operator][opweight] = None

      for line in lines:
        if var == 'm_jj':
          if hists[var][operator][opweight] == None:
            hists[var][operator][opweight],hists["deltaetaVBF"][operator][opweight],hists["eta1VBF"][operator][opweight],hists["eta2VBF"][operator][opweight],hists["pt1VBF"][operator][opweight],hists["pt2VBF"][operator][opweight] = getVBShists(line,xsec_times_BR,var,operator,opweight)
          else: 
            tmp1,tmp2,tmp3,tmp4,tmp5,tmp6 = getVBShists(line,xsec_times_BR,var,operator,opweight)
            hists[var][operator][opweight].Add(tmp1)
            hists["deltaetaVBF"][operator][opweight].Add(tmp2)
            hists["eta1VBF"][operator][opweight].Add(tmp3)
            hists["eta2VBF"][operator][opweight].Add(tmp4)
            hists["pt1VBF"][operator][opweight].Add(tmp5)
            hists["pt2VBF"][operator][opweight].Add(tmp6)     
        else:
          if hists[var][operator][opweight] == None:
              hists[var][operator][opweight] = getHists(line,xsec_times_BR,var,operator,opweight)
          else:
              tmp = getHists(line,xsec_times_BR,var,operator,opweight)
              hists[var][operator][opweight].Add(tmp)  
              
      hists[var][operator][opweight].Write()
      if var == 'm_jj':
        for vbfvar in additionalvbfvariables:
          hists[vbfvar][operator][opweight].Write()      
     
outfile.Close()