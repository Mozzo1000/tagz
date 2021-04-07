import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QSizePolicy
from PyQt5.QtCore import Qt
from gui.components.taglist import TagList
from gui.components.filelist import FileList

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Tagz GUI')

        self.central_widget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        filelist = FileList()
        taglist = TagList(filelist)
        self.addDockWidget(Qt.LeftDockWidgetArea, taglist)
        self.addDockWidget(Qt.RightDockWidgetArea, filelist)

        self.showMaximized()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())