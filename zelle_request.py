from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_request_window(stacked_widget):

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)
    input_text_layout = QHBoxLayout(main_window)

    request_from_lb = QLabel('Request From')
    # main_layout.addWidget(request_from_lb)
    request_from_lb.setStyleSheet('font-size:15px; font-weight:bold')
    main_layout.addWidget(request_from_lb, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20,30,QSizePolicy.Policy.Expanding))

    email_phone_lb = QLabel('Email/Phone')
    email_phone_input = QLineEdit()
    main_layout.addWidget(email_phone_lb)
    main_layout.addWidget(email_phone_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))

    request_amount_lb = QLabel('Request Amonut')
    request_amount_input = QLineEdit()
    main_layout.addWidget(request_amount_lb)
    main_layout.addWidget(request_amount_input)

    main_layout.addSpacerItem(QSpacerItem(50, 30, QSizePolicy.Policy.Expanding))
    request_btn = QPushButton('Request')
    request_btn.setFixedWidth(100)
    main_layout.addWidget(request_btn, alignment=Qt.AlignmentFlag.AlignCenter)

    main_layout.addStretch()

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(9)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)
    

    return main_window

# email_phone_lb = QLabel('Email/Phone')
    # email_phone_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    # email_phone_lb.setStyleSheet('font-size:15px;text-align:center')
    # main_layout.addWidget(email_phone_lb)

    # request_input = QLineEdit()
    # input_text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # input_text_layout.addWidget(request_input)
    # request_input.setPlaceholderText("+1")
    # main_layout.addWidget(request_input)

    # request_amount = QLabel('Request Amount')
    # request_amount.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    # request_amount.setStyleSheet('font-size:15px;text-align:center')
    # main_layout.addWidget(request_amount)

    # request_amount_input = QLineEdit()
    # input_text_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    # input_text_layout.addWidget(request_amount_input)
    # request_amount_input.setPlaceholderText("+1")
    # main_layout.addWidget(request_amount_input)