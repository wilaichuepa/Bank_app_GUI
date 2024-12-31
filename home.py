from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
# from signin import *
import requests
import json

def create_home_window(stacked_widget):
    def submit_profile():
        print("submit_profile")
        stacked_widget.setCurrentWidget(stacked_widget.widget(3))
    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)

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
    header_layout.addWidget(logout_btn)
    main_layout.addLayout(header_layout)

    checking_group = QGroupBox('Checking')
    checking_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    checking_layout = QVBoxLayout()
    checking_balance = QLabel("0.00 \n Available Balance")
    checking_balance.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    checking_layout.addWidget(checking_balance)
    checking_group.setLayout(checking_layout)
    main_layout.addWidget(checking_group)

    saving_group = QGroupBox('Saving')
    saving_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    saving_layout = QVBoxLayout()
    saving_balance = QLabel("0.00 \n Available Balance")
    saving_balance.setAlignment(Qt.AlignmentFlag.AlignCenter)
    saving_layout.addWidget(saving_balance)
    saving_group.setLayout(saving_layout)
    main_layout.addWidget(saving_group)

    btn_layout = QVBoxLayout()
    for text in ["Deposit","Transfer","Widraw","Zelle"]:
        btn = QPushButton(text)
        btn.setFixedSize(QSize(100,60))
        btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        btn_layout.addWidget(btn)
    main_layout.addLayout(btn_layout)
    return main_window
