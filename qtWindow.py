import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Titaleh")
        self.setGeometry(700, 300, 100, 100)
        self.setWindowIcon(QIcon("path"))
        self.setWindowIconText("mewo")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
