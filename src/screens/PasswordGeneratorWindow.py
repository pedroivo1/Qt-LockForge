from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QHBoxLayout,
    QSpinBox, QTextEdit, QPushButton, QCheckBox,
    QMessageBox, QSizePolicy, QLineEdit
)
from PySide6.QtGui import QClipboard
from PySide6.QtCore import Qt, Slot, QTimer
import random

class PasswordGeneratorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Título
        self.title_label = QLabel('PASSWORD GENERATOR')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-weight: bold; font-size: 20px; max-height: 30px")

        # Seleção de tamanho da senha
        # self.char_count_label = QLabel('Password Size')
        # self.char_count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.char_count_label.setStyleSheet("font-weight: bold;")
        self.char_count_selector = QSpinBox()
        self.char_count_selector.setRange(1, 1000)
        self.char_count_selector.setValue(10)
        

        # Display de senha
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setFocusPolicy(Qt.NoFocus)
        self.password_display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.password_display.setMaximumHeight(82)

        # Botão de copiar
        self.copy_button = QPushButton("Copy")
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.copy_button.setFocusPolicy(Qt.NoFocus)

        # Botão para gerar senha
        self.generate_button = QPushButton("Create Password")
        self.generate_button.clicked.connect(self.create_password)
        self.generate_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.generate_button.setFocusPolicy(Qt.NoFocus)
        

        # Checkboxes de opções
        # self.check_box_label = QLabel('Used Characters')
        # self.check_box_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.check_box_label.setStyleSheet("font-weight: bold;")
        self.uppercase_checkbox = QCheckBox('ABC')
        self.uppercase_checkbox.setChecked(True)
        self.uppercase_checkbox.setFocusPolicy(Qt.NoFocus)
        self.lowercase_checkbox = QCheckBox('abc')
        self.lowercase_checkbox.setChecked(True)
        self.lowercase_checkbox.setFocusPolicy(Qt.NoFocus)
        self.numbers_checkbox = QCheckBox('123')
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.setFocusPolicy(Qt.NoFocus)
        self.symbols_checkbox = QCheckBox('#$%')
        self.symbols_checkbox.setChecked(True)
        self.symbols_checkbox.setFocusPolicy(Qt.NoFocus)

        # Layout de options
        self.options_layout = QHBoxLayout()
        self.options_layout.addWidget(self.char_count_selector, 1)
        self.options_layout.addWidget(self.uppercase_checkbox, 1)
        self.options_layout.addWidget(self.lowercase_checkbox, 1)
        self.options_layout.addWidget(self.numbers_checkbox, 1)
        self.options_layout.addWidget(self.symbols_checkbox, 1)

        # Layout de botões de ação
        self.action_buttons_layout = QVBoxLayout()
        self.action_buttons_layout.addWidget(self.generate_button)
        self.action_buttons_layout.addWidget(self.copy_button)

        # Layout principal do display de senha e botões
        self.top_layout = QHBoxLayout()
        self.top_layout.addLayout(self.action_buttons_layout)
        self.top_layout.addWidget(self.password_display)

        # Layout de conteúdo
        self.content_layout = QVBoxLayout()
        self.content_layout.addLayout(self.top_layout)
        self.content_layout.addLayout(self.options_layout)

        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.content_layout)

        # Definir o layout principal da janela
        self.setLayout(self.main_layout)

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
            characters += '!\"#$%&\'()*+,-./:;<=>?@[\]^_{|}~'

        if not characters:
            message = QMessageBox.information(self, "Empty Field", "Please select at least one option.", QMessageBox.Ok, QMessageBox.Ok)
            message.setFocusPolicy(Qt.NoFocus)
            return

        password = ''.join(random.choices(characters, k=length))
        self.password_display.setText(password)

    @Slot()
    def copy_password(self):
        password = self.password_display.text()
        clipboard = QClipboard(self)
        clipboard.setText(password)
        self.copy_button.setText('Copied')
        QTimer.singleShot(2000, self.copy_button_reset)

    def copy_button_reset(self):
        self.copy_button.setText('Copy')
        self.copy_button.clearFocus()

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
