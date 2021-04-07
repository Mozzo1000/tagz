from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem, QMenu, QAction
import PyQt5.QtCore
from PyQt5.QtCore import Qt
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
        self.listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listview.customContextMenuRequested.connect(self.open_action_menu)

        self.tags = Tags()

        self.populate_list()
        
        self.setWidget(self.listview)

    def open_action_menu(self, position):
        menu = QMenu()
        refresh_action = QAction('Refresh', self)
        refresh_action.triggered.connect(self.refresh_listview)
        menu.addAction(refresh_action)

        menu.exec_(self.listview.mapToGlobal(position))

    def refresh_listview(self):
        self.listview.clear()
        self.populate_list()

    def item_clicked(self, event):
        self.filelist.add_file(self.tags.get(event.text()))

    def populate_list(self):
        f = StringIO(self.tags.get_all())
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            for tag in row:
                item = QListWidgetItem(str(tag).strip())
                if item.text():
                    self.listview.addItem(item)
        self.listview.sortItems()
        