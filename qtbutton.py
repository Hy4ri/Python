import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Titaleh")
        self.setGeometry(700, 300, 100, 100)
        self.initUI()

    def initUI(self):
        button = QPushButton("click me!", self)
        button.setGeometry(100, 120, 200, 100)
        button.setStyleSheet("font-size: 30px;")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
