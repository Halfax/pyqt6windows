from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QMessageBox, QCheckBox, QComboBox, QLineEdit, QTextEdit, QHBoxLayout, QGridLayout
import logging
import config
import sys

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
