from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem
import PyQt5.QtCore
from lib.tags import Tags
import csv
from io import StringIO

class TagList(QDockWidget):
    def __init__(self, filelist):
        super().__init__()
        self.filelist = filelist
        self.setWindowTitle('Tags')

        self.listview = QListWidget()
        self.listview.itemDoubleClicked.connect(self.item_clicked)

        self.tags = Tags()

        self.populate_list()
        
        self.setWidget(self.listview)

    def item_clicked(self, event):
        self.filelist.add_file(self.tags.get(event.text()))

    def populate_list(self):
        f = StringIO(self.tags.get_all())
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for tag in row:
                item = QListWidgetItem(str(tag).strip())
                self.listview.addItem(item)
        