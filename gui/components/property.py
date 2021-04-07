from PyQt5.QtWidgets import QDockWidget, QTreeWidget, QTreeWidgetItem

class PropertyWindow(QDockWidget):
    def __init__(self, info):
        super().__init__()
        self.setWindowTitle('Info')

        self.treeview = QTreeWidget()
        self.treeview.setHeaderLabels(["Property", "Value"])
        name_item = QTreeWidgetItem(["Name", info.file_name])
        hash_item = QTreeWidgetItem(["Hash", info.file_hash])
        location_item = QTreeWidgetItem(["Location", info.file_path])
        tag_item = QTreeWidgetItem(["Tags", info.tags])
        created_item = QTreeWidgetItem(['Created', str(info.created)])

        self.treeview.addTopLevelItem(name_item)
        self.treeview.addTopLevelItem(hash_item)
        self.treeview.addTopLevelItem(location_item)
        self.treeview.addTopLevelItem(tag_item)
        self.treeview.addTopLevelItem(created_item)

        self.setWidget(self.treeview)