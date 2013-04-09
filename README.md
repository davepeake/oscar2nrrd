oscar2nrrd
==========

A script to convert between OSCaR reconstruction volumes and nrrd for use in Slicer

Install
=======

Using git:

    git clone https://github.com/davepeake/oscar2nrrd.git
    git submodule init 
    cd pynrrd
    python setup.py install

Usage
=====
    usage: oscar2nrrd.py [-h] [-v] [-o OUTPUT] [-s SPACING] filename

    positional arguments:
        filename              Filename to convert

    optional arguments:
        -h, --help            show this help message and exit
        -v, --verbose
        -o OUTPUT, --output OUTPUT
                            Output filename (Defaults to the input filename with
                            an nrrd extension)
        -s SPACING, --spacing SPACING
                            Spacings

Requirements / Links
====================
* pynrrd: https://github.com/mhe/pynrrd
* OSCaR: http://www.cs.toronto.edu/~nrezvani/OSCaR.html
* Slicer: http://www.slicer.org
