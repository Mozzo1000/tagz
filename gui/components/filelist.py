from PyQt5.QtWidgets import QDockWidget, QListWidget, QListWidgetItem, QMenu, QAction, QStyle, QMessageBox
import PyQt5.QtCore
from PyQt5.QtCore import Qt
from .property import PropertyWindow
from backend.utils import open_prog
from ..ui.document import EditDocumentWindow
from lib.document import Document

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
        remove_action = QAction('Remove', self)
        remove_action.triggered.connect(self.remove)

        menu.addAction(open_action)
        menu.addAction(info_action)
        menu.addAction(edit_action)
        menu.addAction(remove_action)

        menu.exec_(self.listview.mapToGlobal(position))

    def remove(self):
        data = self.listview.selectedItems()[0].data(Qt.UserRole)
        file = Document(file_name=data.file_name, file_hash=data.file_hash)
        file.remove()
        file.save_to_db()
        self.listview.takeItem(self.listview.currentRow())
        self.parent.taglist.refresh_listview()

    def open_edit(self):
        try:
            edit_window = EditDocumentWindow(self, self.listview.selectedItems()[0].data(Qt.UserRole))
            edit_window.show()
        except IndexError:
            QMessageBox.warning(self, "Warning", "Please select a file first to edit tags")


    def open_properties(self):
        try:
            properties = PropertyWindow(self.listview.selectedItems()[0].data(Qt.UserRole))
            self.parent.addDockWidget(Qt.RightDockWidgetArea, properties)
        except IndexError:
            QMessageBox.warning(self, "Warning", "Please select a file first to show info")

    def open_file(self):
        try:
            file_to_open = self.listview.selectedItems()[0].data(Qt.UserRole).file_path + "/" +  self.listview.selectedItems()[0].data(Qt.UserRole).file_name
            open_prog(file_to_open)
        except:
            QMessageBox.warning(self, "Warning", "Please select a file first to open")

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
            item.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileIcon')))
            self.listview.addItem(item)
        