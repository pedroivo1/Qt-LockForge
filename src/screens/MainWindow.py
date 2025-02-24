from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QMainWindow, QVBoxLayout, QWidget)
from .PasswordGeneratorWindow import PasswordGeneratorWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('LockForge')
        self.set_position(0, 0)

        # self.setStyleSheet("""
        #     *:focus {
        #         background-color: #333333;  /* Cor de fundo quando em foco */
        #     }
        # """)


        central_widget = QWidget()
        central_widget.setFocusPolicy(Qt.NoFocus)
        main_layout = QVBoxLayout(central_widget)
        self.setCentralWidget(central_widget)

        self.password_generator_window = PasswordGeneratorWindow()
        main_layout.addWidget(self.password_generator_window)

        # self.setStyleSheet("""
        #     QLabel, QSpinBox, QTextEdit, QPushButton, QCheckBox {
        #         border: 2px solid red;
        #     }
        # """)

    def set_position(self, x, y):
        screen_geometry = self.screen().geometry()
        window_width = int(screen_geometry.width() * 0.5)
        self.setMinimumWidth(window_width)
        self.move(x, y)

    def set_icon(self, theme, BASE_DIR):
        if theme == 'dark':
            icon_path = BASE_DIR / "src/config/favicon_dark.png"
        else:
            icon_path = BASE_DIR / "src/config/favicon_light.png"
        self.setWindowIcon(QIcon(str(icon_path)))

    def no_focus(self):
        for child in self.findChildren(QWidget):
            print(f"Widget: {child.__class__.__name__}")
            child.setFocusPolicy(Qt.NoFocus)
