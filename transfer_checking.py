from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import requests
import json
from login import account_signal
from login import saving_signal


def create_tf_checking_window(stacked_widget):
    sum_saving_current_balance = None 
    withdraw_amount = None
    account_number = None


    def saving_balance_home(account_number):
        nonlocal sum_saving_current_balance
        data = {"account_number": account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_saving_balance", json=data)
        resp = response.json()
        
        sum_saving_current_balance = resp['result']['sum_saving_current_balance']
        transfer_btn_2.setText(f'Saving         {"{:.2f}".format(sum_saving_current_balance)}')

    def submit_transfer_checking():
        nonlocal withdraw_amount, account_number
        transfer_amount = checking_balance_input.text()

        if not account_number:
            QMessageBox.warning(None, "Error", "No account number found. Please log in again.")
            return
        
        data = {
            "account_number": account_number,
            "withdraw_amount": int(transfer_amount)
        }
        print(data)
        try:
            response = requests.post("http://127.0.0.1:8998/insert_data_withdraw", json=data)
            resp = response.json()
            print(resp)
            
            if resp.get("status") == "OK":
                QMessageBox.information(None, "Success", "Withdraw successful")
                checking_balance_input.setText("") 
            else:
                QMessageBox.warning(None, "Failed", "Withdraw failed")
        except requests.RequestException:
            QMessageBox.warning(None, "Error", "Failed to connect to the server")
    
    def submit_transfer_checking():
        stacked_widget.setCurrentWidget(stacked_widget.widget(7))
    

    def store_account_number(acc_num):
        nonlocal account_number
        account_number = acc_num

    account_signal.account_success.connect(store_account_number)


    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    saving_signal.saving_success.connect(saving_balance_home)

    transfer_from_lb = QLabel('Transfer From')
    transfer_from_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    transfer_from_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(transfer_from_lb)

    checking_lb = QLabel('Checking')
    checking_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    checking_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(checking_lb)

    transfer_from_group = QGroupBox('Transfer Amount')
    transfer_from_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    transfer_from_layout = QVBoxLayout()
    # checking_balance = QLabel("$ 0.00")
    checking_balance_input = QLineEdit()
    checking_balance_input.setPlaceholderText("$")
    # checking_balance.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
    # transfer_from_layout.addWidget(checking_balance)
    transfer_from_layout.addWidget(checking_balance_input)
    transfer_from_group.setLayout(transfer_from_layout)
    main_layout.addWidget(transfer_from_group)

    transfer_to_lb = QLabel('Transfer To')
    transfer_to_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    transfer_to_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(transfer_to_lb)

    saving_lb = QLabel('Saving')
    saving_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    saving_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(saving_lb)

    transfer_btn_2 = QPushButton("Saving            500,000.00$")
    main_layout.addWidget(transfer_btn_2)
    # main_layout.addWidget(transfer_btn_2, alignment=Qt.AlignmentFlag.AlignLeft)
    # transfer_btn_2.setFixedWidth(150)
    # # main_layout.addSpacerItem(QSpacerItem(100,100, QSizePolicy.Policy.Expanding))


    transfer_btn = QPushButton('Transfer')
    transfer_btn.setFixedWidth(100)
    transfer_btn_2.clicked.connect(submit_transfer_checking)
    main_layout.addWidget(transfer_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))

    main_layout.addStretch()
    btn_layout = QHBoxLayout()
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignBottom)  #*********
    home_btn = QPushButton('Home')
    home_btn.setFixedWidth(60)
    home_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    btn_layout.addWidget(home_btn, alignment=Qt.AlignmentFlag.AlignCenter)  #*********

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(6)))
    btn_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight) #*********
    main_layout.addLayout(btn_layout) #*********


    return main_window
