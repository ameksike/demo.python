"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""


import os.path
import importlib.machinery


def require(file, module='lib'):
    __NAME__ = file
    __PATH__ = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    loader = importlib.machinery.SourceFileLoader(module, __PATH__ + __NAME__)
    return loader.load_module(module)


lib = require('lib/ks.base.py')


class MyController:

    def __init__(self):
        pass

    def case0(self):
        print("Hello case: 0")

    def caseTest(self):
        print("Hello case: Test")

    def caseDemo1(self):
        print("Hello case: Demo1")

    def caseDefault(self):
        print("Hello case: Default")

    def myAcction(self):
        option = "Test-1"
        lib.switch(option, self)


# .................................................................

obj = MyController()
obj.myAcction()
