import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QImage
from score import return_points
import subprocess


class EndWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Экран смерти')
        self.setGeometry(300, 200, 1200, 600)
        self.setFixedSize(QSize(1200, 600))

        self.pixmap = QPixmap.fromImage(QImage('images/background_2.png'))
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 1200, 600)
        self.image.setPixmap(self.pixmap)

        self.reset_button = QPushButton('Начать сначала', self)
        self.reset_button.setGeometry(640, 470, 200, 40)
        self.reset_button.setStyleSheet("QPushButton {"
                             "    background-color: #9400D3;"
                             "    color: white;"
                             "    border-radius: 10px;"
                             "    font-size: 16px;"
                             "}"
                             "QPushButton:hover {"
                             "    background-color: #8A2BE2;"
                             "}"
                             "QPushButton:pressed {"
                             "    background-color: #9932CC;"
                             "}")
        self.home_button = QPushButton('В главное меню', self)
        self.home_button.setGeometry(350, 470, 200, 40)
        self.home_button.setStyleSheet("QPushButton {"
                             "    background-color: #9400D3;"
                             "    color: white;"
                             "    border-radius: 10px;"
                             "    font-size: 16px;"
                             "}"
                             "QPushButton:hover {"
                             "    background-color: #8A2BE2;"
                             "}"
                             "QPushButton:pressed {"
                             "    background-color: #9932CC;"
                             "}")

        self.reset_button.clicked.connect(self.game)
        self.home_button.clicked.connect(self.home)

        best, last = return_points()
        self.best_score = QLabel(f'Лучший результат: {best}', self)
        self.best_score.setGeometry(350, 10, 250, 40)
        self.best_score.setStyleSheet("font: bold 20px; color: white;")
        self.last_score = QLabel(f'Ваш результат: {last}', self)
        self.last_score.setGeometry(640, 10, 250, 40)
        self.last_score.setStyleSheet("font: bold 20px; color: white;")

    def home(self):
        path = 'start.py'
        self.close()
        subprocess.call(['python', path])

    def game(self):
        path = 'game.py'
        self.close()
        subprocess.call(['python', path])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EndWindow()
    window.show()
    sys.exit(app.exec())
