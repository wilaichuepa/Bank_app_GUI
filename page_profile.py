from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap,QPainter,QBrush
import requests
import json 
from login import login_signal


def create_profile_window(stacked_widget): # add stacked_widget to link with main.py.
    email = None
    phone = None
    address = None
    name = None
    def user_info(username,password):
        nonlocal email
        nonlocal phone
        nonlocal address
        nonlocal name
        data = {"username":username,"password":password}
        response = requests.post("http://127.0.0.1:8998/check_login",json=data)
        resp = response.json()
        
        if resp['status']== 'OK':
                
            name = resp['data'][0]['firstname']+" " + resp['data'][0]['lastname']
            name_lb.setText(f"{name}")
            email =resp['data'][0]['email']
            phone = resp['data'][0]['phone_number']
            address =resp['data'][0]['address']
            
    def show_email_info():
        QMessageBox.information(None,"information",email)
    def show_phone_info():
        QMessageBox.information(None,"information",phone)
    def show_address_info():
        QMessageBox.information(None,"information",address)

    def back_to_home():
        stacked_widget.setCurrentWidget(stacked_widget.widget(2))
    #9-11 set window
      

    main_window = QWidget()
    main_window.setWindowTitle("Profile")
    main_window.setFixedSize(QSize(380, 570))  
    #set Horizontl or vertical 
    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)

    login_signal.login_success.connect(user_info)


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
    name_lb = QLabel(name)
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
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(back_btn,alignment= Qt.AlignmentFlag.AlignRight)

    return main_window

    
