from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QFont

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

label = QLabel("Texto Grande")
font = QFont()
font.setBold(True)
font.setPointSize(40)  # Tente aumentar para testar
label.setFont(font)

layout.addWidget(label)
window.setLayout(layout)
window.show()

app.exec()
