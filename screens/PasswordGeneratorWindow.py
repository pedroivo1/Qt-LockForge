from PySide6.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                               QHBoxLayout, QSpinBox)
from PySide6.QtCore import Qt

class PasswordGeneratorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        title = QLabel('Password Generator Window')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            """
                QLabel {
                    font-size: 18px;
                    font-weight: bold;
                }
            """
        )

        number_of_chars_selector = QSpinBox()
        number_of_chars_selector.setMaximum(20)
        number_of_chars_selector.setMinimum(5)

        content_layout = QHBoxLayout()
        content_window = QWidget()
        content_window.setLayout(content_layout)
        content_layout.addWidget(number_of_chars_selector)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(title)
        layout.addWidget(content_window)
