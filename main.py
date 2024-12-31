import sys
from PyQt6.QtWidgets import QApplication , QStackedWidget
from login import create_login_window
from signin import create_signin_window
from home import create_home_window
from page_profile import create_profile_window #import page_profile with function that we create in page.

if __name__ == "__main__":
    app = QApplication([])
    stacked_widget = QStackedWidget() # to built the object manage each window more easyly and to connect each window.
    login_window = create_login_window(stacked_widget)
    signin_window = create_signin_window(stacked_widget)
    home_window = create_home_window(stacked_widget)
    profile_window = create_profile_window(stacked_widget) # call function and add stacked widget to link with page_profile.

    stacked_widget.addWidget(login_window)# index [0]
    stacked_widget.addWidget(signin_window)#index[1]
    stacked_widget.addWidget(home_window)#index [2]
    stacked_widget.addWidget(profile_window) #index [3]


    stacked_widget.setCurrentWidget(login_window)
    stacked_widget.setFixedSize(380, 570)
    stacked_widget.setWindowTitle("Santander Bank")
    stacked_widget.show()
    
    app.exec()