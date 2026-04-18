import ROOT
h = ROOT.TH1F("h", "Histogram", 10, 0, 10)
for i in range(10):
h.Fill(i)
print("Entries=",h.GetEntries())
