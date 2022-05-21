#! /usr/local/bin/python3

import sys
import argv

args = argv.parse(sys.argv, 'group=exclusive', 'project=exclusive', 'config', 'commit')
if args.passed:
    print(args)
