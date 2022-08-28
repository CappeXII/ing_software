from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

from listaaccount.controller.ControlloreListaAccount import ControlloreListaAccount


class VistaLogin(QWidget):
    def __init__(self):
        super(VistaLogin, self).__init__()
        self.controllore = ControlloreListaAccount()
        v_layout = QVBoxLayout()

        username_text = QLineEdit()
        username_text.setPlaceholderText("Username")
        v_layout.addWidget(username_text)

        password_text = QLineEdit()
        password_text.setPlaceholderText("Password")
        password_text.setEchoMode("Password")
        v_layout.addWidget(password_text)

        login_btn = QPushButton("Login")
        login_btn.clicked.connect(self.login(username_text.text(), password_text.text()))
        v_layout.addWidget(login_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Home")

    def login(self, username, password):
        if username == "" or password == "":
            QMessageBox.critical(self, 'Errore', 'Inserire tutte le informazioni richieste', QMessageBox.Ok,
                                 QMessageBox.Ok)
        else:
            for account in self.controllore.get_lista_account():
                if username == account.username and password == account.password:
                    if account.isAdmin:
                        self.go_vista_home_admin()
                    else:
                        self.go_vista_home_camerieri()
                else:
                    QMessageBox.critical(self, 'Errore', 'Credenziali errate', QMessageBox.Ok, QMessageBox.Ok)

    def go_vista_home_admin(self):
        self.vista_home_admin = VistaHomeAdmin()
        self.vista_home_admin.show()

    def go_vista_home_camerieri(self):
        self.vista_home_camerieri = VistaHomeCamerieri()
        self.vista_home_camerieri.show()