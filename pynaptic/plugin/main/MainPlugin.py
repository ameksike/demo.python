"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""
from plugin.main.model.RepoModel import *
from plugin.main.controller.MainController import *
from plugin.main.view.MainView import *

class MainPlugin:
    def __init__(self):
       self.mainView = MainView()
       self.mainController = MainController()
       self.repoModel = RepoModel()

       self.mainController.setModel(self.repoModel)
       self.mainController.setView(self.mainView)

       # ... event manager
       self.mainView.btnLoad.clicked.connect(self.mainController.load)

       # pyuic5 -x plugin/main/view/mainwindow.ui -o  plugin/main/view/mainwindow_ui.py

    def show(self):
       self.mainView.show()


