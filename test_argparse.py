#! /usr/local/bin/python3
"""
Script purpose line goes here

this is python docstring text which has to appear first after shebang
python docstring is always started and ended with triple-quote marks
all of this will be included in the --help page via 'epilog=__doc__'
"""

import argparse

parser = argparse.ArgumentParser(add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
group = parser.add_mutually_exclusive_group()
group.add_argument('--group', dest='group', type=str, help='list of one or more group paths or ids', nargs='+')
group.add_argument('--project', dest='project', type=str, help='list of one or more project paths or ids', nargs='+')
parser.add_argument('--label', dest='label', type=str, help='name of label to use for overdue items', default='Overdue')
parser.add_argument('--color', dest='color', type=str, help='name of label to use for overdue items', default='red')
parser.add_argument('--section', dest='section', type=str, help='section of ~/.python-gitlab.cfg to load', default='default')
parser.add_argument('--commit', dest='commit', help='tells the script to make the change', action='store_true')

options = parser.parse_args()

print(options)
