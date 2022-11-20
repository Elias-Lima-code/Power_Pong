import sys
from PyQt5 import QtWidgets
import PyQt5
from game import Game


class MenuController():
    def __init__(self, app):
        #the app to be controlled
        self.app = app
        #the game to be played
        self.game = Game()
  
    def run(self):
        """menucontroller class function to start the game and close the menu screen
        """
        self.app.close()
        self.game.start()
        
    def quit(self):
        """menucontroller class function to quit the menu screen
        """
        self.app.close()

    def customization(self):
        """menucontroller class function to open the customization window 
        """
        pass