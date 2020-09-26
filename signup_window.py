from PyQt5 import QtCore, QtGui, QtWidgets
from login_register import LoginRegister


class SignUpDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(570, 375)
        self.Dialog = Dialog

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(250, 130, 141, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")

        self.password1_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password1_lineEdit.setGeometry(QtCore.QRect(250, 180, 141, 20))
        self.password1_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password1_lineEdit.setObjectName("password1_lineEdit")

        self.password2_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password2_lineEdit.setGeometry(QtCore.QRect(250, 230, 141, 20))
        self.password2_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2_lineEdit.setObjectName("password2_lineEdit")

        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(270, 290, 75, 23))
        self.signup_btn.setObjectName("signup_btn")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.signup_btn.setFont(font)
        self.signup_btn.clicked.connect(self.signupSender)

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def signupSender(self):
        self.signup = LoginRegister(username=self.uname_lineEdit.text(),
                                    password1=self.password1_lineEdit.text(),
                                    password2=self.password2_lineEdit.text())
        self.signup = self.signup.signup()
        if self.signup:
            self.showMessageBox('Successful', 'New user created')
            self.Dialog.close()
        else:
            self.showMessageBox('Warning', 'Existent username')

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Close)
        msgBox.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign up"))
        self.label.setText(_translate("Dialog", "Username:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.signup_btn.setText(_translate("Dialog", "Sign up"))
        self.label_4.setText(_translate("Dialog", "Sign up"))
