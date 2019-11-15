"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from plugin.main.MainPlugin import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainPlugin()
    main.show()
    sys.exit(app.exec_())
