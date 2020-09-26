from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel
from PyQt5 import QtWidgets
import re


class DataGrid(QtWidgets.QWidget):
    def __init__(self, parent=None, buttonClicked=None, embg=None, account_number=None):
        super(DataGrid, self).__init__(parent)
        self.buttonClicked = buttonClicked
        self.embg = embg
        self.account_number = account_number
        self.db = None
        self.layout = QtWidgets.QVBoxLayout()
        self.queryModel = QSqlQueryModel()
        self.tableView = QtWidgets.QTableView()
        self.tableView.setModel(self.queryModel)
        self.totalPageLabel = QtWidgets.QLabel()
        self.currentPageLabel = QtWidgets.QLabel()
        self.switchPageLineEdit = QtWidgets.QLineEdit()
        self.prevButton = QtWidgets.QPushButton("Prev")
        self.nextButton = QtWidgets.QPushButton("Next")
        self.switchPageButton = QtWidgets.QPushButton("Enter")
        self.currentPage = 1
        self.totalPage = None
        self.totalRecordCount = None
        self.pageRecordCount = 6

        self.initUI()
        self.initializedModel()
        self.setUpConnect()
        self.updateStatus()

    def initUI(self):
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.layout.addWidget(self.tableView)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.prevButton)
        hLayout.addWidget(self.nextButton)
        hLayout.addWidget(QtWidgets.QLabel("Skip to"))
        self.switchPageLineEdit.setFixedWidth(40)
        hLayout.addWidget(self.switchPageLineEdit)
        hLayout.addWidget(QtWidgets.QLabel("page"))
        hLayout.addWidget(self.switchPageButton)
        hLayout.addWidget(QtWidgets.QLabel("Current page:"))
        hLayout.addWidget(self.currentPageLabel)
        hLayout.addWidget(QtWidgets.QLabel("Total pages:"))
        hLayout.addWidget(self.totalPageLabel)
        hLayout.addStretch(1)

        self.layout.addLayout(hLayout)
        self.setLayout(self.layout)

        self.setWindowTitle("View")
        self.showMaximized()

    def sqlStatement(self):
        if self.buttonClicked == 'Client/accounts':
            self.pageRecordCount = 3
            return "Select* from client inner join client_account on client_account.embg = client.embg" \
                   " order by last_name ASC, datetime(account_creation_date) DESC"
        elif self.buttonClicked == 'Clients':
            self.pageRecordCount = 5
            return "Select* from client order by last_name ASC, datetime(client_creation_date) DESC"
        elif self.buttonClicked == 'Accounts':
            self.pageRecordCount = 4
            return "Select* from client_account order by datetime(account_creation_date) DESC"
        elif self.embg != None:
            return "Select* from client inner join client_account on client_account.embg = client.embg" \
                   " where client_account.embg={} order by last_name ASC, datetime(account_creation_date) DESC".format\
                (self.embg)
        elif self.account_number != None:
            return "Select* from client inner join client_account on client_account.embg = client.embg" \
                   " where account_number={} order by last_name ASC, datetime(account_creation_date) DESC".format\
                (self.account_number)

    def setUpConnect(self):
        self.prevButton.clicked.connect(self.onPrevPage)
        self.nextButton.clicked.connect(self.onNextPage)
        self.switchPageButton.clicked.connect(self.onSwitchPage)

    def initializedModel(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("bank_app.db")
        if not self.db.open():
            return False
        sql = self.sqlStatement()
        self.queryModel.setQuery(sql, self.db)
        self.totalRecordCount = self.queryModel.rowCount()
        if self.totalRecordCount % self.pageRecordCount == 0:
            self.totalPage = self.totalRecordCount / self.pageRecordCount
        else:
            self.totalPage = int(self.totalRecordCount / self.pageRecordCount) + 1
        sql = sql + " limit %d,%d" % (0, self.pageRecordCount)
        self.queryModel.setQuery(sql, self.db)

    def onPrevPage(self):
        self.currentPage -= 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onNextPage(self):
        self.currentPage += 1
        limitIndex = (self.currentPage - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.updateStatus()

    def onSwitchPage(self):
        szText = self.switchPageLineEdit.text()
        pattern = re.compile('^[0-9]+$')
        match = pattern.match(szText)
        if not match:
            QtWidgets.QMessageBox.information(self, "Tips", "please enter a number.")
            return
        if szText == "":
            QtWidgets.QMessageBox.information(self, "Tips", "Please enter a jump page.")
            return
        pageIndex = int(szText)
        if pageIndex > self.totalPage or pageIndex < 1:
            QtWidgets.QMessageBox.information(self, "Tips", "No page specified, re-enter.")
            return

        limitIndex = (pageIndex - 1) * self.pageRecordCount
        self.queryRecord(limitIndex)
        self.currentPage = pageIndex
        self.updateStatus()

    def queryRecord(self, limitIndex):
        sql = self.sqlStatement() + " limit %d,%d" % (limitIndex, self.pageRecordCount)
        self.queryModel.setQuery(sql)

    def updateStatus(self):
        self.currentPageLabel.setText(str(self.currentPage))
        self.totalPageLabel.setText(str(self.totalPage))
        if self.currentPage <= 1:
            self.prevButton.setEnabled(False)
        else:
            self.prevButton.setEnabled(True)

        if self.currentPage >= self.totalPage:
            self.nextButton.setEnabled(False)
        else:
            self.nextButton.setEnabled(True)

    def closeEvent(self, event):
        self.db.close()
