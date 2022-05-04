import ctypes
import json
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QAction, QLabel


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadusers()
        self.show()

    def loadusers(self):
        self.success_login = False
        with open("src/user_data.json", "r") as file:
            self.LoginUsernames: dict = json.load(file)

    def update_user(self):
        with open("src/user_data.json", "w") as file:
            json.dump(self.LoginUsernames, file, indent=4)

    def delete_user(self, username: str):
        self.LoginUsernames.pop(username)
        self.update_user()

    def setupUi(self):
        uic.loadUi("gui/login.ui", self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Login Panel")
        # Menu
        self.LoginUserEdit: QLineEdit
        self.RegisterUserEdit: QLineEdit

        # Pass Echo Mode
        self.LoginPassEdit: QLineEdit
        self.RegisterPassEdit: QLineEdit
        self.LoginPassEdit.setEchoMode(2)
        self.RegisterPassEdit.setEchoMode(2)

        # Login Action
        self.actionLogin: QAction
        self.actionLogin.triggered.connect(self.LoginVisible)

        # Register Action
        self.actionRegister: QAction
        self.actionRegister.triggered.connect(self.RegisterVisible)

        # Login Button
        self.LoginButton: QPushButton
        self.LoginButton.clicked.connect(self.LoginChecking)

        # Register Button
        self.RegisterButton: QPushButton
        self.RegisterButton.clicked.connect(self.RegisterChecking)

        # Login Widget
        self.LoginWidget: QtWidgets
        self.LoginWidget.setVisible(False)

        # Register Widget
        self.RegisterWidget: QtWidgets
        self.RegisterWidget.setVisible(False)

    def LoginVisible(self):
        self.RegisterWidget.setVisible(False)
        self.LoginWidget.setVisible(True)

    def RegisterVisible(self):
        self.RegisterWidget.setVisible(True)
        self.LoginWidget.setVisible(False)

    def LoginChecking(self):
        self.LoginPassword = self.LoginPassEdit.text()
        self.LoginUsername = self.LoginUserEdit.text()
        if self.LoginUsername in self.LoginUsernames:
            if self.LoginPassword == self.LoginUsernames[self.LoginUsername]:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    "User Name ve ya Parol düzgün daxil edilib, programa yönləndirilisiniz !",
                    "Məlumat !",
                    0,
                )
                self.success_login = True

                self.close()
            else:  # password failed
                ctypes.windll.user32.MessageBoxW(
                    0, "User Name ve ya Parol düzgün deyil !", "Diqqət !", 0
                )
        else:  #  user not found
            ctypes.windll.user32.MessageBoxW(
                0, "User Name ve ya Parol düzgün deyil !", "Diqqət !", 0
            )

    def RegisterChecking(self):
        self.RegisterPassword = self.RegisterPassEdit.text()
        self.RegisterUsername = self.RegisterUserEdit.text()
        self.LoginUsernames[self.RegisterUsername] = self.RegisterPassword
        self.update_user()
        print(self.LoginUsernames)
