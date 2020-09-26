from PyQt5.QtWidgets import QApplication, QDialog
from login_window import LoginDialog
from sys import argv, exit
from sqlite3 import connect

def launch():
    connection = connect('bank_app.db')
    connection.execute("""CREATE TABLE IF NOT EXISTS client (
                                                            first_name TEXT NOT NULL,
                                                            last_name TEXT NOT NULL,
                                                            embg TEXT NOT NULL UNIQUE,
                                                            birthdate TEXT NOT NULL,
                                                            address TEXT NOT NULL,
                                                            client_creation_date TEXT NOT NULL,
                                                            PRIMARY KEY(embg));""")
    connection.execute("""CREATE TABLE IF NOT EXISTS client_account (
                                                                    embg TEXT NOT NULL,
                                                                    account_number TEXT NOT NULL,
                                                                    currency TEXT NOT NULL,
                                                                    balance TEXT NOT NULL,
                                                                    bank_product TEXT NOT NULL,
                                                                    account_creation_date TEXT NOT NULL);""")
    connection.execute("""CREATE TABLE IF NOT EXISTS login_register (
                                                                    username TEXT NOT NULL,
                                                                    password TEXT NOT NULL);""")
    connection.commit()
    connection.close()
    app = QApplication(argv)
    Dialog = QDialog()
    ui = LoginDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    exit(app.exec_())


if __name__ == "__main__":
    launch()
