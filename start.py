import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap, QImage
from score import return_points
import subprocess


class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Главное меню')
        self.setGeometry(300, 200, 1200, 600)
        self.setFixedSize(QSize(1200, 600))

        self.pixmap = QPixmap.fromImage(QImage('images/background.png'))
        self.image = QLabel(self)
        self.image.setGeometry(0, 0, 1200, 600)
        self.image.setPixmap(self.pixmap)

        self.start_button = QPushButton('Начать', self)
        self.start_button.setGeometry(500, 510, 200, 40)
        self.start_button.setStyleSheet("QPushButton {"
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

        self.see_points = QPushButton('Посмотреть результаты', self)
        self.see_points.setGeometry(250, 510, 200, 40)
        self.see_points.setStyleSheet("QPushButton {"
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

        self.exit_button = QPushButton('Выход', self)
        self.exit_button.setGeometry(750, 510, 200, 40)
        self.exit_button.setStyleSheet("QPushButton {"
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

        self.reset_button = QPushButton('Сбросить результаты', self)
        self.reset_button.setGeometry(950, 375, 200, 40)
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
        self.reset_button.hide()

        self.clean_button = QPushButton('Скрыть результаты', self)
        self.clean_button.setGeometry(950, 325, 200, 40)
        self.clean_button.setStyleSheet("QPushButton {"
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
        self.clean_button.hide()

        best, last = return_points()
        self.best_score = QLabel(f'Лучший результат: {best}', self)
        self.best_score.setGeometry(937, 235, 263, 40)
        self.best_score.setStyleSheet("font: bold 20px; color: white;")
        self.best_score.hide()
        self.last_score = QLabel(f'Прошлый результат: {last}', self)
        self.last_score.setGeometry(937, 275, 263, 40)
        self.last_score.setStyleSheet("font: bold 20px; color: white;")
        self.last_score.hide()

        self.start_button.clicked.connect(self.runner)
        self.exit_button.clicked.connect(self.exit)
        self.see_points.clicked.connect(self.see)
        self.clean_button.clicked.connect(self.clean)
        self.reset_button.clicked.connect(self.reset)

    def runner(self):
        path = 'game.py'
        self.close()
        subprocess.call(['python', path])

    def exit(self):
        self.close()

    def see(self):
        self.clean_button.show()
        self.reset_button.show()
        self.best_score.show()
        self.last_score.show()

    def clean(self):
        self.clean_button.hide()
        self.reset_button.hide()
        self.best_score.hide()
        self.last_score.hide()

    def reset(self):
        with open('points', 'w') as f:
            f.write(f'0, 0')
        self.best_score.setText('Лучший результат: 0')
        self.last_score.setText('Прошлый результат: 0')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StartWindow()
    window.show()
    sys.exit(app.exec())
