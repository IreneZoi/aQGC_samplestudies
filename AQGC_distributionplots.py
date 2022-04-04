# Irene's code inspired by Jay's code:  takes a text list of input files, an output root file, and an input cross section (see run.sh)
# makes histograms of a given variable (currently maximum m_{jj} per event for different working points of various operators and saves to the output           file
# currently setup for about the limits from SMP-18-006 (taken from figures 6,7,8 here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSMPaTGC           )
import ROOT, json
import sys,os
ROOT.gROOT.SetBatch(True)

def getCanvas():
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
 cname = "c"
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

def get_canvas_forRatio():

 H_ref = 600 
 W_ref = 600 
 W = W_ref
 H  = H_ref

 # references for T, B, L, R
 T = 0.07*H_ref
 B = 0.12*H_ref 
 L = 0.15*W_ref
 R = 0.05*W_ref

 cname="c"
 canvas = ROOT.TCanvas(cname,cname,W,H)
 canvas.SetFillColor(0)
 canvas.SetBorderMode(0)
 canvas.SetFrameFillStyle(0)
 canvas.SetFrameBorderMode(0)
 canvas.SetFrameBorderSize(0)
 canvas.SetFrameLineWidth(0)
 canvas.SetLeftMargin( L/W )
 canvas.SetRightMargin( R/W )
 canvas.SetTopMargin( T/H )
 canvas.SetBottomMargin( B/H )
 canvas.SetTickx(0)
 canvas.SetTicky(0)
 
 return canvas

def getLegend(x1=0.5809045,y1=0.6363636,x2=0.9522613,y2=0.8020979):
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

operatorsfile = 'aQGC_WPHADWMLEP_UL2018/operators.json'
#operatorsfile = 'aQGC_WPHADWMLEP_UL2018/operators_test.json'
inputfilename = 'aQGC_WMLEPWMHADjj_EWK_LO_NPle1_TuneCP5_13TeV-madgraph-pythia8_UL2018-NANOAODSIMv9_morefiles.root'
filetype = inputfilename.split("_")[0]+"_"+inputfilename.split("_")[1]
print( "filetype ",filetype)
fileversion = inputfilename.split("_")[-2]


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

inputfile = ROOT.TFile(inputfilename,'READ')

variables = ["m_VVgenpart","m_Jel","m_Jmu","massJ","etaJ","ptJ","ptEl","ptMu","m_jj","deltaetaVBF","eta1VBF","eta2VBF","pt1VBF","pt2VBF"] 
colors = ["#4292c6","#41ab5d","#ef3b2c","#17202A","#fdae61","#abd9e9","#2c7bb6"]
linestyle = [1,2,3,4,5,6,7,8,9]
markerstyle = [4,25,31,21,8]
ROOT.gStyle.SetOptStat(0)
for var in variables:
  for operator in shortoperatorsdata:
    print(" operator ",operator)
    canvas = get_canvas_forRatio()
    canvas.SetTitle(operator)
    legend = getLegend()
    # Upper histogram plot is pad1
    pad1 = ROOT.TPad("pad1", "pad1", 0, 0.31, 1, 1.0)
    pad1.SetBottomMargin(0)  # joins upper and lower plot
    pad1.SetRightMargin(0.05)
    pad1.SetLeftMargin(0.15)
    pad1.SetTopMargin(0.1)
    pad1.Draw()

    # Lower ratio plot is pad2
    canvas.cd()  # returns to main canvas before defining pad2
    pad2 = ROOT.TPad("pad2", "pad2", 0, 0.00, 1, 0.3)
    pad2.SetTopMargin(0)  # joins upper and lower plot
    pad2.SetBottomMargin(0.25)
    pad2.SetRightMargin(0.05)
    pad2.SetLeftMargin(0.15)
    pad2.Draw()

    pad1.cd()
    hist_r = []
    for i,opweight in enumerate(shortoperatorsdata[operator]):
      print(" opweight ",opweight)
      hist = inputfile.Get(var+"_"+operator+"_"+opweight)
      if opweight == "0p00": histSM = hist
      hist.SetTitle(operator)
      hist.SetLineColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
      hist.SetLineWidth(2)
      hist.SetLineStyle(linestyle[i])
      hist.SetMarkerColor(ROOT.TColor.GetColor(colors[i]))                                                                                                                                                                                                                
      hist.SetLineWidth(2)
      hist.SetMarkerStyle(markerstyle[i])
      hist_r.append(hist)
      if "pt" in var: pad1.SetLogy()
      legend.AddEntry(hist,opweight.replace("m","-").replace("p","."))
      hist.Draw("Psame")
    legend.Draw("same")
    pad2.cd()
    
    h = []
    for i,opweight in enumerate(shortoperatorsdata[operator]):
      if opweight != "0p00":
        h.append(hist_r[i].Clone())
        h[-1].Divide(histSM)
        h[-1].SetTitle("")
        h[-1].Draw("Psame")
    h[0].GetXaxis().SetTitle(str(h[0].GetXaxis().GetTitle()).replace("pt","p_{T}").replace("_{El}","^{e^{-}}").replace("_{Mu}","^{#mu}"))
    h[0].GetXaxis().SetTitleSize(0.11)
    h[0].GetXaxis().SetLabelSize(0.11)
    h[0].GetYaxis().SetTitleSize(0.11)
    h[0].GetYaxis().SetTitle("weight/SM")
    h[0].GetYaxis().SetTitleOffset(0.5)
    h[0].GetYaxis().SetLabelSize(0.11)
    h[0].GetYaxis().SetRangeUser(0.,10.)
    h[0].GetYaxis().SetNdivisions(5)
    linea =  ROOT.TLine(histSM.GetXaxis().GetXmin(),1.,histSM.GetXaxis().GetXmax(),1.)
    linea.SetLineColor(17)
    linea.SetLineWidth(2)
    linea.SetLineStyle(2)
    linea.Draw("same")
    try:
      os.mkdir(filetype+"_"+fileversion)
    except:
      print()  
    canvas.SaveAs(filetype+"_"+fileversion+"/"+var+"_"+operator+".pdf")  
    canvas.SaveAs(filetype+"_"+fileversion+"/"+var+"_"+operator+".png")  
