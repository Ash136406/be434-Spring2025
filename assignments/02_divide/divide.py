#!/usr/bin/env python3
"""
Author : Ashley Rigg 
Date   : 2025-02-08
Purpose: Divide two numbers
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Perform integer division",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('num1', 
                        metavar='int', 
                        type=int, 
                        help="First integer")

    parser.add_argument('num2', 
                        metavar='int', 
                        type=int, 
                        help="Second integer")

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Perform division"""

    args = get_args()
    num1, num2 = args.num1, args.num2

    if num2 == 0:
                    print("usage: divide.py num1 num2", file=sys.stderr)
                    print("Cannot divide by zero, dum-dum!", file=sys.stderr)
                    sys.exit(1)

    result = num1 // num2
    print(f"{num1} / {num2} = {result}")

# --------------------------------------------------
##--
if __name__ == '__main__':
    main()