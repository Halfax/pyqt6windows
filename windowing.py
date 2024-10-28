from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QMessageBox, QCheckBox, QComboBox, QLineEdit, QTextEdit, QHBoxLayout, QGridLayout
from PyQt6.QtCore import Qt
import logging
import config
import sys
import functions as myfun

logger = logging.getLogger(__name__)

def newgame(sub1, allitems, app1):
    loopit = True
    tracked_monsters = []
    tile_in_front = ''

    name_label = QLabel("Enter character name:")
    name_input = QLineEdit()
    
    vocation_label = QLabel("Enter character vocation (a, b):")
    vocation_input = QComboBox()
    vocation_input.addItems(["a", "b"])
    
    race_label = QLabel("Enter character race (1, 2):")
    race_input = QComboBox()
    race_input.addItems(["1", "2"])
    
    start_button = QPushButton("roll")
    
    layout = QVBoxLayout()
    layout.addWidget(name_label)
    layout.addWidget(name_input)
    layout.addWidget(vocation_label)
    layout.addWidget(vocation_input)
    layout.addWidget(race_label)
    layout.addWidget(race_input)
    layout.addWidget(start_button)
    
    container = QWidget()
    container.setLayout(layout)
    sub1.setCentralWidget(container)
    start_button.clicked.connect(lambda: setattr(sub1, 'whattodo', 'roll'))
    sub1.show() 


    while sub1.whattodo != "roll":
        app1.processEvents()

    name = name_input.text()
    vocation = vocation_input.currentText()
    race = race_input.currentText()

    my_character = Character(name, race, vocation,sub1,app1)
    my_character.initial_inventory(allitems)
    sub1.accepted(app1,my_character)

        
    
    loopit = False
    level = 0
    dungeon = town.towngen()
    dungeon,my_character= place_player(dungeon,my_character,level)
    new_game = True
    sub1.clear_central_widget()
    return dungeon, level,  my_character,  tile_in_front , tracked_monsters,loopit,new_game,sub1,app1

        
def create_main():
    def close_all_windows():
        for widget in QApplication.topLevelWidgets():
            widget.close()
        sys.exit()    

    app1 = QApplication(sys.argv)   
    main_window = QMainWindow()
    main_window.setWindowTitle("My Game")
    main_window.setGeometry(100, 100, 600, 400)
    main_window.layout = QVBoxLayout()
    main_window.label = QLabel("Welcome to the game!", main_window)
    main_window.layout.addWidget(main_window.label)

    close_button = QPushButton("Close All Windows", main_window)
    close_button.clicked.connect(close_all_windows)
    main_window.layout.addWidget(close_button)
    return app1 ,main_window

def showmain(mw):
    mw.show()

def pop_game_start(app,whattodo):
    sub1 = QMainWindow()
    sub1.setWindowTitle('New Game Window')
    sub1.setGeometry(120, 120, 200, 200)
    sub1.layout = QVBoxLayout()
    sub1.whattodo = 'nothing'
    logging.debug(f"whattodo = {sub1.whattodo}")
    sub1.central_widget = QWidget()
    sub1.central_widget.setLayout(sub1.layout)
    sub1.setCentralWidget(sub1.central_widget)
    sub1.label = QLabel("Welcome to the game!", sub1.central_widget)
    sub1.layout.addWidget(sub1.label)
    new_game_button = QPushButton("New Game", sub1)
    new_game_button.clicked.connect(lambda: setattr(sub1, 'whattodo', 'new_game'))
    sub1.layout.addWidget(new_game_button)

    load_game_button = QPushButton("Load Game", sub1)
    load_game_button.clicked.connect(lambda: setattr(sub1, 'whattodo', 'load_game'))
    sub1.layout.addWidget(load_game_button)
    show_sub1_window(sub1)
    while sub1.whattodo not in ['new_game' ,'load_game']:  
        app.processEvents()
    logging.debug('new game or load game got')
    whattodo = sub1.whattodo
    logging.debug(f'whattodo = {whattodo}')
    sub1.close()
    return whattodo,app
    
def pop_char_create(app,whattodo):
    sub1 = QMainWindow()
    sub1.setWindowTitle('create char Window')
    sub1.setGeometry(120, 120, 200, 200)
    sub1.layout = QVBoxLayout()
    sub1.whattodo = 'nothing'
    myvalue = myfun.roll_dice(20 ,4)
    logging.debug(f"whattodo = {sub1.whattodo}")
    sub1.central_widget = QWidget()
    sub1.central_widget.setLayout(sub1.layout)
    sub1.setCentralWidget(sub1.central_widget)
    sub1.label = QLabel("your character", sub1.central_widget)
    sub1.layout.addWidget(sub1.label)
    sub1.label = QLabel(f"your value is {myvalue}", sub1.central_widget)    
    sub1.layout.addWidget(sub1.label)
    accept_button = QPushButton("accept", sub1)
    accept_button.clicked.connect(lambda: setattr(sub1, 'whattodo', 'created'))
    sub1.layout.addWidget(accept_button)

    reroll_button = QPushButton("reroll", sub1)
    reroll_button.clicked.connect(lambda: sub1.label.setText(f"your value is {myfun.roll_dice(20, 4)}"))  
    sub1.layout.addWidget(reroll_button)
    show_sub1_window(sub1)
    while sub1.whattodo not in ['created']:  
        app.processEvents()
    logging.debug('got accpted or reroll get')
    whattodo = sub1.whattodo
    logging.debug(f'whattodo = {whattodo}')
    sub1.close()
    return whattodo,app    

def update_myvalue(myvalue):
    myvalue = myfun.roll_dice(20, 4)
    return myvalue
    
def pop_load_game(app,whattodo):
    sub1 = QMainWindow()
    sub1.setWindowTitle('load Game Window')
    sub1.setGeometry(120, 120, 200, 200)
    sub1.layout = QVBoxLayout()
    sub1.whattodo = 'loading'
    logging.debug(f"whattodo = {sub1.whattodo}")
    sub1.central_widget = QWidget()
    sub1.central_widget.setLayout(sub1.layout)
    sub1.setCentralWidget(sub1.central_widget)
    sub1.label = QLabel("loading game", sub1.central_widget)
    sub1.layout.addWidget(sub1.label)
    file_dialog = QFileDialog(sub1)
    file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    file_dialog.setNameFilter("Game Files (*.game)")
    if file_dialog.exec():
        selected_file = file_dialog.selectedFiles()[0]
        sub1.label.setText(f"Selected file: {selected_file}")
        sub1.whattodo = 'loaded'
    else:
        sub1.label.setText("No file selected")
        sub1.whattodo = 'nothing'

    show_sub1_window(sub1)
    while sub1.whattodo not in ['loaded','nothing']:  
        app.processEvents()
    logging.debug('loaded got processed')
    whattodo = sub1.whattodo
    logging.debug(f'whattodo = {whattodo}')
    sub1.close()
    return whattodo,app

def pop_dungeon(app,whattodo):  
    sub2 = QMainWindow()
    sub2.setWindowTitle('dungeon Window')
    sub2.setGeometry(120, 120, 200, 200)
    sub2.layout = QVBoxLayout()
    sub2.whattodo = 'dungeon'
    logging.debug(f"whattodo = {sub2.whattodo}")
    sub2.central_widget = QWidget()
    sub2.central_widget.setLayout(sub2.layout)
    sub2.setCentralWidget(sub2.central_widget)
    sub2.label = QLabel("dungeon will be displayed here", sub2.central_widget)
    sub2.layout.addWidget(sub2.label)
    sub2.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
    sub2.closeEvent = lambda event: setattr(sub2, 'whattodo', 'exit')
    show_sub1_window(sub2)
    while sub2.whattodo not in ['exit']:  
        app.processEvents()
    logging.debug('dungeon exited')
    print (f"dungeon exited")
    print (f"whattodo = {sub2.whattodo}")
    whattodo = sub2.whattodo
    logging.debug(f'whattodo = {whattodo}')
    sub2.close()
    return whattodo,app

def create_sub1_window():
    sub1 = QApplication.instance()
    new_window = QMainWindow()
    new_window.setWindowTitle('New Window')
    new_window.setGeometry(120, 120, 200, 200)

    label = QLabel('This is a new window', new_window)
    label.move(50, 50)
    return sub1 ,new_window

def show_sub1_window(sub1):
    sub1.show()
