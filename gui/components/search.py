from PyQt5.QtWidgets import QDockWidget, QLineEdit, QPushButton, QWidget, QGridLayout, QButtonGroup, QCheckBox
from lib.document import Document

class GlobalSearchWindow(QDockWidget):
    def __init__(self, filelist):
        super().__init__()
        self.filelist = filelist
        self.setWindowTitle('Global search')

        self.main_widget = QWidget()
        self.layout = QGridLayout()


        search_button = QPushButton('Search')
        search_button.clicked.connect(self.search)
        self.search_input = QLineEdit()
        self.search_input.returnPressed.connect(search_button.click)

        button_group = QButtonGroup(self)
        button_group.setExclusive(True)
        check_1 = QCheckBox('File name')
        check_1.setChecked(True)
        button_group.addButton(check_1)
        
        self.layout.addWidget(self.search_input, 0, 0)
        self.layout.addWidget(search_button, 0, 1)
        self.layout.addWidget(check_1, 1, 0)


        self.main_widget.setLayout(self.layout)
        self.setWidget(self.main_widget)

    def search(self):
        if self.search_input.text():
            print(self.search_input.text())
            docs = Document(self.search_input.text(), file_hash='Dummy hash')
            print(docs.get())
            self.filelist.add_file(docs.get())
