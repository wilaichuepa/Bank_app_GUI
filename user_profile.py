from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
import sys

def show_profile_info():
    # Mock profile information. Replace this with an API call if needed.
    profile_info = {
        "email": "jan.doe@example.com",
        "phone": "+1 123-456-7890",
        "address": "1234 Elm Street, Springfield, USA"
    }
    
    # Create and display the QMessageBox
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Profile Information")
    msg_box.setIcon(QMessageBox.Icon.Information)
    
    # Format profile information into a message
    profile_message = (
        f"Email: {profile_info['email']}\n"
        f"Phone: {profile_info['phone']}\n"
        f"Address: {profile_info['address']}"
    )
    msg_box.setText(profile_message)
    msg_box.exec()  # Show the message box

if __name__ == "__main__":
    # Initialize the application
    app = QApplication(sys.argv)
    
    # Create a main window with a button to trigger the function
    window = QWidget()
    window.setWindowTitle("Profile Demo")
    window.setFixedSize(300, 200)
    
    layout = QVBoxLayout()
    button = QPushButton("Show Profile")
    button.clicked.connect(show_profile_info)  # Connect button click to the function
    layout.addWidget(button)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec())