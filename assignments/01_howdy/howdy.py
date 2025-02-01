#!/usr/bin/env python3

import argparse

# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""
    
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='Stranger', help='Name to greet')  #KEEP PARSER ARGUMENTS TOGETHER!!!!!!!
    parser.add_argument('-g', '--greeting', default='Howdy', help='Word to greet')
    parser.add_argument('-e', '--excited', action='store_true', help='Make excited')  #store true = must be true to have ?
    return parser.parse_args()
# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    if args.excited:
        excited = '!'
    else:
         excited = '.'

    print(f'{args.greeting}, {args.name}{excited}')

#------- KEEP AT BOTTOM 
if __name__ == '__main__':
    main()
# should pass all? 