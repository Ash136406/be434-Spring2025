#!/usr/bin/env python3
"""
Author : Ashley Rigg
Date   : 2025-04-13
Purpose: Show conserved regions in FASTA sequences
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Show conserved regions in FASTA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input FASTA file')

    return parser.parse_args()


# --------------------------------------------------
def read_seqs(file_handle):
    """Read sequences from a FASTA file, ignoring headers"""

    seqs = []
    for line in file_handle:
        line = line.strip()
        if not line or line.startswith('>'):
            continue
        seqs.append(line)

    return seqs


# --------------------------------------------------
def get_conserved_line(seqs):
    """Return a line with '|' where all residues match, 'X' otherwise"""

    conserved = []

    for chars in zip(*seqs):
        if all(c == chars[0] for c in chars):
            conserved.append('|')
        else:
            conserved.append('X')

    return ''.join(conserved)


# --------------------------------------------------
def main():
    """Main program logic"""

    args = get_args()
    try:
        seqs = read_seqs(args.file)
        if not seqs:
            raise ValueError('No sequences found in file')

        conserved_line = get_conserved_line(seqs)
        for seq in seqs:
            print(seq)
        print(conserved_line)

    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
