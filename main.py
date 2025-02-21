import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPalette
from src.screens.MainWindow import MainWindow
from qt_material import apply_stylesheet
from pathlib import Path

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_theme_change)
        self.timer.start(200)
        self.previous_theme = self.get_current_theme()
        self.set_theme()

    def get_current_theme(self):
        return "dark" if self.palette().color(QPalette.Window).lightness() < 128 else "light"

    def check_theme_change(self):
        current_theme = self.get_current_theme()
        if current_theme != self.previous_theme:
            self.previous_theme = current_theme
            self.set_theme()

    def set_theme(self):
        if self.palette().color(QPalette.Window).lightness() < 128:
            path = BASE_DIR / "src/config/dark.xml"
        else:
            path = BASE_DIR / "src/config/light.xml"
        apply_stylesheet(self, theme=str(path))

# para compilar
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent

if __name__ == '__main__':
    app = App(sys.argv)

    window = MainWindow()
    window.set_icon(app.get_current_theme(), BASE_DIR)
    window.show()

    sys.exit(app.exec())
