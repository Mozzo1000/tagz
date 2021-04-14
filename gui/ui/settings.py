from PyQt5.QtWidgets import QMainWindow, QPushButton, QCheckBox, QFontDialog, QMessageBox, \
    QComboBox, QListWidget, QHBoxLayout, QWidget, QStackedWidget, QFormLayout
from PyQt5.QtCore import QSize, QSettings

class SettingsWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('Settings')

        self.settings = QSettings('tagz', 'app')

        self.main_widget = QWidget()
        self.layout = QHBoxLayout()

        self.stack_widget = QStackedWidget(self)

        self.general_widget = QWidget(self)

        self.view_widget = QWidget()
        self.view_ui()

        self.stack_widget.addWidget(self.general_widget)
        self.stack_widget.addWidget(self.view_widget)

        settings_list = QListWidget(self)
        settings_list.currentRowChanged.connect(self.switch_display)
        settings_list.insertItem(0, 'General')
        settings_list.insertItem(1, 'View')

        save_btn = QPushButton("Save", self)
        save_btn.setToolTip("Save settings")
        save_btn.clicked.connect(self.save_settings)

        self.layout.addWidget(settings_list)
        self.layout.addWidget(self.stack_widget)
        self.layout.addWidget(save_btn)
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.load_settings()

    def view_ui(self):
        layout = QFormLayout()

        self.show_preview_by_default = QCheckBox("Show preview by default", self)
        self.show_preview_by_default.setTristate(False)

        layout.addRow(self.show_preview_by_default)

        self.view_widget.setLayout(layout)

    def switch_display(self, i):
        self.stack_widget.setCurrentIndex(i)

    def load_settings(self):
        if self.settings.contains('default_preview'):
            self.show_preview_by_default.setCheckState(self.settings.value('default_preview'))
        else:
            self.settings.setValue('default_preview', True)

    def save_settings(self):
        print("SAVE SETTINGS")
        self.settings.setValue('default_preview', self.show_preview_by_default.checkState())

        QMessageBox.question(self, 'Info', 'Please restart the application for changes to take affect.', QMessageBox.Ok)