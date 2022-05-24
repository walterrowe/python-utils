#! /usr/local/bin/python3
"""
Script purpose line goes here

some other useful docstring text goes here
all of this will be included in the --help page
"""

import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=__doc__)
group = parser.add_mutually_exclusive_group()
group.add_argument('--group', dest='group', type=str, help='list of one or more group paths or ids', nargs='+')
group.add_argument('--project', dest='project', type=str, help='list of one or more project paths or ids', nargs='+')
parser.add_argument('--label', dest='label', type=str, help='name of label to use for overdue items', default='Overdue')
parser.add_argument('--color', dest='color', type=str, help='color of label to use for overdue items', default='red')
parser.add_argument('--section', dest='section', type=str, help='section of ~/.python-gitlab.cfg to load', default='default')
parser.add_argument('--commit', dest='commit', help='tells the script to make the change', action='store_true')

options = parser.parse_args()

print(options)
# print(options.group)
# print(options.project)
# print(options.section)
# print(options.label)
# print(options.color)
# print(options.commit)
