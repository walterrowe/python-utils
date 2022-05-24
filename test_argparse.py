#! /usr/local/bin/python3
"""
%(prog)s [ --help ] [ --group=group[,group...] ] [ --project=project[,project...] ] [ --commit ]

parameters:
    --help: prints this usage message
        (default is False)
    --group: comma separated list of one or more project paths or ids
    --project: comma separated list of one or more group paths or ids
    --config: section of ~/.python-config.cfg to load
    --commit: tells the script to make the change
        (default is False -- dry-run mode)

    group and project are mutually exclusive (specify one or the other, not both)
"""

import argparse

parser = argparse.ArgumentParser(description='test parsing arguments with argparse')
group = parser.add_mutually_exclusive_group()
group.add_argument('--group', dest='group', type=str, help='list of one or more group paths or ids', nargs='+')
group.add_argument('--project', dest='project', type=str, help='list of one or more project paths or ids', nargs='+')
parser.add_argument('--label', dest='label', type=str, help='name of label to use for overdue items', nargs=1, default='Overdue')
parser.add_argument('--color', dest='color', type=str, help='name of label to use for overdue items', nargs=1, default='red')
parser.add_argument('--section', dest='section', type=str, help='section of ~/.python-config.cfg to load', default='default')
parser.add_argument('--commit', dest='commit', help='tells the script to make the change', action='store_true')

options = parser.parse_args()

print(options)
# print(options.group)
# print(options.project)
# print(options.section)
# print(options.label)
# print(options.color)
# print(options.commit)
