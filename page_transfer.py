from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import requests
import json
# from login import login_signal
from login import account_signal
from login import saving_signal

def create_transfer_window(stacked_widget):
    sum_current_balance = None
    sum_saving_current_balance = None 

    def checking_balance_home(account_number):
        nonlocal  sum_current_balance

        data = {"account_number":account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_cash_balance",json=data)
        resp = response.json()
        sum_current_balance =resp['result']['sum_current_balance']
        print(sum_current_balance)
        transfer_btn_1.setText(f'Chicking       {"{:.2f}".format(sum_current_balance)}')
    
    def saving_balance_home(account_number):
        nonlocal sum_saving_current_balance

        data = {"account_number": account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_saving_balance", json=data)
        resp = response.json()
        
        sum_saving_current_balance = resp['result']['sum_saving_current_balance']
        transfer_btn_2.setText(f'Saving         {"{:.2f}".format(sum_saving_current_balance)}')


    def submit_transfer_checking():
        stacked_widget.setCurrentWidget(stacked_widget.widget(7))

    def submit_transfer_saving():
        stacked_widget.setCurrentWidget(stacked_widget.widget(8))


    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    account_signal.account_success.connect(checking_balance_home)
    saving_signal.saving_success.connect(saving_balance_home)


    transfer_lb = QLabel('Make a Transfer')
    transfer_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    transfer_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(transfer_lb)

    transfer_group = QGroupBox('Transfer from')
    transfer_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    transfer_layout = QVBoxLayout()
    transfer_group.setLayout(transfer_layout)
    transfer_btn_1 = QPushButton(sum_current_balance)
    
    transfer_btn_2 = QPushButton(sum_saving_current_balance)
    transfer_btn_1.clicked.connect(submit_transfer_checking)
    transfer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    transfer_layout.addWidget(transfer_btn_1)
    transfer_btn_2.clicked.connect(submit_transfer_saving)
    # transfer_layout.addWidget(transfer_btn_1)
    transfer_layout.addWidget(transfer_btn_2)
    main_layout.addWidget(transfer_group)
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    
    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)







    return main_window