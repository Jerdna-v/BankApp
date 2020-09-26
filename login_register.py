from datetime import datetime
from sqlite3 import connect


class LoginRegister:
    def __init__(self, username, password1, password2=None):
        self.username = username
        self.password1 = password1
        self.password2 = password2

    def login(self):
        connection = connect("bank_app.db")
        result = connection.execute("SELECT username, password FROM login_register WHERE username = ? AND password = ?",
                                    (self.username, self.password1))

        if len(result.fetchall()) > 0:
            connection.close()
            self.activity_log('New login', self.username, self.password1)
            return True
        else:
            connection.close()
            self.activity_log('Invalid credentials', self.username, self.password1)
            return False


    def signup(self):
        connection = connect("bank_app.db")
        result = connection.execute("SELECT username FROM login_register WHERE username = ?", (self.username,))

        if self.password1 == self.password2:
            if len(result.fetchall()) <= 0:

                connection.execute("INSERT INTO login_register(username, password) VALUES(?, ?)", (self.username,
                                                                                                   self.password1))
                connection.commit()
                connection.close()
                self.activity_log('New user added', self.username, self.password1)
                return True
            else:
                connection.close()
                self.activity_log('Username already exists', self.username, self.password1)
                return False

    def activity_log(self, text, parameter1, parameter2='', parameter3=''):
        with open("activity_log.txt", 'a+') as f:
            f.write('\n{} - {} - {} - {} - {}'.format(str(datetime.now().replace(microsecond=0)),
                                                      text, parameter1, parameter2, parameter3))
