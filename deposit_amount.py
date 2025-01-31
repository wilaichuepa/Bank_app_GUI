
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
   

def create_deposit_window(stacked_widget):
    # Main window setup
    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

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
    main_layout.addWidget(deposit_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    # main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    # Back button to navigate home
    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)
    

    

    return main_window
