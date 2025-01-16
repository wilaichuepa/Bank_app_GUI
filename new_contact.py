from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_contact_window(stacked_widget):

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))
    #Set layout to be in center
    main_layout = QVBoxLayout()
    main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_window.setLayout(main_layout)

    firstname_lb = QLabel('Frist name')
    firstname_input = QLineEdit()
    main_layout.addWidget(firstname_lb)
    main_layout.addWidget(firstname_input)

    lastname_lb = QLabel('Last name')
    lastname_input = QLineEdit()
    main_layout.addWidget(lastname_lb)
    main_layout.addWidget(lastname_input)

    nickname_lb = QLabel('Nickname(Optional)')
    email_input = QLineEdit()
    main_layout.addWidget(nickname_lb)
    main_layout.addWidget(email_input)

    add_btn = QPushButton('Add')
    add_btn.setFixedWidth(100)
    main_layout.addWidget(add_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(9)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight)

    return main_window