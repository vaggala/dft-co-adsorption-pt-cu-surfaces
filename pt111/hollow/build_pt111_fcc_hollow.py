from ase.io import read, write
from ase.build import add_adsorbate, molecule

slab = read("../clean/pt111_clean.xyz")

# place CO above a top-layer Pt atom at x=0, y=0
add_adsorbate(slab, molecule("CO"), height=1.85, position=(0.0, 0.0))

write("pt111_atop.xyz", slab)

print(slab, "wrote pt111_atop.xyz")
