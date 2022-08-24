from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QCheckBox

from account.model.Account import Account


class VBoxLayout:
    pass


class VistaInserisciAccount(QWidget):
    def __init__(self, controllore, callback):
        super(VistaInserisciAccount, self).__init__()
        self.controllore = controllore
        self.callback = callback

        v_layout = QVBoxLayout()
        self.nome_text = QLineEdit(self)
        self.nome_text.setPlaceholderText("Nome")
        v_layout.addWidget(self.nome_text)

        self.cognome_text = QLineEdit(self)
        self.cognome_text.setPlaceholderText("Cognome")
        v_layout.addWidget(self.cognome_text)

        self.username_text = QLineEdit(self)
        self.username_text.setPlaceholderText("Username")
        v_layout.addWidget(self.username_text)

        self.password_text = QLineEdit(self)
        self.password_text.setPlaceholderText("Password")
        self.password_text.setEchoMode("Password")
        v_layout.addWidget(self.password_text)

        self.codice_fiscale_text = QLineEdit(self)
        self.codice_fiscale_text.setPlaceholderText("Codice fiscale")
        v_layout.addWidget(self.codice_fiscale_text)

        self.isAdmin = QCheckBox("Tipologia (spuntare solo se admin)")
        v_layout.addWidget(self.isAdmin)

        add_btn = QPushButton("Inserisci")
        add_btn.clicked.connect(self.inserisci_account)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Insersci Account')

    def inserisci_account(self):
        nome = self.nome_text.text()
        cognome = self.cognome_text.text()
        username = self.username_text.text()
        password =self.password_text.text()
        codice_fiscale = self.codice_fiscale_text.text()
        isAdmin = self.isAdmin.isChecked()

        if nome == "" or cognome == "" or username == "" or password == "" or codice_fiscale == "":
            QMessageBox.critical(self, 'Errore', 'Inserire tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        else:
            check = False
            for account in self.controllore.get_lista_account():
                if username == account.username:
                    check = True
            if check:
                QMessageBox.critical(self, 'Errore', 'Esiste già un acocunt con questo username', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controllore.add_account(Account(nome, cognome, codice_fiscale, username, password, isAdmin))
                self.callback()
                self.close()


