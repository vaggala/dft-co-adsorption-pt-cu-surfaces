from ase.build import fcc111
from ase.io import write

# build a Pt(111) slab
# size = (nx, ny, layers)

slab = fcc111(
    "Pt",
    size=(3, 3, 4),
    a=3.92,          
    vacuum=15.0      
)

slab.center(axis=2, vacuum = 15.0)

write("pt111_clean.xyz", slab)

print(slab, "successfully wrote pt111_clean.xyz")