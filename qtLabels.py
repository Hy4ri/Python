import sys

from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Titaleh")
        self.setGeometry(700, 300, 100, 100)
        self.setWindowIcon(QIcon("path"))
        self.setWindowIconText("mewo")
        self.setStyleSheet("background: #121212;color: #e2e2e2;")

        label = QLabel("Hello", self)
        label.setFont((QFont("JetBrainsMono Nerd Font", 50)))
        label.setGeometry(100, 100, 200, 100)
        label.setStyleSheet("background: #990000;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
