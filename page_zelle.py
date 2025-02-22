from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# from login import login_signal
from login import account_signal
import requests
import json

def create_zelle_window(stacked_widget):

    def send_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(10))
    def request_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(11))
    def contact_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(12))

    def favorite_account_number(account_number):
        data = {"account_number":account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_favorite_account",json=data)
        resp = response.json()

        favorite_account_1 = resp['message'][0]['account_number']
        favorite_account_2 = resp['message'][1]['account_number']
        favorite_account_3 = resp['message'][2]['account_number']
        
        name_account_1 = resp['message'][0]['firstname']+"  "+resp['message'][0]['lastname']
        phone_account_1 = resp['message'][0]['phone_number']
        email_account_1 = resp['message'][0]['email']
        recippient_1_btn.setText(f'{name_account_1}\n{phone_account_1}\n{email_account_1}')

        name_account_2 =resp['message'][1]['firstname']+"  "+resp['message'][1]['lastname']
        phone_account_2= resp['message'][1]['phone_number']
        email_account_2=resp['message'][1]['email']
        recippient_2_btn.setText(f'{name_account_2}\n{phone_account_2}\n{email_account_2}')

        name_account_3 =resp['message'][2]['firstname']+"  "+resp['message'][2]['lastname']
        phone_account_3= resp['message'][2]['phone_number']
        email_account_3=resp['message'][2]['email']
        recippient_3_btn.setText(f'{name_account_3}\n{phone_account_3}\n{email_account_3}')
    
    account_signal.account_success.connect(favorite_account_number)

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 540))

    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)
    btn_layout = QHBoxLayout(main_window)

    send_btn = QPushButton("Send")
    send_btn.clicked.connect(send_submit)
    send_btn.setFixedSize(QSize(100,60))
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(send_btn)

    request_btn = QPushButton("Request")
    request_btn.clicked.connect(request_submit)
    request_btn.setFixedSize(QSize(100,60))
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(request_btn)
    main_layout.addLayout(btn_layout) # put send and request to main_layout 
    # buil 2 layout in same window // เอา วัตถุในแนวนอน send  request ใส่ใน QVBoxLayout
    contact_btn = QPushButton('+ New Contact')
    contact_btn.clicked.connect(contact_submit)
    contact_btn.setFixedWidth(100)
    main_layout.addWidget(contact_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))

    recippients_lb = QLabel('Recippients')
    recippients_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    recippients_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(recippients_lb)

    recippient_1_btn = QPushButton("Wilai Chuepa\n9733174164")
    recippient_1_btn.setFixedWidth(200)
    main_layout.addWidget(recippient_1_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    # main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(recippient_1_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    recippient_2_btn = QPushButton(" Mak Maxx\n1023456789")
    recippient_2_btn.setFixedWidth(200)
    main_layout.addWidget(recippient_2_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    # main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(recippient_2_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    recippient_3_btn = QPushButton(" Wilson Mc \n1234567890")
    recippient_3_btn.setFixedWidth(200)
    main_layout.addWidget(recippient_2_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    # main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(recippient_3_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)

    return main_window