#!/usr/bin/env python3
"""
Author : Ashley Rigg
Date   : 2025-05-04
Purpose: Caesar cipher
"""

import argparse
import sys
from string import ascii_uppercase


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-n',
                        '--number',
                        metavar='NUMBER',
                        type=int,
                        default=3,
                        help='A number to shift')

    parser.add_argument('-d',
                        '--decode',
                        action='store_true',
                        help='A boolean flag')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Output file (default: stdout)')

    return parser.parse_args()


# --------------------------------------------------
def shift_char(char, shift_dict):
    """Shift a single character using the shift dictionary"""
    return shift_dict.get(char, char)


# --------------------------------------------------
def build_shift_dict(shift, decode=False):
    """Build Caesar cipher shift dictionary"""
    alpha = ascii_uppercase
    if decode:
        shift = -shift
    trans = {char: alpha[(i + shift) % 26] for i, char in enumerate(alpha)}
    return trans


# --------------------------------------------------
def main():
    """Caesar shift"""

    args = get_args()
    file_arg = args.file
    shift_num = args.number
    decode = args.decode
    out_fh = args.outfile or sys.stdout

    shift_dict = build_shift_dict(shift_num, decode)

    for line in file_arg:
        new_line = ''.join(
            shift_char(c.upper(), shift_dict) if c.isalpha() else c
            for c in line)
        print(new_line.rstrip(), file=out_fh)


# --------------------------------------------------
if __name__ == '__main__':
    main()
