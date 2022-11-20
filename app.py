import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys

from screens.menu import Ui_MainWindow
from services.menu_controller import MenuController

class main_app(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(main_app,self).__init__()
        #the window to open
        self.ui = Ui_MainWindow()
        #a window to be defined
        self.ui.setupUi(self)
        #menu controls
        self.menu_controller = MenuController(self)
        #button to start
        self.ui.btn_play.clicked.connect(self.menu_controller.run)
        #button to quit
        self.ui.btn_quit.clicked.connect(self.menu_controller.quit)
        
        
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)        
    window = main_app()
    window.show()
    sys.exit(app.exec_())


