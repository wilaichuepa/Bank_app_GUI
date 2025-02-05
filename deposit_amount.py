
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from login import account_signal
import requests
import json

   

def create_deposit_window(stacked_widget):
    deposit_amount = None
    account_number = None
    def submit_deposit():
        nonlocal deposit_amount,account_number
        deposit_amount = checking_balance_input.text()
       
        data = {"account_number":account_number,
                "deposit_amount":deposit_amount}
        response = requests.post("http://127.0.0.1:8998/insert_data_deposit",json=data)
        resp = response.json()
        if resp["status"] == "OK":
            QMessageBox.information(None,"Warning","deposit success") 
        else:
            QMessageBox.information(None,"Warning","deposit fail")

    def store_account_number(acc_num):
        nonlocal account_number
        account_number = acc_num

    # Connect the account signal to store the account number
    account_signal.account_success.connect(store_account_number)

    # Main window setup
    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    # account_signal.account_success.connect(submit_deposit)

    # Main layout
    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    main_window.setLayout(main_layout)

    # Deposit Group Box
    deposit_group = QGroupBox('Deposit Amount')
    deposit_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    deposit_layout = QVBoxLayout()
    # checking_balance = QLabel("$ 0.00")
    checking_balance_input = QLineEdit()
    checking_balance_input.setPlaceholderText("$")
    # checking_balance.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
    # deposit_layout.addWidget(checking_balance)
    deposit_layout.addWidget(checking_balance_input)
    deposit_group.setLayout(deposit_layout)
    main_layout.addWidget(deposit_group)

    # Header layout with a deposit button
    deposit_btn = QPushButton('Deposit')
    deposit_btn.setFixedWidth(100)
    deposit_btn.clicked.connect(submit_deposit)
    main_layout.addWidget(deposit_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    # main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    # Back button to navigate home
    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)
    

    

    return main_window
