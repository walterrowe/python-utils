#! /usr/local/bin/python3

import sys
import argv

args = argv.Parse(sys.argv, 'group=exclusive', 'project=exclusive', 'config', 'commit')
if args.passed:
    print(args)

if args.get('commit') == True:
    print('commit = true')
