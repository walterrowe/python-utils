#! /usr/local/bin/python3

import sys
import Argv

args = Argv.parse(sys.argv, 'group=exclusive', 'project=exclusive', 'config', 'commit')
if args.passed:
    print(args)
