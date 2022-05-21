##
## parse argv command line options in the format of --key=value
##

import sys

class parse():
    def __init__(self, argv):
        self.options = {}
        for i in range(1, len(argv)):
            if argv[i].startswith('--') and '=' in argv[i]:
                key, val = argv[i][2:].split('=')
                if ',' in val:
                    val = list(val.split(','))
                self.options[key] = val

    def __dict__(self):
        return self.options.keys()

    def __str__(self):
        return f'{self.options}'
