from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QApplication)
from .PasswordGeneratorWindow import PasswordGeneratorWindow
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('LockForge')
        self.set_position(0, 0)

        
        

        central_widget = QWidget()
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        password_generator_window = PasswordGeneratorWindow()
        main_layout.addWidget(password_generator_window)

    def set_position(self, x, y):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_width = int(screen_geometry.width() * 0.43)
        window_height = int(screen_geometry.height() * 0.5)
        self.resize(window_width, window_height)
        self.move(x, y)
