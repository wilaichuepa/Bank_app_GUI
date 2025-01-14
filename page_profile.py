from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QPainter,QBrush
import requests
import json 

def create_profile_window(stacked_widget): # add stacked_widget to link with main.py.
    def show_email_info():
        QMessageBox.information(None,"information","well@gmail.com")
    def show_phone_info():
        QMessageBox.information(None,"information","9733174164")
    def show_address_info():
        QMessageBox.information(None,"information","40 standley rd nj 07079")

    def back_to_home():
        stacked_widget.setCurrentWidget(stacked_widget.widget(2))
    #9-11 set window
    main_window = QWidget()
    main_window.setWindowTitle("Profile")
    main_window.setFixedSize(QSize(380, 570))  
    #set Horizontl or vertical 
    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)

    img_lb = QLabel()
    img = QPixmap("./DSC_0020.JPG")
    if not img.isNull():
        desired_width = 150
        desired_height = 150
        # Scale the QPixmap
        scaled_pixmap = img.scaled(desired_width, desired_height, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        circle_pixmap = QPixmap(150,150)
        circle_pixmap.fill(Qt.GlobalColor.transparent) #set background to be clear
        painter = QPainter(circle_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(scaled_pixmap))
        painter.drawEllipse(0,0,150,150)
        # offset_x = (scaled_pixmap.width() - desired_width) // 2
        # offset_y = (scaled_pixmap.height() - desired_height) // 2
        # painter.drawPixmap(-offset_x, -offset_y, scaled_pixmap)

        painter.end()
        # Set the scaled QPixmap to the QLabel
        img_lb.setPixmap(circle_pixmap)
        
    else:
        img_lb.setText('image not found')
    img_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(img_lb)

    name_lb = QLabel('Wilai Chuepa')
    name_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    # name_lb.setStyleSheet('font-size:30px; font-weight:bold;text-align:center')
    name_lb.setStyleSheet('font-size:15px; font-weight:bold;text-align:center')
    main_layout.addWidget(name_lb)

    email_btn = QPushButton('Email')
    # email_btn.setFixedSize(80,30)
    email_btn.clicked.connect(show_email_info)
    main_layout.addWidget(email_btn)
    

    phone_btn = QPushButton('Phone')
    # phone_btn.setFixedSize(80,30)
    phone_btn.clicked.connect(show_phone_info)
    main_layout.addWidget(phone_btn)

    address_btn = QPushButton('Address')
    # address_btn.setFixedSize(80,30)
    address_btn.clicked.connect(show_address_info)
    main_layout.addWidget(address_btn)

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(back_to_home)
    main_layout.addWidget(back_btn,alignment= Qt.AlignmentFlag.AlignRight)

    return main_window

    
