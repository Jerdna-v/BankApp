from PyQt5 import QtCore, QtGui, QtWidgets
from view_window import DataGrid

class SearchDialog(object):
    def setupUi(self, Dialog, buttonClicked):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 103)
        self.Dialog = Dialog
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 40, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupbox = QtWidgets.QGroupBox(Dialog)
        self.groupbox.setGeometry(QtCore.QRect(50, 23, 185, 51))
        self.groupbox.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.groupbox.setObjectName("groupbox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buttonClicked = buttonClicked
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.clicked.connect(self.resultShow)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def resultShow(self):
        if self.buttonClicked == 'EMBG':
            self.window = DataGrid(embg=self.lineEdit.text())
        elif self.buttonClicked == 'Account number':
            self.window = DataGrid(account_number=self.lineEdit.text())
        self.window.show()
        self.Dialog.close()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", self.buttonClicked))