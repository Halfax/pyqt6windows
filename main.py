
import config
import logging

import os
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit, QComboBox
import sys
from windowing import MainWindow

def play_game():
    app = QApplication(sys.argv)
    main_window = MainWindow()

    app.exec()
    logging.debug('out of move loop and print windows')

logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
logging.info('Started')
play_game()
logging.info('Finished')