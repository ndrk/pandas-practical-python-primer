"""
This module provides a CLI that...
"""
import argparse

parser = argparse.ArgumentParser(
    prog="My Cool Program",
    description="My cool program does a lot of cool things.",
    epilog="Thanks for using my cool program")

parser.add_argument("--filenames", nargs="+", metavar="FILENAME",
                    required=True, help="Names of files to copy.")

parser.add_argument('--destination', required=True,
                    dest='destination', help='Location to copy files to.')


program_arguments = parser.parse_args()
print(program_arguments)
