#! /usr/local/bin/python3
"""
%(script)s [ --help ] [ --group=group[,group...] ] [ --project=project[,project...] ] [ --commit ]

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
import sys
import argv

options = argv.Parse(sys.argv, 'help', 'group=exclusive', 'project=exclusive', 'config', 'commit')
if options.passed != True or options.get('help') == True:
    print(__doc__ % { "script" : sys.argv[0].split('/')[-1] } )
    exit()

print(args)
