#!/usr/bin/env python3
"""
Author : Ashley Rigg
Date   : 2025-04-20
Purpose: Compress a DNA sequence using run-length encoding (RLE)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Compress a DNA sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A sequence string or a file containing one')

    return parser.parse_args()


# --------------------------------------------------
def read_sequence(s):
    """Return the sequence either directly or from file"""

    if os.path.isfile(s):
        with open(s, 'rt') as fh:
            return fh.read().strip()
    else:
        return s


# --------------------------------------------------
def compress(seq):
    """Compress sequence using run-length encoding"""

    if not seq:
        return ''

    result = []
    prev = seq[0]
    count = 1

    for char in seq[1:]:
        if char == prev:
            count += 1
        else:
            result.append(prev if count == 1 else f'{prev}{count}')
            prev = char
            count = 1

    result.append(prev if count == 1 else f'{prev}{count}')
    return ''.join(result)


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    seq = read_sequence(args.positional)
    print(compress(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
