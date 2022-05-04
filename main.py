import sys
from src.login_gui import Ui_MainWindow, QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    app.exec_()
    app.exit()

    if window.success_login:
        username = window.LoginUsername
        password = window.LoginPassword
        print(username, password)
    else:
        sys.exit()


if __name__ == "__main__":
    main()