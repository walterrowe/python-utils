#!/usr/local/bin/python3

## https://docs.python.org/3/
## https://pythonexamples.org/python-basic-examples/
## https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3

import sys      # system library
import re       # regular expressions

def flatten_list(list_of_lists):
    flat_list = []
    for item in list_of_lists:
        if isinstance(item,list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# play with a class
class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self) -> str:
        return str(self.__class__) + ': ' + str(self.__dict__)

    def __str__(self) -> str:
        return f'First: {self.first}, Last: {self.last}'

    def __add__(x: list, y: list) -> list:
        return [ x, y ]

    def print(self):
        if isinstance(self,list):
            this_list = flatten_list(self)
            for item in this_list:
                item.print()
        else:
            print (f'First: {self.first}, Last: {self.last}')

x = Name('Walter','Rowe')
y = Name('Debbie','Rowe')
z = x + y

# print(repr(x))
# print(repr(z))

print(f'my_class len = {len(z)}')
print(f'x = {x}')
print(f'y = {y}')
Name.print(z)

# some other tests
my_tupl = (1, 3, 5, 7, 9)
my_list = [1, 3, 5, 7, 9]
my_json = { 'first':'Walter', 'last':'Rowe'}
my_othr = [ { 'first':'Walter', 'last':'Rowe'}, { 'first':'Walter', 'last':'Rowe'}, { 'first':'Walter', 'last':'Rowe'} ]

print(f'my_tupl len = {len(my_tupl)}')
print(f'my_list len = {len(my_list)}')
print(f'my_json len = {len(my_json)}')
print(f'my_othr len = {len(my_othr)}')
print(f'my_othr[0] len = {len(my_othr[0])}')
