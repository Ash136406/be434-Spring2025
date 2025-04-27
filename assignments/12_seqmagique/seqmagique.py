#!/usr/bin/env python3
"""
Author : Your Name <you@example.com>
Date   : 2025-04-26
Purpose: 
"""

import os
import argparse
from typing import List, NamedTuple, TextIO
from tabulate import tabulate
from Bio import SeqIO


# --------------------------------------------------
class Args(NamedTuple):
    """Command-line arguments"""
    files: List[TextIO]
    tablefmt: str


class FastaInfo(NamedTuple):
    """FASTA file information"""
    filename: str
    min_len: int
    max_len: int
    avg_len: float
    num_seqs: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mimic seqmagick',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        metavar='table',
                        type=str,
                        choices=[
                            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst',
                            'mediawiki', 'latex', 'latex_raw', 'latex_booktabs'
                        ],
                        default='plain',
                        help='Tabulate table style')

    args = parser.parse_args()

    return Args(args.file, args.tablefmt)


# --------------------------------------------------
def main():
    """Main program"""

    args = get_args()
    results = []

    for fh in args.files:
        lengths = [len(rec.seq) for rec in SeqIO.parse(fh, 'fasta')]
        filename = os.path.relpath(fh.name)
        num_seqs = len(lengths)
        min_len = min(lengths) if lengths else 0
        max_len = max(lengths) if lengths else 0
        avg_len = sum(lengths) / num_seqs if num_seqs > 0 else 0.0

        results.append(
            FastaInfo(filename, min_len, max_len, avg_len, num_seqs))

    headers = ["name", "min_len", "max_len", "avg_len", "num_seqs"]
    print(tabulate(results,
                   headers=headers,
                   floatfmt='.2f',
                   tablefmt=args.tablefmt))


# --------------------------------------------------
if __name__ == '__main__':
    main()
