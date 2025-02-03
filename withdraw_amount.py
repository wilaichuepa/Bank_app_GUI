from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from login import account_signal
import requests
import json

def create_withdraw_window(stacked_widget):
    withdraw_saving_amount = ""
    account_number = None

    def store_account_number(acc_num):
        nonlocal account_number
        account_number = acc_num

    account_signal.account_success.connect(store_account_number)

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    if main_window.layout() is None:
        main_layout = QVBoxLayout()
        main_window.setLayout(main_layout) 
    else:
        main_layout = main_window.layout()

    withdraw_group = QGroupBox('Withdraw Amount')
    withdraw_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    withdraw_layout = QVBoxLayout()

    checking_balance_input = QLineEdit()  
    checking_balance_input.setPlaceholderText("$")
    withdraw_layout.addWidget(checking_balance_input)

    withdraw_group.setLayout(withdraw_layout)
    main_layout.addWidget(withdraw_group)

    def submit_withdraw():
        nonlocal withdraw_saving_amount, account_number
        withdraw_saving_amount = checking_balance_input.text()

        if not account_number:
            QMessageBox.warning(None, "Error", "No account number found. Please log in again.")
            return
        
        data = {
            "account_number": account_number,
            "withdraw_saving_amount": withdraw_saving_amount
        }

        try:
            response = requests.post("http://127.0.0.1:8998/insert_data_saving_withdraw", json=data)
            resp = response.json()
            
            if resp.get("status") == "OK":
                QMessageBox.information(None, "Success", "Withdraw successful")
                checking_balance_input.setText("") 
            else:
                QMessageBox.warning(None, "Failed", "Withdraw failed")
        except requests.RequestException:
            QMessageBox.warning(None, "Error", "Failed to connect to the server")

    withdraw_btn = QPushButton('Withdraw')
    withdraw_btn.setFixedWidth(100)
    withdraw_btn.clicked.connect(submit_withdraw)
    main_layout.addWidget(withdraw_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)
    
    return main_window
