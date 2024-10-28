
import config
import logging
import os
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit, QComboBox
import sys
import windowing as mywin

def play_game():
    whattodo = "StartingUp"
    app ,main_win1 = mywin.create_main()
    mywin.showmain(main_win1)
    whattodo,app = mywin.pop_game_start(app,whattodo)  
      
    if whattodo == "new_game":
        logging.debug('new game')
    elif whattodo == "load_game":       
        logging.debug('load game')



    
    logging.debug('out of move loop and print windows')
    app.exec()
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
logging.info('Started')
play_game()
logging.info('Finished')