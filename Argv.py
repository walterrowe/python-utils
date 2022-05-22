##
## module: argv
## class: parse
##
## date: 2022-05-21
## auth: walter rowe <walter.rowe@nist.gov>
##

class Parse:
    '''

    This class parses sys.argv arguments into a key-value dictionary

    - pass a list of allowed keys and it filters for only those keys
    - pass a list of allowed keys and they are initialize to empty list
    - filter options can include '=exclusive' to be mutually exclusive
    - with no key filters it will parse all options into key-values
    - keys with no values specified on command line are set to True

    Command line options must be "--key" or "--key=value[,value...]"

    All other command line arguments are ignored

    Parse the command line arguments via:
        args = argv.parse(sys.argv [, 'option1[=exclusive]', ..., 'optionN' ])

    Get the value of a key via
        value = args.options[key]
        value = args.get(key)

    '''

    def __init__(self, argv=None, *allowed):
        '''
        Parse sys.argv command line via:
            args = argv.parse(sys.argv [, 'option1[=exclusive]', ..., 'optionN' ])
        '''
        self.argv = argv                # preserve original argv
        self.allowed = []               # preserve allowed args
        self.exclusive = []             # list of exclusive args
        self.passed = True
        self.options = {}               # initialize options dict
        seen = []

        if self.argv == None or len(argv) == 0:
            print(self.__doc__)
            return None

        # if passed a list of allowed options, initialize and build exclusive list
        if len(allowed) > 0:
            for key in allowed:
                if '=' in key:
                    key, val = key.split('=')
                    if val != None and val.lower() == 'exclusive' and key not in self.exclusive:
                        self.exclusive.append(key)
                self.allowed.append(key)
                self.options[key] = []

        # parse argv into key-value pairs and add to options dictionary
        for i in range(1, len(argv)):
            if argv[i].startswith('--'):
                if '=' in argv[i]:
                    key, val = argv[i][2:].split('=')
                    if ',' in val:
                        val = list(val.split(','))
                    if allowed == None or key in self.options.keys():
                        if isinstance(val,list):
                            for this_val in val:
                                self.options[key].append(this_val)
                        else:
                            self.options[key].append(val)
                        # build a list of options seen
                        if key not in seen:
                            seen.append(key)
                else:
                    key = argv[i][2:]
                    if allowed == None or key in self.options.keys():
                        self.options[key] = True
                        seen.append(key)

        # evaluate seen options for exclusive arguments
        keys = [ x for x in seen if x in self.exclusive ]
        if len(keys) > 1:
            print('the following arguments are exclusive:', *keys)
            self.passed = False

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __str__(self):
        return f'{self.options}'

    def get(self, key):
        '''
        Get the value of a key via
            value = args.options[key]
            value = args.get(key)

        '''
        if key in self.options.keys():
            return self.options[key]
        else:
            return None

    def show(self):
        '''
        Show the values of an argv object
        '''
        print(f'command: ', *self.argv)
        print(f'passed: ', self.passed)
        print(f'allowed: ', *self.allowed)
        print(f'exclusive: ', *self.exclusive)

        if len(self.options.keys()) > 0:
            print('parsed options:')
            for key in self.options.keys():
                print (f'  {key}: {self.options[key]}')
