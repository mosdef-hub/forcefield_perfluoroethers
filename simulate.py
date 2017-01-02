from foyer import Forcefield
from foyer.forcefield import generate_topology
#import mbuild as mb
import parmed as pmd

struct = pmd.load_file('molecules/Zdol.mol2', structure=True)
forcefield = Forcefield('PFEs.xml')
zdol =  forcefield.apply(struct)
# import sys; sys.exit()

# topology = generate_topology(struct)
# system = forcefield.createSystem(topology)
# zdol = pmd.openmm.load_topology(topology=topology, system=system, use_ids_as_types=True)


#system = mb.fill_box(compound=zdol, box=[4, 4, 4], n_compounds=500)
#forcefield = Forcefield(doi='10.5281/zenodo.56807')


#system.save('pfa.top', forcefield=forcefield)

print("Atoms: ", len(zdol.atoms))
for atom in zdol.atoms:
    print('Atom {} is typed as {}'.format(atom, atom.type))

print("Bonds: ", len(zdol.atoms))
for bond in zdol.bonds:
    print('{} '.format(bond))

print("Angles: ", len(zdol.atoms))
for angle in zdol.angles:
    print('{} '.format(angle))

print("Dihedrals: ", len(zdol.dihedrals))
for dihedral in zdol.dihedrals:
    print('{} '.format(dihedral))

print("RBs: ", len(zdol.rb_torsions))
for dihedral in zdol.rb_torsions:
    print('{} '.format(dihedral))
