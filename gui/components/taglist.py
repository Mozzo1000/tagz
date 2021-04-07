from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem, QMenu, QAction, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStyle
from PyQt5.QtCore import Qt
from lib.tags import Tags
import csv
from io import StringIO

class TagList(QDockWidget):
    def __init__(self, filelist):
        super().__init__()
        self.filelist = filelist
        self.setWindowTitle('Tags')
        self.main_widget = QWidget(self)
        self.layout = QVBoxLayout(self)
        self.hlayout = QHBoxLayout(self)

        self.listview = QListWidget()
        self.listview.itemDoubleClicked.connect(self.item_clicked)
        self.listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listview.customContextMenuRequested.connect(self.open_action_menu)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Search...')
        self.search_input.textChanged.connect(self.search_changed)

        self.refresh_button = QPushButton()
        self.refresh_button.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_BrowserReload')))
        self.refresh_button.clicked.connect(self.refresh_listview)


        self.tags = Tags()

        self.populate_list()
        
        self.hlayout.addWidget(self.search_input)
        self.hlayout.addWidget(self.refresh_button)
        self.layout.addLayout(self.hlayout)
        self.layout.addWidget(self.listview)

        self.main_widget.setLayout(self.layout)
        self.setWidget(self.main_widget)

    def search_changed(self, event):
        items = self.listview.findItems(event, Qt.MatchRegularExpression)
        all_items = self.listview.findItems('*', Qt.MatchWildcard)
        for item in all_items:
            item.setHidden(True)
        for item in items:
            item.setHidden(False)
    
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
        