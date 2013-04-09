#!/usr/bin/python
'''
Oscar to nrrd code
'''

import sys
import os
import argparse
import logging

from scipy.io.matlab import loadmat
import nrrd

logger = logging.getLogger(__name__)

def convert(in_filename, out_filename=None, spacings=None):
    A = loadmat(in_filename, struct_as_record=False)

    # struct
    S = A['Save_data'][0,0]
    # volume
    V = S.P

    # output filename
    if out_filename == None:
        out_filename = os.path.splitext(in_filename)[0] + '.nrrd'
        
    logger.debug('Output filename: %s', out_filename)
    logger.debug('Writing NRRD file.')

    # NRRD options
    options = {}
    if spacings == None:
        xs = float((S.xmax - S.xmin) / V.shape[0])
        ys = float((S.ymax - S.ymin) / V.shape[1])
        zs = float((S.zmax - S.zmin) / V.shape[2])
        options['spacings'] = [xs, ys, zs]
    else:
        options['spacings'] = eval(spacings)

    logger.debug('Setting spacings to: %s', options['spacings'])

    nrrd.write(out_filename, V, options)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-v", "--verbose", action="store_true")
    parser.add_argument("-o", "--output", type=str, help="Output filename (Defaults to the input filename with an nrrd extension)")
    parser.add_argument("-s", "--spacing", type=str, default=None, help="Spacings")
    parser.add_argument("filename", type=str, help="Filename to convert")

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level = logging.DEBUG, format='%(asctime)s %(filename)s:%(funcName)s:%(levelname)s: %(message)s ')
    else:
        logging.basicConfig(level = logging.INFO, format='%(message)s')

    convert(args.filename, out_filename=args.output, spacings=args.spacing)

    logger.info('Done.')
