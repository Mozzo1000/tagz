from PyQt5.QtWidgets import QMainWindow, QLabel,QLineEdit, QWidget, QVBoxLayout, QPushButton
from lib.document import Document

class AddDocumentWindow(QMainWindow):
    def __init__(self, parent, fileinfo):
        super().__init__(parent)
        self.fileinfo = fileinfo
        self.setWindowTitle('Add file')
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self)

        file_name_label = QLabel(self)
        file_name_label.setText('File: ')
        file_name = QLineEdit(self)
        file_name.setText(fileinfo)
        file_name.setReadOnly(True)


        self.tag_input = QLineEdit(self)
        self.tag_input.setPlaceholderText('Tags,go,here')

        add_button = QPushButton(self)
        add_button.setText('Add')
        add_button.clicked.connect(self.add_document)

        self.layout.addWidget(file_name_label)
        self.layout.addWidget(file_name)
        self.layout.addWidget(self.tag_input)
        self.layout.addWidget(add_button)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def add_document(self):
        new_doc = Document(self.fileinfo)
        new_doc.add(self.tag_input.text())
        new_doc.save_to_db()
        self.close()
