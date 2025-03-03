#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-27
Purpose: Calculate GC content of a FASTA file
"""

import argparse
import sys  # Ensure sys is imported for stdin handling

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate GC content of a FASTA file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='?',
                        type=argparse.FileType('rt'),
                        default=None,
                        help='Input FASTA file')

    return parser.parse_args()

# --------------------------------------------------


def gc_content(seq):
    """Calculate GC content of a sequence"""
    return (seq.count('G') + seq.count('C')) / len(seq) * 100 if seq else 0


def main():
    """Main function"""

    args = get_args()
    name = None
    seq = []
    max_gc = 0
    max_name = None

    try:
        # Determine input source: file or stdin
        if args.file:
            f = args.file
        else:
            f = sys.stdin  # Use stdin if no file is provided

        # Read the input line by line
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if name:
                    # Compute GC content for the previous sequence
                    gc = gc_content(''.join(seq))
                    if gc > max_gc:
                        max_gc = gc
                        max_name = name
                name = line[1:]  # Extract sequence name (remove '>')
                seq = []  # Reset sequence list
            else:
                seq.append(line)  # Append sequence parts

        # Check last sequence after the loop ends
        if name:
            gc = gc_content(''.join(seq))
            if gc > max_gc:
                max_gc = gc
                max_name = name

        # Print the sequence with the highest GC content
        if max_name:
            print(f'{max_name} {max_gc:.6f}')

    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

# --------------------------------------------------


if __name__ == '__main__':
    main()
