from PyQt5 import QtCore, QtGui, QtWidgets
from signup_window import SignUpDialog
from login_register import LoginRegister
import main_window


class LoginDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 274)
        Dialog.setStyleSheet("")
        Dialog.setWindowTitle("Login")
        self.Dialog = Dialog
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(150, 110, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")

        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(150, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")

        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")

        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")

        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(230, 200, 51, 23))
        self.login_btn.setObjectName("login_btn")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.login_btn.setFont(font)
        self.login_btn.clicked.connect(self.loginSender)

        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(290, 200, 51, 23))
        self.signup_btn.setObjectName("signup_btn")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.signup_btn.setFont(font)
        self.signup_btn.clicked.connect(self.signUpShow)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def loginSender(self):
        self.login = LoginRegister(username=self.uname_lineEdit.text(), password1=self.pass_lineEdit.text())
        self.login = self.login.login()
        if not self.login:
            self.showMessageBox('Warning', 'Invalid username or password.')
        else:
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = main_window.mainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
            self.Dialog.close()

    def signUpShow(self):
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = SignUpDialog()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.show()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.u_name_label.setText(_translate("Dialog", "Username:"))
        self.pass_label.setText(_translate("Dialog", "Password:"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.signup_btn.setText(_translate("Dialog", "Sign up"))
        self.label.setText(_translate("Dialog", "Login"))
