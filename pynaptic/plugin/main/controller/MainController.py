"""
 " @package    demos
 " @author     Antonio Membrides Espinosa
 " @email      tonykssa@gmail.com
 " @date       22/10/2019
"""
class MainController:
   def __init__(self):
      self.mainView = 0
      self.mainModel = 0

   def setModel(self, obj):
      self.mainModel = obj

   def setView(self, obj):
      self.mainView = obj

   def load(self):
      if self.mainView != 0:
         self.mainView.txtPath.setText("Haz clic en el botón y veras")


   def download(self):
      print("download Action")

   def list(self):
      print("list Action")

   def clear(self):
      print("clear Action")
