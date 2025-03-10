#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-09
Purpose: Convert DNA sequences to RNA
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Convert DNA to RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--out_dir',
                        metavar='DIR',
                        type=str,
                        default='out',
                        help='Output directory')

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.out_dir
    files = args.files

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    total_seqs = 0
    for fh in files:
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        with open(out_file, 'wt') as out_fh:
            for line in fh:
                rna_seq = line.rstrip().replace('T', 'U')
                out_fh.write(rna_seq + '\n')
                total_seqs += 1

    print(f'Done, wrote {total_seqs} sequence' + ('' if total_seqs == 1 else 's') +
          f' in {len(files)} file' + ('' if len(files) == 1 else 's') +
          f' to directory "{out_dir}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
