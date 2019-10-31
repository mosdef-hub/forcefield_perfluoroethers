from glob import glob

import parmed as pmd
import pytest

import foyer
from foyer.tests.utils import atomtype

from perfluoroethers.perfluoroethers import load_PFE


MOL2_FILES = glob('test_molecules/*.mol2')
PFE = load_PFE()

@pytest.mark.parametrize('mol2_file', MOL2_FILES)
def test_atomtyping(mol2_file):
    structure = pmd.load_file(mol2_file, structure=True)
    foyer.tests.utils.atomtype(
        structure,
        PFE,
        assert_dihedral_params=False
    )
