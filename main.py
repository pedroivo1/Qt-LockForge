import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon, QPalette
from screens.MainWindow import MainWindow
from qt_material import apply_stylesheet
from pathlib import Path

def set_theme(app):
    if app.palette().color(QPalette.Window).lightness() < 128:
        path = Path(r'config/dark.xml')
    else:
        path = Path(r'config/light.xml')

    apply_stylesheet(app, theme=str(path))

def set_icon(window):
    if app.palette().color(QPalette.Window).lightness() < 128:
        icon_path = Path(r'config/favicon_dark.png')
    else:
        icon_path = Path(r'config/favicon_light.png')
    window.setWindowIcon(QIcon(str(icon_path)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    set_theme(app)

    window = MainWindow()
    set_icon(window)
    window.show()
    sys.exit(app.exec())
