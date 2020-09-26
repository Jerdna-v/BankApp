from sqlite3 import connect
from datetime import datetime


class Edit:
    def __init__(self, radioButton1=None, embg=None, currency=None, bank_product=None, balance=None,
                 account_number=None, first_name=None, last_name=None, birthdate=None, address=None, radioButton2=None):
        self.account_number = account_number
        self.currency = currency
        self.bank_product = bank_product
        self.balance = balance
        self.account_creation_date = datetime.now().replace(microsecond=0)

        self.embg = embg

        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.address = address
        self.client_creation_date = datetime.now().replace(microsecond=0)

        self.radioButton1 = radioButton1
        self.radioButton2 = radioButton2

    def new(self):
        if self.embg.isdigit() and self.account_number.isdigit() and len(self.embg) == 13 and len(self.account_number) == 8:
            connection = connect("bank_app.db")
            cursor = connection.cursor()
            acc_num_checker = cursor.execute("SELECT account_number FROM client_account WHERE account_number=?",
                                             (self.account_number,))
            embg_checker = cursor.execute("SELECT embg FROM client WHERE embg = ?", (self.embg,))
            if self.radioButton1:
                if len(embg_checker.fetchall()) == 0 and len(acc_num_checker.fetchall()) == 0:
                    connection.execute("INSERT INTO client(first_name,last_name,embg,birthdate,address,"
                                       "client_creation_date) VALUES(?,?,?,?,?,?)",
                                       (self.first_name, self.last_name, self.embg, self.birthdate,
                                        self.address, self.client_creation_date))
                    connection.execute("INSERT INTO client_account(embg,account_number,currency,balance,"
                                        "bank_product,account_creation_date) VALUES(?,?,?,?,?,?)",
                                       (self.embg, self.account_number, self.currency, self.balance,
                                        self.bank_product, self.account_creation_date))
                    connection.commit()
                    self.activity_log('New client added ', self.embg, self.account_number)
                    connection.close()
                    return True
            else:
                if len(embg_checker.fetchall()) > 0 and len(acc_num_checker.fetchall()) == 0:
                    connection.execute("INSERT INTO client_account(embg,account_number,currency,balance,"
                                       "bank_product,account_creation_date) VALUES(?,?,?,?,?,?)",
                                       (self.embg, self.account_number, self.currency, self.balance,
                                        self.bank_product, self.account_creation_date))
                    connection.commit()
                    self.activity_log('New account added', self.embg, self.account_number)
                    connection.close()
                    return True
            self.activity_log('Invalid EMBG or account number', self.embg, self.account_number)
            return False

    def update(self):
        connection = connect("bank_app.db")
        embg_checker = connection.execute("SELECT embg FROM client WHERE embg = ?", (self.embg,))
        acc_num_checker = connection.execute("SELECT account_number FROM client_account WHERE account_number=?",
                                             (self.account_number,))
        if len(embg_checker.fetchall()) > 0:
            if self.radioButton1:
                connection.execute("UPDATE client SET first_name=?, last_name=?, address=? WHERE embg=?",
                                   (self.first_name, self.last_name, self.address, self.embg))
                connection.commit()
                self.activity_log('Client updated', self.embg)
                connection.close()
                return True
            elif self.radioButton2:
                if len(acc_num_checker.fetchall()) > 0:
                    connection.execute("UPDATE client_account SET currency=?, balance=?, bank_product=?"
                                       " WHERE account_number=?",
                                       (self.currency, self.balance, self.bank_product, self.account_number))
                    connection.commit()
                    self.activity_log('Account updated', self.embg)
                    connection.close()
                    return True
        self.activity_log('Nonexistent EMBG or account number or no button checked', self.embg, self.account_number)
        connection.close()
        return False

    def delete(self, c_a=0):
        connection = connect("bank_app.db")
        embg_checker = connection.execute("SELECT embg FROM client WHERE embg = ?", (self.embg,))
        acc_num_checker = connection.execute("SELECT account_number FROM client_account WHERE account_number=?",
                                             (self.account_number,))
        if len(embg_checker.fetchall()) > 0:
            if c_a == 1:
                if len(acc_num_checker.fetchall()) > 0:
                    connection.execute("DELETE FROM client_account WHERE embg=? AND account_number=?",
                                       (self.embg, self.account_number))
                    connection.commit()
                    self.activity_log('Account deleted', self.embg, self.account_number)
                    connection.close()
                    return True
            else:
                connection.execute("DELETE FROM client_account WHERE embg=?", (self.embg,))
                connection.execute("DELETE FROM client WHERE embg=?", (self.embg,))
                connection.commit()
                self.activity_log("Client deleted", self.embg)
                connection.close()
                return True
        self.activity_log('Nonexistent EMBG or account number', self.embg, self.account_number)
        connection.close()
        return False

    def activity_log(self, text, parameter1, parameter2='', parameter3=''):
        with open("activity_log.txt", 'a+') as f:
            f.write('\n{} - {} - {} - {} - {}'.format(str(datetime.now().replace(microsecond=0)),
                                                      text, parameter1, parameter2, parameter3))