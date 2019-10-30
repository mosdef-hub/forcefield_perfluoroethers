import os
import glob
from pkg_resources import resource_filename

from foyer import Forcefield


def get_ff_path():
    return [resource_filename('perfluoroethers', 'xml')]


def get_perfluoroether_forcefield_path():
    for dir_path in get_ff_path():
        file_pattern = os.path.join(dir_path, '*.xml')
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
    return file_paths


def get_perfluoroether_forcefield():
    return Forcefield(get_perfluoroether_forcefield_path())


PFE = get_perfluoroether_forcefield()
