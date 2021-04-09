from PyQt5.QtWidgets import QMainWindow, QLabel,QLineEdit, QWidget, QGridLayout, QLabel, QStyle
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class AboutWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('About Tagz')
        self.setFixedSize(272, 160)
        self.main_widget = QWidget()
        self.layout = QGridLayout()

        icon_label = QLabel("")
        icon = QIcon('assets/icon.png')
        icon_label.setPixmap(icon.pixmap(128))
        title_label = QLabel('<strong style="font-size: 22px">Tagz</strong><br/>Version 1.0.0<br/><br/>Copyright © 2021<br>Andreas Backström')
        
        link_label = QLabel('<a href="https://github.com/Mozzo1000/tagz">Source code</a>')
        link_label.setTextFormat(Qt.RichText)
        link_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        link_label.setOpenExternalLinks(True)


        self.layout.addWidget(icon_label, 0, 1)
        self.layout.addWidget(title_label, 0, 2)
        self.layout.addWidget(link_label, 1, 2)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
