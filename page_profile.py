from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
import requests
import json 


def create_profile_window(stacked_widget): # add stacked_widget to link with main.py.
    print("page_profile_window")
    #9-11 set window
    main_window = QWidget()
    main_window.setWindowTitle("Profile")
    main_window.setFixedSize(QSize(380, 570))  
    #set Horizontl or vertical 
    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)

    img = QPixmap("/IMG_0711.JPG")
    img_lb = QLabel()
    img_lb.setPixmap(img)
    img_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(img_lb)
    return main_window

    
