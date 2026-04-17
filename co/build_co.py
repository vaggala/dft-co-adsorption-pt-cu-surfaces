from ase.build import molecule
from ase.io import write

### need isolated CO because energy equation is
### E_ads = E_co+slab - E_slab - E_co
co = molecule("CO")

co.set_cell(
    [15.0, 15.0, 15.0]
)
co.center()
co.pbc = [False, False, False]

write("co.traj", co)

print("wrote co.traj")
print(co)

# for pt111
# Eatop_ads = E_pt+co(atop) - E_pt - E_co
# Efcc_ads = E_pt+co(fcc) - E_pt - E_co
# this last term is why you isolate co in this script