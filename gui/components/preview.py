from PyQt5.QtWidgets import QWidget, QDockWidget, QLabel, QSizePolicy, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QPalette
from PyQt5.QtCore import Qt, QFileInfo, QSize

class FilePreview(QDockWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.setWindowTitle('Preview')
        self.allowed_images = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg']

        self.label = QLabel()

        scrollArea = QScrollArea()
        scrollArea.setWidget(self.label)
        scrollArea.setVisible(True)

        self.setWidget(scrollArea)
        self.validate_file()

    def validate_file(self):
        file_info = QFileInfo(self.data.data(Qt.UserRole).file_path + "/" + self.data.data(Qt.UserRole).file_name)
        if file_info.completeSuffix() in self.allowed_images:
            self.show_image()
        else:
            self.label.setText('The selected file cannot be previewed')
            self.label.adjustSize()

    def update_preview(self, data):
        self.data = data
        self.validate_file()

    def show_image(self):
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setScaledContents(True)
        #scrollArea.setWidgetResizable(True) # Fit to window
        pixmap = QPixmap(self.data.data(Qt.UserRole).file_path + "/" + self.data.data(Qt.UserRole).file_name)
        self.label.setPixmap(pixmap)
        self.label.adjustSize()

