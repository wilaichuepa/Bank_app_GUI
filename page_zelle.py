from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_zelle_window(stacked_widget):

    def send_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(10))
    def request_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(11))
    def contact_submit():
        stacked_widget.setCurrentWidget(stacked_widget.widget(12))


    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)
    btn_layout = QHBoxLayout(main_window)

    send_btn = QPushButton("Send")
    send_btn.clicked.connect(send_submit)
    send_btn.setFixedSize(QSize(100,60))
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(send_btn)

    request_btn = QPushButton("Request")
    request_btn.clicked.connect(request_submit)
    request_btn.setFixedSize(QSize(100,60))
    btn_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    btn_layout.addWidget(request_btn)
    main_layout.addLayout(btn_layout) # put send and request to main_layout 
    # buil 2 layout in same window // เอา วัตถุในแนวนอน send  request ใส่ใน QVBoxLayout
    contact_btn = QPushButton('+ New Contact')
    contact_btn.clicked.connect(contact_submit)
    contact_btn.setFixedWidth(100)
    main_layout.addWidget(contact_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))

    recippients_lb = QLabel('Recippients')
    recippients_lb.setAlignment(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
    recippients_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(recippients_lb)

    recippient_1_btn = QPushButton("Wilai Chuepa\n9733174164")
    recippient_1_btn.setFixedWidth(100)
    main_layout.addWidget(recippient_1_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))

    recippient_2_btn = QPushButton(" Mak Maxx\n1023456789")
    recippient_2_btn.setFixedWidth(100)
    main_layout.addWidget(recippient_2_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))

    recippient_2_btn = QPushButton(" Wilson Ws \n9087654321")
    recippient_2_btn.setFixedWidth(100)
    main_layout.addWidget(recippient_2_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(2, 2, QSizePolicy.Policy.Expanding))

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(2)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)

    return main_window