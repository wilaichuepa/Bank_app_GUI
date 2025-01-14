from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_withdraw_window(stacked_widget):

    # Main window setup
    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    # Main layout
    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    # Deposit Group Box
    withdraw_group = QGroupBox('Withdraw Amount')
    withdraw_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    withdraw_layout = QVBoxLayout()
    # checking_balance = QLabel("$ 0.00")
    checking_balance_input = QLineEdit()
    checking_balance_input.setPlaceholderText("$")
    # checking_balance.setAlignment(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
    # withdraw_layout.addWidget(checking_balance)
    withdraw_layout.addWidget(checking_balance_input)
    withdraw_group.setLayout(withdraw_layout)
    main_layout.addWidget(withdraw_group)

    # Header layout with a deposit button
    withdraw_btn = QPushButton('Withdraw')
    withdraw_btn.setFixedWidth(100)
    main_layout.addWidget(withdraw_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))

    # Back button to navigate home
    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)

    return main_window