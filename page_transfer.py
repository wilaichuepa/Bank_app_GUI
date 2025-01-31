from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_transfer_window(stacked_widget):

    def submit_transfer_checking():
        stacked_widget.setCurrentWidget(stacked_widget.widget(7))

    def submit_transfer_saving():
        stacked_widget.setCurrentWidget(stacked_widget.widget(8))


    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))

    main_layout = QVBoxLayout(main_window)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    transfer_lb = QLabel('Make a Transfer')
    transfer_lb.setAlignment(Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignTop)
    transfer_lb.setStyleSheet('font-size:15px;text-align:center')
    main_layout.addWidget(transfer_lb)

    transfer_group = QGroupBox('Transfer from')
    transfer_group.setAlignment(Qt.AlignmentFlag.AlignCenter)
    transfer_layout = QVBoxLayout()
    transfer_group.setLayout(transfer_layout)
    transfer_btn_1 = QPushButton("Checking            500.00$")
    transfer_btn_2 = QPushButton("Saving            500,000.00$")
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