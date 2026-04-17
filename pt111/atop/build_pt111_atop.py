from ase.io import read, write
from ase import Atoms

slab = read("../clean/pt111_clean.xyz")

# top surface height
z_top = max(
    atom.position[2] for atom in slab
)
# print(z_top)

# typical c-pt bond distance is 1.85 - 2.1 A.
# according to https://pubs.aip.org/aip/jcp/article/117/5/2264/453406/CO-on-Pt-111-puzzle-A-possible-solution
# same paper references that CO bond length is ~1.12 - 1.19 A
z_C = z_top + 1.85
z_O = z_C + 1.12

# place CO directly above pt atom top tayer at (0, 0)
co = Atoms(
    "CO",
    positions = [
        (0.0, 0.0, z_C), # carbon
        (0.0, 0.0, z_O)  # oxygen above carbon :)
    ]
)

slab += co # add CO to slab :)

# DEBUG
write("pt111_atop.xyz", slab)
print(slab, "wrote pt111_atop.xyz")
