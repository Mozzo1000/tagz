import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QWidget, QSizePolicy, QMenu, QAction, QFileDialog, QDockWidget
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import Qt
from gui.components.taglist import TagList
from gui.components.filelist import FileList
from gui.ui.document import AddDocumentWindow
from gui.ui.about import AboutWindow
from gui.components.search import GlobalSearchWindow
from gui.ui.settings import SettingsWindow

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Tagz GUI')
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setAcceptDrops(True)

        self.central_widget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        
        self.filelist = FileList(self)
        self.taglist = TagList(self.filelist)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.taglist)
        self.addDockWidget(Qt.RightDockWidgetArea, self.filelist)

        self._menubar()
        
        self.showMaximized()
        self.show()

    def _menubar(self):
        exit_action = QAction(QIcon('exit.png'), ' &Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        add_file_action = QAction('&Add file(s)', self)
        add_file_action.setStatusTip('Add file for tagging')
        add_file_action.triggered.connect(self.open_add_file)

        open_settings_action = QAction('&Settings', self)
        open_settings_action.setStatusTip('Open settings')
        open_settings_action.triggered.connect(self.open_settings)

        about_action = QAction('&About Tagz', self)
        about_action.setStatusTip('Show about window')
        about_action.triggered.connect(self.open_about)

        global_search_action = QAction('&Global search', self)
        global_search_action.setStatusTip('Show global search window')
        global_search_action.triggered.connect(self.open_global_search)
        global_search_action.setShortcut(QKeySequence("Ctrl+F"))

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(add_file_action)
        file_menu.addAction(open_settings_action)
        file_menu.addAction(exit_action)

        search_menu = menubar.addMenu('&Search')
        search_menu.addAction(global_search_action)

        help_menu = menubar.addMenu('&Help')
        help_menu.addAction(about_action)

    def open_settings(self):
        settings = SettingsWindow(self)
        settings.show()

    def open_global_search(self):
        for dock in self.findChildren(QDockWidget):
            dock_widget = dock
        if not "Global search" in dock_widget.windowTitle():
            search_window = GlobalSearchWindow(self.filelist)
            self.addDockWidget(Qt.LeftDockWidgetArea, search_window)
        else:
            dock_widget.show()
            dock_widget.search_input.setFocus()


    def open_about(self):
        about_window = AboutWindow(self)
        about_window.show()

    def open_add_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileNames(self,"Select file", "","All Files (*)", options=options)
        if fileName:
            add_document = AddDocumentWindow(self, fileName)
            add_document.show()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)
            add_document = AddDocumentWindow(self, f)
            add_document.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = Gui()
    sys.exit(app.exec_())