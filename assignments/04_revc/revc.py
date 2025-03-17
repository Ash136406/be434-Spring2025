#!/usr/bin/env python3
import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Complement and reverse a DNA sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='DNA',
                        help='DNA sequence or input file')

#    parser.add_argument('-f',
#                        '--file',
#                        nargs='?',
#                        help='File containing the DNA sequence')

# you can check to see if sequence is a file or string like so...
    args = parser.parse_args()

    if os.path.isfile(args.sequence):
        args.sequence = open(args.sequence).read().rstrip()

    return args


# --------------------------------------------------
def complement_and_reverse(seq: str) -> str:
    """Reverse the DNA sequence and get the complement, respecting the case"""
   
    # add in the lower case here too so you can match the case from the user
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    transformed = ''.join(complement[base.upper()]
                          if base.isupper()
                          else complement[base.upper()].lower()
                          for base in reversed(seq))
        
    return transformed

# --------------------------------------------------


def main():
    """Process input and print result"""

    args = get_args()

    seq = args.sequence

    transformed_seq = complement_and_reverse(seq)

    print(transformed_seq)


# --------------------------------------------------
if __name__ == '__main__':
    main()
