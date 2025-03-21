from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# from signin import *
import requests
import json
# from login import login_signal
from login import account_signal
from login import saving_signal

def create_home_window(stacked_widget):
    sum_current_balance = None
    sum_saving_current_balance = None 
    
    def checking_balance_home(account_number):
        nonlocal  sum_current_balance

        data = {"account_number":account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_cash_balance",json=data)
        resp = response.json()
        sum_current_balance =resp['result']['sum_current_balance']
        checking_balance_lb.setText(f'{"{:.2f}".format(sum_current_balance)}\n Available Balance')

    def saving_balance_home(account_number):
        nonlocal sum_saving_current_balance

        data = {"account_number": account_number}
        response = requests.post("http://127.0.0.1:8998/select_data_saving_balance", json=data)
        resp = response.json()
        
        sum_saving_current_balance = resp['result']['sum_saving_current_balance']
        saving_balance_lb.setText(f'{"{:.2f}".format(sum_saving_current_balance)}\n Saving Balance')
        

    def submit_logout():
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Log Out")
        msg_box.setText("Are you sure you want to log out?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.No|QMessageBox.StandardButton.Yes)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Yes)
        # test = QMessageBox.critical(self,"แจ้งเตือน","test",QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes)
        response = msg_box.exec()
        if response == QMessageBox.StandardButton.Yes:
            stacked_widget.setCurrentWidget(stacked_widget.widget(0))
        else:
            stacked_widget.setCurrentWidget(stacked_widget.widget(2))
    def submit_profile():
        print("submit_profile")
        stacked_widget.setCurrentWidget(stacked_widget.widget(3))

    def submit_deposit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(4))

    def submit_withdraw():
        stacked_widget.setCurrentWidget(stacked_widget.widget(5))

    def submit_transfer():
        stacked_widget.setCurrentWidget(stacked_widget.widget(6))
    
    def submit_zelle():
        stacked_widget.setCurrentWidget(stacked_widget.widget(9))



    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)

    account_signal.account_success.connect(checking_balance_home)

    saving_signal.saving_success.connect(saving_balance_home)

    header_layout = QHBoxLayout()
    header_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    profile_btn = QPushButton('Profile')
    # profile_btn.setFixedSize(80,30)
    header_layout.addWidget(profile_btn)
    profile_btn.clicked.connect(submit_profile)
    header_layout.addSpacerItem(QSpacerItem(20,20,QSizePolicy.Policy.Expanding))

    santander_lb = QLabel('Santander Bank')
    santander_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    # santander_lb.setStyleSheet('font-size:30px; font-weight:bold;text-align:center')
    header_layout.addWidget(santander_lb)
    header_layout.addSpacerItem(QSpacerItem(20,20,QSizePolicy.Policy.Expanding))

    logout_btn = QPushButton('Log out')
    logout_btn.clicked.connect(submit_logout)
    header_layout.addWidget(logout_btn)
    main_layout.addLayout(header_layout)


    checking_group = QGroupBox('Checking')
    checking_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    checking_layout = QVBoxLayout()
    checking_balance_lb = QLabel(sum_current_balance)
    checking_balance_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    checking_layout.addWidget(checking_balance_lb)
    checking_group.setLayout(checking_layout)
    main_layout.addWidget(checking_group)

    saving_group = QGroupBox('Saving')
    saving_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    saving_layout = QVBoxLayout()
    saving_balance_lb = QLabel(sum_saving_current_balance) #********put sum_current_balance for saving
    saving_balance_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    saving_layout.addWidget(saving_balance_lb)
    saving_group.setLayout(saving_layout)
    main_layout.addWidget(saving_group)

    btn_layout = QVBoxLayout()
    # for text in ["Deposit","Transfer","Withdraw","Zelle"]:
        # btn = QPushButton(text)
        # btn.setFixedSize(QSize(100,60))
        # btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # btn_layout.addWidget(btn)                                # ***** for we can use when we need to run samething
    
    deposit_btn = QPushButton("Deposit")
    deposit_btn.setFixedSize(QSize(100,60))
    deposit_btn.clicked.connect(submit_deposit)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(deposit_btn)

    transfer_btn = QPushButton("Transfer")
    transfer_btn.setFixedSize(QSize(100,60))
    transfer_btn.clicked.connect(submit_transfer)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(transfer_btn)

    withdraw_btn = QPushButton("Withdraw")
    withdraw_btn.setFixedSize(QSize(100,60))
    withdraw_btn.clicked.connect(submit_withdraw)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(withdraw_btn)

    zelle_btn = QPushButton("Zelle")
    zelle_btn.setFixedSize(QSize(100,60))
    zelle_btn.clicked.connect(submit_zelle)
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(zelle_btn)

    main_layout.addLayout(btn_layout)
    return main_window
