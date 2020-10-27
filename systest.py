#! /usr/bin/env python3
# accept arguments when you start the program

import sys
if(len(sys.argv) == 2):
    print(f'The argument was {sys.argv[1]}.')
    print(f'The name of the script was {sys.argv[0]}.')
else:
    sys.stderr.write(f"Usage: systest.py [argument]\n")

