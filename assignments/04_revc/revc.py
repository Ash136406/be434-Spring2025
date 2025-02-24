#!/usr/bin/env python3
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Complement and reverse a DNA sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='str',
                        help='DNA sequence')

    parser.add_argument('-f',
                        '--file',
                        nargs='?',
                        help='File containing the DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def complement_and_reverse(seq: str) -> str:
    """Reverse the DNA sequence and get the complement, respecting the case"""

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
