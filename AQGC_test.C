// Jay's code:  takes a text list of input files, an output root file, and an input cross section (see run.sh)
// makes histograms of a given variable (currently maximum m_{jj} per event for different working points of various operators and saves to the output           file
// currently setup for about the limits from SMP-18-006 (taken from figures 6,7,8 here: https://twiki.cern.ch/twiki/bin/view/CMSPublic/PhysicsResultsSMPaTGC           )

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <stdint.h>
#include <iomanip>
#include <ctime>
#include <map>
#include <math.h>

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

void AQGC_test(TString inputfile = "input.dat", TString outputfile = "output.root", float xsec = 0.9067 * 1000)
{

  TFile *outfile = new TFile(outputfile, "RECREATE");

  string var = "M_{jj}";
  int nbins = 22, xmin = 800, xmax = 3000;

  TH1D *hSM = new TH1D("hSM", var.c_str(), nbins, xmin, xmax);

  TH1D *hFS0 = new TH1D("hFS0", var.c_str(), nbins, xmin, xmax);
  TH1D *hFS1 = new TH1D("hFS1", var.c_str(), nbins, xmin, xmax);

  TH1D *hFM0 = new TH1D("hFM0", var.c_str(), nbins, xmin, xmax);
  TH1D *hFM1 = new TH1D("hFM1", var.c_str(), nbins, xmin, xmax);
  TH1D *hFM6 = new TH1D("hFM6", var.c_str(), nbins, xmin, xmax);
  TH1D *hFM7 = new TH1D("hFM7", var.c_str(), nbins, xmin, xmax);

  TH1D *hFT0 = new TH1D("hFT0", var.c_str(), nbins, xmin, xmax);
  TH1D *hFT1 = new TH1D("hFT1", var.c_str(), nbins, xmin, xmax);
  TH1D *hFT2 = new TH1D("hFT2", var.c_str(), nbins, xmin, xmax);

  std::ifstream ifs;
  ifs.open(inputfile.Data());
  assert(ifs.is_open());
  std::string line;
  int lineCount = 0;
  while (getline(ifs, line))
  {
    std::stringstream ss(line);
    std::string filetoopen;
    ss >> filetoopen;

    TFile *f = TFile::Open(TString(filetoopen), "READ");
    TTree *t = (TTree *)f->FindObjectAny("Events");

    Events et(t);

    Long64_t nentries = et.fChain->GetEntriesFast();
    Long64_t nbytes = 0, nb = 0;

    for (Long64_t i = 0; i < nentries; i++)
    {
      Long64_t ientry = et.LoadTree(i);
      nb = et.fChain->GetEntry(i);
      nbytes += nb;

      uint vbf1 = -1, vbf2 = -1;
      float mjj = 0.0;

      std::cout<< " nGenJet " << et.nGenJet << std::endl;
      for (uint j = 0; j < et.nGenJet; j++)
      {
        std::cout << "j "<<  j << " pt "<< et.GenJet_pt[j] <<std::endl;

        for (uint k = j + 1; k < et.nGenJet; k++)
        {

          std::cout << "k "<<  k << " pt "<< et.GenJet_pt[k] <<std::endl;

          TLorentzVector tmp1(0, 0, 0, 0);
          tmp1.SetPtEtaPhiM(et.GenJet_pt[j],
                            et.GenJet_eta[j],
                            et.GenJet_phi[j],
                            et.GenJet_mass[j]);

          TLorentzVector tmp2(0, 0, 0, 0);
          tmp2.SetPtEtaPhiM(et.GenJet_pt[k],
                            et.GenJet_eta[k],
                            et.GenJet_phi[k],
                            et.GenJet_mass[k]);

          TLorentzVector tempVBF = tmp1 + tmp2;
           //considering as vbs jets the two with the higher mjj 
          if (tempVBF.M() < mjj)
            continue;
          mjj = tempVBF.M();
          std::cout<< " mjj " << mjj << std::endl;
          //saving their corresponding index. This could be useful to plot more vbf related kinematic variables
          vbf1 = j; 
          vbf2 = k;
        }
      }




      float smWeight = et.fs0_0p00;

      // s0, s1, m0, m1, m6, m7, t0, t1, t2
      std::cout << " before filling " << mjj << std::endl;
      hSM->Fill(mjj, smWeight * xsec);

      hFS0->Fill(mjj, et.fs0_3p00 * xsec);
      hFS1->Fill(mjj, et.fs1_3p00 * xsec);

      hFM0->Fill(mjj, et.fm0_0p90 * xsec);
      hFM1->Fill(mjj, et.fm1_2p10 * xsec);
      // hFM6->Fill(mjj, et.fm6_3p00*xsec);
      hFM7->Fill(mjj, et.fm7_4p00 * xsec);

      hFT0->Fill(mjj, et.ft0_0p10 * xsec);
      hFT1->Fill(mjj, et.ft1_0p15 * xsec);
      hFT2->Fill(mjj, et.ft2_0p30 * xsec);
    }

    
    delete t;
    delete f;
  }
  // hSM->Draw("hist");
  // hFS0->Draw("histsame");

  outfile->Write();
  outfile->Close();
}
