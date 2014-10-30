"""Iterate over parts of a cif file.
"""

import os
import sys
import argparse

here = os.path.abspath(os.path.dirname(__file__))
fr3d = os.path.abspath(os.path.join(here, ".."))
sys.path.insert(0, fr3d)

from fr3d.cif.reader import CIF


def main(filename):
    with open(filename, 'rb') as raw:
        structure = CIF(raw).structure()

    print('Iterating over all parts')
    for model in structure.models:
        print('model: %s' % model.model)
        for chain in model.chains:
            print(' chain: %s' % chain.chain)
            for residue in chain.residues():
                print('  residue: %s' % residue.unit_id())

    # You can use residues to iterate over the residues of a structure
    # directly.
    print('Short cut iteration')
    for residue in structure.residues():
        print(residue.unit_id())

    # The residues method accepts keyword arguments. These arguments are things
    # to filter the residues by. Below limits the residues to only those that
    # have sequence equal to 'A'.
    print('Iterating over specific residues')
    for residue in structure.residues(sequence='A'):
        print(residue.unit_id())

    # You can give more than one condition. Below limits the residues to only
    # those in chain B which are a G or C.
    print('Iterating over atoms')
    for residue in structure.residues(chain='B', sequence=['G', 'C']):
        for atom in residue.atoms():
            print(atom.unit_id())

    # You can also filter the atoms in the same way.
    print('Iterating over specific atoms')
    for residue in structure.residues(chain='A', sequence=['G', 'C']):
        for atom in residue.atoms(name=['N1', 'C2']):
            print(atom.unit_id())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument("cif", help="CIF file to read")
    args = parser.parse_args()
    main(args.cif)
