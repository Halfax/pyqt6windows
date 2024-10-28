
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
        whattodo,app = mywin.pop_char_create(app,whattodo)
    elif whattodo == "load_game":       
        logging.debug('load game')
        whattodo,app = mywin.pop_load_game(app,whattodo)
    print (f"whattodo = {whattodo}")
    if whattodo in ["created","loaded"]:
        whattodo,app = mywin.pop_dungeon(app,whattodo)
    else:
        logging.debug('nothing')    
    print (f"whattodo = {whattodo}")
    logging.debug(f'whattodo should be exit = {whattodo}')
    logging.debug('out of move loop and print windows')
    app.exec()
    logging.debug('app.exec_() done')
logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
logging.info('Started')
play_game()
logging.info('Finished')