#!/usr/bin/env python3
import argparse
import sys


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words between two files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("file1",
                        metavar="FILE1",
                        type=argparse.FileType("rt"),
                        help="Input file 1")

    parser.add_argument("file2",
                        metavar="FILE2",
                        type=argparse.FileType("rt"),
                        help="Input file 2")

    parser.add_argument("-o",
                        "--outfile",
                        metavar="FILE",
                        type=argparse.FileType("wt"),
                        default=sys.stdout,
                        help="Output file (default: stdout)")

    return parser.parse_args()


def get_words(filehandle):
    """Extract words from a file handle"""
    words = set()
    for line in filehandle:
        words.update(line.split())
    return words


def main():
    """Find common words"""

    args = get_args()

    words1 = get_words(args.file1)
    words2 = get_words(args.file2)

    common_words = sorted(words1 & words2)

    for word in common_words:
        print(word, file=args.outfile)


if __name__ == "__main__":
    main()
