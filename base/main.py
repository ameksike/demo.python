"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""

from lib.ks_base import switch

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
        switch(option, self)


# .................................................................

obj = MyController()
obj.myAcction()
