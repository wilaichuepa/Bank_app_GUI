from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from login import account_signal
import requests
import json

def create_send_window(stacked_widget):
    account_number = None  # Store account number

    def send_submit(acc_num=None):
        nonlocal account_number
        if acc_num is not None:
            account_number = acc_num  # Set account number when signal emits

        if account_number is None:
            print("Error: Account number is not set.")
            return  # Prevent sending request if account number is missing

        email_phone = email_phone_input.text()
        zelle_amount = zelle_amount_input.text()

        if not email_phone or not zelle_amount:
            print("Error: Email/Phone or Amount is missing.")
            return  # Prevent sending empty data


        data = {
            "phone_email": email_phone,
            "my_account_number": account_number,
            "zelle_amount": int(zelle_amount),
        }

        response = requests.post("http://127.0.0.1:8998/recippient_zelle", json=data)
        resp = response.json()
        print("Response:", resp)

        if resp["status"] == "OK":
            QMessageBox.information(None,"Warning","zelle success")
        else :
            QMessageBox.warning(None,"Warning","zelle  fail")

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    main_window.setLayout(main_layout)

    send_to_lb = QLabel('Send To ')
    send_to_lb.setStyleSheet('font-size:15px; font-weight:bold')
    main_layout.addWidget(send_to_lb, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20,30,QSizePolicy.Policy.Expanding))

    email_phone_lb = QLabel('Email/Phone')
    main_layout.addWidget(email_phone_lb)
    email_phone_input = QLineEdit()
    main_layout.addWidget(email_phone_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))

    # Connect account success signal to update account number
    account_signal.account_success.connect(lambda acc_num: send_submit(acc_num))     

    zelle_amount_lb = QLabel('Zelle Amount')
    main_layout.addWidget(zelle_amount_lb)
    zelle_amount_input = QLineEdit()
    main_layout.addWidget(zelle_amount_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))

    send_btn = QPushButton('Send')
    send_btn.setFixedWidth(100)
    send_btn.clicked.connect(lambda: send_submit())  # Calls send_submit without acc_num
    main_layout.addWidget(send_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    main_layout.addStretch()

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(9)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)

    return main_window
