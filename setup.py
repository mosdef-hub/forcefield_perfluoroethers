from setuptools import setup

setup(
    name="perfluoroethers",
    version="0.0",
    description="OPLS-AA perfluoroether plugin for foyer",
    url="http://github.com/mosdef-hub/forcefield_perfluoroethers",
    author="Jana E. Black, Christoph Klein, Matthew W. Thompson",
    author_email="matt.thompson@vanderbilt.edu",
    license="MIT",
    entry_points={
        "foyer.forcefields": [
            "PFE = perfluoroethers.perfluoroethers:PFE",
        ],
    },
    packages=["perfluoroethers"],
    zip_safe=False,
)
