# from PyQt5 import QtGui
# from PyQt5 import QtWidgets

# class ImageWidget(QtGui.QWidget):
#     def __init__(self,game,parent=None):
#         super(ImageWidget,self).__init__(parent)
#         width= game.screen.get_width()
#         height= game.screen.get_height()
#         self.data= game.screen.get_buffer().raw
#         self.image=QtGui.QImage(self.data,width,height,QtGui.QImage.Format_RGB32)

#     def paintEvent(self,event):
#         qp=QtGui.QPainter()
#         qp.begin(self)
#         qp.drawImage(0,0,self.image)
#         qp.end()
