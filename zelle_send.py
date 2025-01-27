from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_send_window(stacked_widget):

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
    main_window.setLayout(main_layout)

    send_to_lb = QLabel('Send To ')
    # main_layout.addWidget(send_to_lb)
    send_to_lb.setStyleSheet('font-size:15px; font-weight:bold')
    main_layout.addWidget(send_to_lb, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20,30,QSizePolicy.Policy.Expanding))

    email_phone_lb = QLabel('Email/Phone')
    # email_phone_lb.setAlignment(Qt.AlignmentFlag.AlignTop)
    main_layout.addWidget(email_phone_lb)
    email_phone_input = QLineEdit()
    main_layout.addWidget(email_phone_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))

    zelle_amount_lb = QLabel('Zelle Amonut')
    main_layout.addWidget(zelle_amount_lb)
    zelle_amount_input = QLineEdit()
    main_layout.addWidget(zelle_amount_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))
    send_btn = QPushButton('Send')
    main_layout.addWidget(send_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    send_btn.setFixedWidth(100)

    main_layout.addStretch()

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(9)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)
   
    
    return main_window
    
    
    
    # input_text_layout = QHBoxLayout(main_window)

    # email_phone_lb = QLabel('Email/Phone')
    # email_phone_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    # email_phone_lb.setStyleSheet('font-size:15px;text-align:center')
    # main_layout.addWidget(email_phone_lb)

    # # send_input = QLineEdit()
    # # input_text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # # input_text_layout.addWidget(send_input)
    # # send_input.setPlaceholderText("+1")
    # # main_layout.addWidget(send_input)

    # zelle_amount = QLabel('Zelle Amount')
    # zelle_amount.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    # zelle_amount.setStyleSheet('font-size:15px;text-align:center')
    # main_layout.addWidget(zelle_amount)

    # zelle_amount_input = QLineEdit()
    # input_text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # input_text_layout.addWidget(zelle_amount_input)
    # zelle_amount_input.setPlaceholderText("+1")
    # main_layout.addWidget(zelle_amount_input)