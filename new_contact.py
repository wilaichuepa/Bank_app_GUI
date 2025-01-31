from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

def create_contact_window(stacked_widget):

    main_window = QWidget()
    main_window.setWindowTitle("Santander Bank")
    main_window.setFixedSize(QSize(380, 570))
    #Set layout to be in centop
    main_layout = QVBoxLayout()
    main_window.setLayout(main_layout)
    main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

    new_contact_lb = QLabel('New Contact Information ')
    # main_layout.addWidget(new_contact_lb)
    new_contact_lb.setStyleSheet('font-size:15px; font-weight:bold')
    main_layout.addWidget(new_contact_lb, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20,30,QSizePolicy.Policy.Expanding))
    
    firstname_lb = QLabel('Frist name')
    main_layout.addWidget(firstname_lb)
    firstname_input = QLineEdit()
    main_layout.addWidget(firstname_input)

    lastname_lb = QLabel('Last name')
    main_layout.addWidget(lastname_lb)
    lastname_input = QLineEdit()
    main_layout.addWidget(lastname_input)

    nickname_lb = QLabel('Nickname(Optional)')
    main_layout.addWidget(nickname_lb)
    email_input = QLineEdit()
    main_layout.addWidget(email_input)

    add_btn = QPushButton('Add')
    add_btn.setFixedWidth(100)
    main_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding))
    main_layout.addWidget(add_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

    #back_layout = QVBoxLayout()

# Add a spacer to push content to the bottom
    main_layout.addStretch()

    back_btn = QPushButton('Back')
    back_btn.setFixedWidth(60)
    back_btn.clicked.connect(lambda: stacked_widget.setCurrentWidget(stacked_widget.widget(9)))
    main_layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)
    #main_layout.addWidget(back_layout)
    # main_layout.addSpacerItem(QSpacerItem(10,100,QSizePolicy.Policy.Expanding))

    return main_window