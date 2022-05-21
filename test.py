import sys
import argv

argv = argv.parse(sys.argv)
for key in argv.options.keys():
    print(f'{key} => {argv.options[key]}')
