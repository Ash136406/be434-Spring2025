#!/usr/bin/env python3
"""Generate synthetic DNA or RNA sequences."""

import random
import string
import sys
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import gc_fraction


def GC(sequence):
    """Calculate GC content percentage."""
    return 100 * gc_fraction(sequence, ambiguous="ignore")


def random_string(length=5):
    """Generate a random string of uppercase letters and digits."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits,
                                  k=length))


def generate_sequence(seq_type, length, pct_gc):
    """Generate a synthetic DNA or RNA sequence."""
    if seq_type == 'rna':
        bases = ['A', 'C', 'G', 'U']
    else:
        bases = ['A', 'C', 'G', 'T']

    sequence = []
    gc_count = int(length * pct_gc)
    at_count = length - gc_count

    sequence.extend(random.choices(['G', 'C'], k=gc_count))
    sequence.extend(random.choices(['A', 'T']
                                   if seq_type == 'dna' else ['A','U'], k=at_count))
    random.shuffle(sequence)

    return ''.join(sequence)


def main():
    """Main function to parse arguments and generate sequences."""
    parser = argparse.ArgumentParser(description="Generate synthetic DNA/RNA sequences")
    parser.add_argument("-m", "--minlen",
                        type=int,
                        default=50,
                        help="minimum length of sequences")
    parser.add_argument("-x", "--maxlen",
                        type=int,
                        default=75,
                        help="maximum length of sequences")
    parser.add_argument("-n", "--numseqs",
                        type=int,
                        default=10,
                        help="number of sequences")
    parser.add_argument("-o", "--output",
                        type=str,
                        default="out.fa",
                        help="output file name")
    parser.add_argument("-p", "--pctgc",
                        type=float,
                        default=0.5,
                        help="desired GC content as a fraction (0 to 1)")
    parser.add_argument("-t", "--seqtype",
                        type=str,
                        choices=["dna", "rna"],
                        default="dna",
                        help="sequence type")
    parser.add_argument("-s", "--seed",
                        type=int,
                        default=None,
                        help="random seed for reproducibility")

    args = parser.parse_args()

    if not (0 <= args.pctgc <= 1):
        parser.print_help()
        print(f"Error: --pctgc \"{args.pctgc}\" must be between 0 and 1")
        sys.exit(1)

    if args.seed is not None:
        random.seed(args.seed)

    seq_records = []
    for _ in range(args.numseqs):
        seq_len = random.randint(args.minlen,
                                 args.maxlen)
        seq = generate_sequence(args.seqtype,
                                seq_len,
                                args.pctgc)
        seq_records.append(SeqRecord(Seq(seq),
                                     id=random_string(),
                                     description=""))

    with open(args.output, "w") as out_file:
        SeqIO.write(seq_records,
                    out_file, "fasta")

    print(f"Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to \"{args.output}\".")


if __name__ == "__main__":
    main()
