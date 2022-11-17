import sys
from PyQt5 import QtWidgets
import PyQt5
from game import Game


class MenuController():
    def __init__(self, app):
        self.app = app
        self.game = Game()
        self.playing = False
    

    def run(self):
        self.app.close()
        self.game.start()
        
    def quit(self):
        self.app.close()

    def custumization(self):
        pass