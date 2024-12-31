from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import requests
import json

def create_signin_window(stacked_widget):
    def back_to_login():
        stacked_widget.setCurrentWidget(stacked_widget.widget(0))
    def signin():
        firstname =firstname_input.text()
        lastname= lastname_input.text()
        email = email_input.text()
        username = username_input.text()
        password = password_input.text()
        phone = phone_input.text()
        address =address_input.text()
       

        data = {
                "firstname":firstname,
                "lastname":lastname,
                "email":email,
                "username":username,
                "password":password,
                "phone_number":phone,
                "address":address
                }
        
        response = requests.post("http://127.0.0.1:8998/signin_data",json=data)
        resp = response.json()
        
        if resp["status"] == "OK":
            QMessageBox.information(None,"Warning","sign in success")
            
            # print(response)
        else:
            QMessageBox.information(None,"Warning","sign in fail")
            

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))
    #Set layout to be in center
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_window.setLayout(main_layout)
    #QLalet to put text and set it in the center
    signin_lb = QLabel('Sign in')
    signin_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
    signin_lb.setStyleSheet('font-size:30px; font-weight:bold;text-align:center')
    main_layout.addWidget(signin_lb)

    firstname_lb = QLabel('Frist name')
    firstname_input = QLineEdit()
    main_layout.addWidget(firstname_lb)
    main_layout.addWidget(firstname_input)

    lastname_lb = QLabel('Last name')
    lastname_input = QLineEdit()
    main_layout.addWidget(lastname_lb)
    main_layout.addWidget(lastname_input)

    email_lb = QLabel('Email')
    email_input = QLineEdit()
    main_layout.addWidget(email_lb)
    main_layout.addWidget(email_input)

    username_lb = QLabel('User name')
    username_input = QLineEdit()
    main_layout.addWidget(username_lb)
    main_layout.addWidget(username_input)

    password_lb = QLabel('Create password')
    password_input = QLineEdit()
    main_layout.addWidget(password_lb)
    main_layout.addWidget(password_input)

    phone_lb = QLabel('Phone number')
    phone_input = QLineEdit()
    main_layout.addWidget(phone_lb)
    main_layout.addWidget(phone_input)

    address_lb = QLabel('Address')
    address_input = QLineEdit()
    main_layout.addWidget(address_lb)
    main_layout.addWidget(address_input)

    signin_btn = QPushButton('Sign in')
    signin_btn.setFixedWidth(60)
    signin_btn.clicked.connect(signin)
    main_layout.addWidget(signin_btn,alignment= Qt.AlignmentFlag.AlignCenter)

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(back_to_login)
    main_layout.addWidget(back_btn,alignment= Qt.AlignmentFlag.AlignCenter)
    return main_window
    