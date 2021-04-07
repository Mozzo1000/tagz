from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem, QMenu, QAction
import PyQt5.QtCore
from PyQt5.QtCore import Qt
from .property import PropertyWindow
from backend.utils import open_prog
from ..ui.document import EditDocumentWindow

class FileList(QDockWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle('Files')

        self.listview = QListWidget()
        self.listview.itemDoubleClicked.connect(self.item_clicked)
        self.listview.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listview.customContextMenuRequested.connect(self.open_action_menu)
        
        self.setWidget(self.listview)

    def open_action_menu(self, position):
        menu = QMenu()
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        info_action = QAction('Info', self)
        info_action.triggered.connect(self.open_properties)
        edit_action = QAction('Edit', self)
        edit_action.triggered.connect(self.open_edit)

        menu.addAction(open_action)
        menu.addAction(info_action)
        menu.addAction(edit_action)

        menu.exec_(self.listview.mapToGlobal(position))

    def open_edit(self):
        edit_window = EditDocumentWindow(self, self.listview.selectedItems()[0].data(Qt.UserRole))
        edit_window.show()

    def open_properties(self):
        try:
            properties = PropertyWindow(self.listview.selectedItems()[0].data(Qt.UserRole))
            self.parent.addDockWidget(Qt.RightDockWidgetArea, properties)
        except IndexError:
            pass

    def open_file(self):
        file_to_open = self.listview.selectedItems()[0].data(Qt.UserRole).file_path + "/" +  self.listview.selectedItems()[0].data(Qt.UserRole).file_name
        open_prog(file_to_open)

    def item_clicked(self, event):
        file_to_open = event.data(Qt.UserRole).file_path + "/" +  event.data(Qt.UserRole).file_name
        open_prog(file_to_open)
        

    def add_file(self, file_objects, clear=True):
        if clear:
            self.listview.clear()
        if not file_objects:
            item = QListWidgetItem("No files has the selected tag")
            item.setFlags(Qt.NoItemFlags)
            self.listview.addItem(item)
        for object in file_objects:
            item = QListWidgetItem(object.file_name)
            item.setData(Qt.UserRole, object)
            self.listview.addItem(item)
        