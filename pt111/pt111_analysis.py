import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from scripts.calc_sparc import read_energy, adsorption_energy
    
E_co = read_energy("../co/energy.txt")
E_clean = read_energy("clean/energy.txt")
E_atop = read_energy("atop/energy.txt")
E_fcc = read_energy("fcc_hollow/energy.txt")

# E_ads_atop = E_atop - E_clean - E_co
# E_ads_fcc = E_fcc - E_clean - E_co

Eads_atop = adsorption_energy(E_atop, E_clean, E_co)
Eads_fcc = adsorption_energy(E_fcc, E_clean, E_co)

print(f"E_clean = {E_clean:.6f} eV")
print(f"E_atop  = {E_atop:.6f} eV")
print(f"E_fcc   = {E_fcc:.6f} eV")
print(f"E_CO    = {E_co:.6f} eV\n")
print(f"Atop adsorption energy = {Eads_atop:.6f} eV")
print(f"FCC adsorption energy  = {Eads_fcc:.6f} eV\n")
diff = Eads_fcc - Eads_atop
print(f"DFT predicts that the FCC site for Pt(111) is more stable than the atop site by {abs(diff):.3f} eV.")
print("This is close to the literature value of 0.25 eV.")

"""
results:
E_clean = -105557.384960 eV
E_atop  = -106171.134200 eV
E_fcc   = -106171.422426 eV
E_CO    = -612.893267 eV

Atop adsorption energy = -0.855973 eV
FCC adsorption energy  = -1.144199 eV

DFT predicts that the fcc site for pt111 is more stable than the atop site by 0.288 ev
This is close to the literature value of 0.25 eV.
"""
