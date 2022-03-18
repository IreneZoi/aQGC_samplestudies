#include <TROOT.h>
#include <TFile.h>
#include <TTree.h>
#include <TSystem.h>
#include <TString.h>
#include <TH1D.h>
#include <TH2D.h>
#include <TProfile.h>
#include <TF1.h>
#include <TMath.h>
#include <iostream>
#include <fstream>
#include "TRandom.h"
#include "TLorentzVector.h"
#include "Events.C"

void AQGC_test2() {

  TProfile *h = new TProfile("h","fs0",81,-40.5,40.5); //h->Sumw2();

  //TH1D *quad = new TH1D("quad","quad term",50,-1e-9,1e-9);
  //TH1D *lin = new TH1D("lin","lin term",50,-1e-9,1e-9);
  //TH1D *sm = new TH1D("sm","sm term",50,0,1e-5);

  TFile *f = new TFile("aQGC_WPHADWMLEPjj_UL2018.root","READ");
  TTree *t = (TTree*) f->FindObjectAny("Events");

  Events et(t);

  Long64_t nentries = et.fChain->GetEntriesFast();
  Long64_t nbytes = 0, nb = 0;

  for (Long64_t i=0; i<nentries; i++) {
    Long64_t ientry=et.LoadTree(i);
    nb = et.fChain->GetEntry(i);   nbytes += nb;
    //quad->Fill((et.fs0_0p75 + et.fs0_m0p75 - 2*et.fs0_0p00)/(2));
    //lin->Fill((et.fs0_0p75 - et.fs0_m0p75)/(2));
    //sm->Fill(et.fs0_0p00);

    h->Fill(0.0-40,et.fs0_m30p00);
    h->Fill(1-40,et.fs0_m29p25);
    h->Fill(2-40,et.fs0_m28p50);
    h->Fill(3-40,et.fs0_m27p75);
    h->Fill(4-40,et.fs0_m27p00);
    h->Fill(5-40,et.fs0_m26p25);
    h->Fill(6-40,et.fs0_m25p50);
    h->Fill(7-40,et.fs0_m24p75);
    h->Fill(8-40,et.fs0_m24p00);
    h->Fill(9-40,et.fs0_m23p25);
    h->Fill(10-40,et.fs0_m22p50);
    h->Fill(11-40,et.fs0_m21p75);
    h->Fill(12-40,et.fs0_m21p00);
    h->Fill(13-40,et.fs0_m20p25);
    h->Fill(14-40,et.fs0_m19p50);
    h->Fill(15-40,et.fs0_m18p75);
    h->Fill(16-40,et.fs0_m18p00);
    h->Fill(17-40,et.fs0_m17p25);
    h->Fill(18-40,et.fs0_m16p50);
    h->Fill(19-40,et.fs0_m15p75);
    h->Fill(20-40,et.fs0_m15p00);
    h->Fill(21-40,et.fs0_m14p25);
    h->Fill(22-40,et.fs0_m13p50);
    h->Fill(23-40,et.fs0_m12p75);
    h->Fill(24-40,et.fs0_m12p00);
    h->Fill(25-40,et.fs0_m11p25);
    h->Fill(26-40,et.fs0_m10p50);
    h->Fill(27-40,et.fs0_m9p75);
    h->Fill(28-40,et.fs0_m9p00);
    h->Fill(29-40,et.fs0_m8p25);
    h->Fill(30-40,et.fs0_m7p50);
    h->Fill(31-40,et.fs0_m6p75);
    h->Fill(32-40,et.fs0_m6p00);
    h->Fill(33-40,et.fs0_m5p25);
    h->Fill(34-40,et.fs0_m4p50);
    h->Fill(35-40,et.fs0_m3p75);
    h->Fill(36-40,et.fs0_m3p00);
    h->Fill(37-40,et.fs0_m2p25);
    h->Fill(38-40,et.fs0_m1p50);
    h->Fill(39-40,et.fs0_m0p75);
    h->Fill(40-40,et.fs0_0p00);
    h->Fill(41-40,et.fs0_0p75);
    h->Fill(42-40,et.fs0_1p50);
    h->Fill(43-40,et.fs0_2p25);
    h->Fill(44-40,et.fs0_3p00);
    h->Fill(45-40,et.fs0_3p75);
    h->Fill(46-40,et.fs0_4p50);
    h->Fill(47-40,et.fs0_5p25);
    h->Fill(48-40,et.fs0_6p00);
    h->Fill(49-40,et.fs0_6p75);
    h->Fill(50-40,et.fs0_7p50);
    h->Fill(51-40,et.fs0_8p25);
    h->Fill(52-40,et.fs0_9p00);
    h->Fill(53-40,et.fs0_9p75);
    h->Fill(54-40,et.fs0_10p50);
    h->Fill(55-40,et.fs0_11p25);
    h->Fill(56-40,et.fs0_12p00);
    h->Fill(57-40,et.fs0_12p75);
    h->Fill(58-40,et.fs0_13p50);
    h->Fill(59-40,et.fs0_14p25);
    h->Fill(60-40,et.fs0_15p00);
    h->Fill(61-40,et.fs0_15p75);
    h->Fill(62-40,et.fs0_16p50);
    h->Fill(63-40,et.fs0_17p25);
    h->Fill(64-40,et.fs0_18p00);
    h->Fill(65-40,et.fs0_18p75);
    h->Fill(66-40,et.fs0_19p50);
    h->Fill(67-40,et.fs0_20p25);
    h->Fill(68-40,et.fs0_21p00);
    h->Fill(69-40,et.fs0_21p75);
    h->Fill(70-40,et.fs0_22p50);
    h->Fill(71-40,et.fs0_23p25);
    h->Fill(72-40,et.fs0_24p00);
    h->Fill(73-40,et.fs0_24p75);
    h->Fill(74-40,et.fs0_25p50);
    h->Fill(75-40,et.fs0_26p25);
    h->Fill(76-40,et.fs0_27p00);
    h->Fill(77-40,et.fs0_27p75);
    h->Fill(78-40,et.fs0_28p50);
    h->Fill(79-40,et.fs0_29p25);
    h->Fill(80-40,et.fs0_30p00);
    
  }

  h->Draw("hist");

  double n00 = h->GetBinContent(41);
  double np1 = h->GetBinContent(42);
  double nm1 = h->GetBinContent(40);

  TF1 *approx = new TF1("approx", "[0]*x*x+[1]*x+[2]",-40,40);
  //approx->SetParameter(0,quad->GetMean());
  //approx->SetParameter(1,lin->GetMean());
  approx->SetParameter(0,0.5*(np1+nm1-2*n00));
  approx->SetParameter(1,0.5*(np1-nm1));
  approx->SetParameter(2,n00);

  approx->Draw("same");

}
