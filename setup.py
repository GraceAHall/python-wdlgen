from setuptools import setup

__version__ = "v0.3.2"

DESCRIPTION = (
    "Contains classes and helpers to generate WDL without worrying about the syntax. "
    "This is primarily intended for generating WDL from other in-memory representations of a workflow."
)

# ======== SHOULDN'T NEED EDITS BELOW THIS LINE ======== #

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="illusional.wdlgen",
    version=__version__,
    description=DESCRIPTION,
    url="https://github.com/PMCC-BioinformaticsCore/python-wdlgen",
    author="Richard Lupat",
    author_email="richard.lupat@petermac.org",
    license="GNU",
    packages=["wdlgen"],
    install_requires=[],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
