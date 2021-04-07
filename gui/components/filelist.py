from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem
import PyQt5.QtCore

class FileList(QDockWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Files')

        self.listview = QListWidget()
        self.listview.itemDoubleClicked.connect(self.item_clicked)
        
        self.setWidget(self.listview)

    def item_clicked(self, event):
        print(event.text())

    def add_file(self, file_objects, clear=True):
        if clear:
            self.listview.clear()
        for object in file_objects:
            item = QListWidgetItem(object.file_name)
            self.listview.addItem(item)
        