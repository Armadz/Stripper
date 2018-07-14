"""stripper

Strips all trailling whitespace from a given flile or directory from the command line
"""

import argparse
import os.path

def file_strip(filename):
    """
    Checks to see if a commandline agrument is a valid file

    Returns: True or raises an error
    """


    with open(filename) as f:
        content = f.readlines()

    with open(filename, 'w') as f:
        f.write('\n'.join([line.rstrip() for line in content]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames',
        nargs='+',
        help = 'file to remove trailing whitespace from.'
        )

    args = parser.parse_args()

    for filename in args.filenames:
        file_strip(filename)
if __name__ == '__main__':
    main()
