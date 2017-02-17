from ROOT import *
import random 
from array import array
import itertools

def create_tree():
    #njet histo
    h_njet = TH1D("h_njet", "h_njet", 5, 0.5, 5.5)
    h_njet.SetBinContent(1, 5)
    h_njet.SetBinContent(2, 4)
    h_njet.SetBinContent(3, 3)
    h_njet.SetBinContent(4, 2)
    h_njet.SetBinContent(5, 1)

    #x histo
    h_x = TH1D("h_x", "h_x", 5, 0, 10)
    h_x.SetBinContent(1, 1)
    h_x.SetBinContent(2, 2)
    h_x.SetBinContent(3, 3)
    h_x.SetBinContent(4, 2)
    h_x.SetBinContent(5, 4)

    #eff(x) histo
    h_eff_true = TH1D("h_eff_true", "h_eff_true", 5, 0, 10);#could be different binning
    h_eff_true.SetBinContent(1, 0.1)
    h_eff_true.SetBinContent(2, 0.2)
    h_eff_true.SetBinContent(3, 0.2)
    h_eff_true.SetBinContent(4, 0.2)
    h_eff_true.SetBinContent(5, 0.3)

    f = TFile( 'toy.root', 'recreate' )
    t = TTree('treeR','')
    x_b = std.vector(float)()
    x_t = std.vector(float)()
    t.Branch( 'X_BASICCALOJETS1PT20', 'vector<float>', x_b )
    t.Branch( 'X_INCLUSIVETAGGEDCALOJETSE', 'vector<float>', x_t )

    h_count = TH1D("noCutSignature_COUNT", "noCutSignature_COUNT", 1, 0, 1)

    #loop over events
    for e in range(10000):
        h_count.Fill(0.5)

        x_b.clear()
        x_t.clear()

        #sample njet 
        njet = h_njet.GetRandom()
        njet_int = int(njet+0.5)

        for j in range(njet_int):

            #sample x
            x = h_x.GetRandom()
            x_b.push_back(x)
                       
            prob = h_eff_true.GetBinContent(h_eff_true.FindBin(x))
           
            #using h_eff_true, not from toys!
            r = random.random()
            if(r<prob):
                x_t.push_back(x)

        t.Fill()

    h_count.Write()
    t.Write()
    f.Write()

def main():

   create_tree() 

if __name__ == '__main__': main()
