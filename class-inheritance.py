#!/usr/local/bin/python3

## https://docs.python.org/3/
## https://pythonexamples.org/python-basic-examples/
## https://www.digitalocean.com/community/tutorial_series/how-to-code-in-python-3

import sys      # system library
import re       # regular expressions

# play with a class
class Name:
    # def __init__(self, first, last):
        # self.first = first
        # self.last = last

    # def __repr__(self):
    #     return str(self.__class__) + ": " + str(self.__dict__)

    # def __str__(self):
    #     return f"First: {self.first}, Last: {self.last}"

    # def __add__(x, y):
    #     return [ x, y ]

    def NamePrint(self):
        print('Name:', self)
        # if isinstance(self,list):
        #     for mine in self:
        #         mine.printName
        # else:
        #     print (f"First: {self.first}, Last: {self.last}")

class subName(Name):
    # def __init__(self):
    #     super().__init__(first, last)

    def subNamePrint(self):
        print('subName:', self)
        self.NamePrint()

# x = Name('Walter','Rowe')
y = subName()

# print(repr(x))
# print(repr(z))

# print(x)
y.subNamePrint()

# some other tests
# my_tupl = (1, 3, 5, 7, 9)
# my_list = [1, 3, 5, 7, 9]
# my_json = { 'first':'Walter', 'last':'Rowe'}
# my_othr = [ { 'first':'Walter', 'last':'Rowe'}, { 'first':'Walter', 'last':'Rowe'}, { 'first':'Walter', 'last':'Rowe'} ]

# print(f"my_tupl len = {len(my_tupl)}")
# print(f"my_list len = {len(my_list)}")
# print(f"my_json len = {len(my_json)}")
# print(f"my_othr len = {len(my_othr)}")
# print(f"my_othr[0] len = {len(my_othr[0])}")
