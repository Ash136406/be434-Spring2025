#!/usr/bin/env python3
"""
Author : Your Name <your.email@example.com>
Date   : 2025-04-01
Purpose:
"""

import argparse
import pandas as pd
import os
import sys

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b', '--blasthits',
                        help='BLAST -outfmt 6 file',
                        metavar='FILE',
                        type=str,
                        required=True)

    parser.add_argument('-a', '--annotations',
                        help='Annotations file',
                        metavar='FILE',
                        type=str,
                        required=True)

    parser.add_argument('-o', '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=str,
                        default='out.csv')

    parser.add_argument('-d', '--delimiter',
                        help='Output field delimiter',
                        metavar='DELIM',
                        type=str,
                        default=None)

    parser.add_argument('-p', '--pctid',
                        help='Minimum percent identity',
                        metavar='PCTID',
                        type=float,
                        default=0.0)

    return parser.parse_args()

# --------------------------------------------------


def guess_delimiter(filename):
    """Guess delimiter based on file extension"""
    if filename.endswith('.csv'):
        return ','
    elif filename.endswith(('.tsv', '.tab', '.txt')):
        return '\t'
    return ','

# --------------------------------------------------


def read_csv(file, delimiter=None):
    """Read a CSV file with an optional delimiter"""
    delimiter = delimiter or guess_delimiter(file)
    return pd.read_csv(file, delimiter=delimiter, dtype=str)

# --------------------------------------------------


def main():
    """Main program"""
    args = get_args()

    for file in [args.blasthits, args.annotations]:
        if not os.path.isfile(file):
            print(f"Error: No such file or directory: '{file}'",
                  file=sys.stderr)
            exit(1)

    blast_df = read_csv(args.blasthits)
    meta_df = read_csv(args.annotations)

    required_blast_cols = {'qseqid', 'sseqid', 'pident', 'evalue'}
    if not required_blast_cols.issubset(blast_df.columns):
        print('Error: Missing required columns in BLAST file', file=sys.stderr)
        exit(1)

    blast_df['pident'] = blast_df['pident'].astype(float)
    filtered_blast = blast_df[blast_df['pident'] >= args.pctid]

    merged_df = filtered_blast.merge(meta_df, on='qseqid', how='left')

    output_df = merged_df[['qseqid', 'pident', 'depth', 'lat_lon']]
# might break code idk
    delimiter = args.delimiter or guess_delimiter(args.outfile)
    output_df.to_csv(args.outfile, index=False, sep=delimiter)
    print(f'Exported {len(output_df)} to "{args.outfile}".')
# AHHHHHHHHHHH

# --------------------------------------------------


if __name__ == '__main__':
    main()
