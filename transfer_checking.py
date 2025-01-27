from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_tf_checking_window(stacked_widget):

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

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
    main_layout.addWidget(transfer_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))

    home_btn = QPushButton('Home')
    home_btn.setFixedWidth(60)
    home_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(home_btn, alignment=Qt.AlignmentFlag.AlignRight)

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(6)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)


    return main_window
