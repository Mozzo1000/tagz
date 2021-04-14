from PyQt5.QtWidgets import QMainWindow, QLabel,QLineEdit, QWidget, QVBoxLayout, QPushButton
from lib.document import Document

class AddDocumentWindow(QMainWindow):
    def __init__(self, parent, fileinfo):
        super().__init__(parent)
        self.fileinfo = fileinfo
        self.setWindowTitle('Add file')
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        file_name_label = QLabel(self)
        file_name_label.setText('File: ')
        file_name = QLineEdit(self)
        file_name.setText(str(fileinfo))
        file_name.setReadOnly(True)

        add_button = QPushButton(self)
        add_button.setText('Add')
        add_button.clicked.connect(self.add_document)

        self.tag_input = QLineEdit(self)
        self.tag_input.setPlaceholderText('Tags,go,here')
        self.tag_input.returnPressed.connect(add_button.click)

        

        self.layout.addWidget(file_name_label)
        self.layout.addWidget(file_name)
        self.layout.addWidget(self.tag_input)
        self.layout.addWidget(add_button)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def add_document(self):
        for i in range(len(self.fileinfo)):
            new_doc = Document(self.fileinfo[i])
            new_doc.add(self.tag_input.text())
            new_doc.save_to_db()
        self.close()


class EditDocumentWindow(QMainWindow):
    def __init__(self, parent, fileinfo):
        super().__init__(parent)
        self.fileinfo = fileinfo
        self.setWindowTitle('Edit tags')
        self.main_widget = QWidget()
        self.layout = QVBoxLayout()

        save_button = QPushButton('Save')
        save_button.clicked.connect(self.edit_document)

        self.tag_input = QLineEdit(self)
        self.tag_input.setText(fileinfo.tags)
        self.tag_input.returnPressed.connect(save_button.click)

        

        self.layout.addWidget(self.tag_input)
        self.layout.addWidget(save_button)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

    def edit_document(self):
        doc = Document(self.fileinfo.file_name, file_hash=self.fileinfo.file_hash)
        doc.edit(self.tag_input.text())
        doc.save_to_db()
        self.close()