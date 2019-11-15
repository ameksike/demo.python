# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from plugin.main.view.mainwindow_ui import *

class MainView(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
