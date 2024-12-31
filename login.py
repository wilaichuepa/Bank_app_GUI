from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# from signin import *
import requests
import json

def create_login_window(stacked_widget):
    def submit():
        username = username_input.text()
        password = password_input.text()
        
        data = {"username":username,"password":password}
        response = requests.post("http://127.0.0.1:8998/check_login",json=data)
        resp = response.json()
        
        if resp["status"] == "OK":
            QMessageBox.information(None,"Warning","log in success")
            stacked_widget.setCurrentWidget(stacked_widget.widget(2))
            
            # print(response)
        else:
            QMessageBox.information(None,"Warning","log in fail")
            

    def goto_signin():
        stacked_widget.setCurrentWidget(stacked_widget.widget(1))

    # open window
    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))
    #Set layout to be in center
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_window.setLayout(main_layout)
    #QLalet to put text and set it in the center
    login_lb = QLabel('Log in')
    login_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)
    login_lb.setStyleSheet('font-size:30px; font-weight:bold;text-align:center')
    main_layout.addWidget(login_lb)
    #create the username text and be able to input the text
    username_lb = QLabel('Username')
    username_input = QLineEdit()
    main_layout.addWidget(username_lb)
    main_layout.addWidget(username_input)

    password_lb = QLabel('Password')
    password_input = QLineEdit()
    password_input.setEchoMode(QLineEdit.EchoMode.Password)
    main_layout.addWidget(password_lb)
    main_layout.addWidget(password_input)
    # create submit button
    login_btn = QPushButton('Login')
    login_btn.setFixedSize(80,30)
    login_btn.clicked.connect(submit)
    main_layout.addWidget(login_btn,alignment= Qt.AlignmentFlag.AlignCenter)
    #Sing in 
    signin_btn = QPushButton('Sign in')
    signin_btn.setFixedSize(80,30)
    signin_btn.clicked.connect(goto_signin)
    main_layout.addWidget(signin_btn,alignment= Qt.AlignmentFlag.AlignCenter)
    return main_window
    