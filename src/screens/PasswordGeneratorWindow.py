from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QSpinBox, QTextEdit, QPushButton, QCheckBox,
    QMessageBox)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt, Slot
import random

class PasswordGeneratorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title_label = QLabel('PASSWORD GENERATOR')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-weight: bold; font-size: 16px")

        self.char_count_selector = QSpinBox()
        self.char_count_selector.setRange(1, 1000)
        self.char_count_selector.setValue(10)

        self.password_display = QTextEdit()
        self.password_display.setReadOnly(True)

        self.generate_button = QPushButton("Create Password")
        self.generate_button.clicked.connect(self.create_password)

        self.uppercase_checkbox = QCheckBox('ABC')
        self.uppercase_checkbox.setChecked(True)
        self.lowercase_checkbox = QCheckBox('abc')
        self.lowercase_checkbox.setChecked(True)
        self.numbers_checkbox = QCheckBox('123')
        self.numbers_checkbox.setChecked(True)
        self.symbols_checkbox = QCheckBox('#$%')
        self.symbols_checkbox.setChecked(True)

        self.options_layout = QVBoxLayout()
        self.options_layout.addWidget(self.char_count_selector)
        self.options_layout.addWidget(self.uppercase_checkbox)
        self.options_layout.addWidget(self.lowercase_checkbox)
        self.options_layout.addWidget(self.numbers_checkbox)
        self.options_layout.addWidget(self.symbols_checkbox)

        self.output_layout = QVBoxLayout()
        self.output_layout.addWidget(self.password_display)
        self.output_layout.addWidget(self.generate_button)

        self.content_layout = QHBoxLayout()
        self.content_layout.addLayout(self.output_layout)
        self.content_layout.addLayout(self.options_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.content_layout)

        self.setLayout(self.main_layout)

        self.warning_label = QLabel('Select at least one option!')
        self.warning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning_label.setStyleSheet('background-color: yellow; font-size: 16px; color: red;')
        self.warning_label.setVisible(False)
        self.warning_label.setMaximumHeight(30)

    @Slot()
    def create_password(self):
        length = self.char_count_selector.value()

        characters = ""
        if self.uppercase_checkbox.isChecked():
            characters += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.lowercase_checkbox.isChecked():
            characters += 'abcdefghijklmnopqrstuvwxyz'
        if self.numbers_checkbox.isChecked():
            characters += '0123456789'
        if self.symbols_checkbox.isChecked():
            characters += '!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'  # removed this symbol: `

        if not characters:
            QMessageBox.information(self, "Empty Field", "Please select at least one option.", QMessageBox.Ok, QMessageBox.Ok)
            return

        password = ''.join(random.choices(characters, k=length))
        self.password_display.setPlainText(password)

    def print_widget_sizes(self):
        widgets = [
            self.title_label, 
            self.char_count_selector, 
            self.password_display, 
            self.generate_button, 
            self.uppercase_checkbox, 
            self.lowercase_checkbox, 
            self.numbers_checkbox, 
            self.symbols_checkbox
        ]
        
        for widget in widgets:
            print(f"Widget: {widget.__class__.__name__} - Width: {widget.width()} - Height: {widget.height()}")
