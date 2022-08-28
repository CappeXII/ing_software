from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from account.controller.ControlloreAccount import ControlloreAccount
from account.view.VistaModificaAccount import VistaModificaAccount
from account.view.VistaEliminaAccount import VistaEliminaAccount


class VistaAccount(QWidget):
    def __init__(self, account, elimina_callback, parent=None):
        super(VistaAccount, self).__init__(parent)
        self.controllore = ControlloreAccount(account)
        self.elimina_callback = elimina_callback
        h_layout = QHBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        h_layout.addLayout(self.info_layout)

        button_layouts = QVBoxLayout()
        update_button = QPushButton("Modifica")
        update_button.clicked.connect(self.show_update_account)
        button_layouts.addWidget(update_button)

        delete_button = QPushButton("Elimina")
        delete_button.clicked.connect(self.show_delete_account)
        button_layouts.addWidget(delete_button)
        h_layout.addLayout(button_layouts)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Account ' + self.controllore.get_username_account())

    def show_update_account(self):
        self.vista_modifica = VistaModificaAccount(self.controllore.model, self.controllore.update_nome_account,
                                                   self.controllore.update_cognome_account,
                                                   self.controllore.update_username_account,
                                                   self.controllore.update_password_account,
                                                   self.controllore.update_codice_fiscale_account, self.update_ui)
        self.vista_modifica.show()

    def show_delete_account(self):
        self.vista_elimina = VistaEliminaAccount(self.controllore.model, self.controllore.delete_account,
                                                 self.elimina_callback)
        self.vista_elimina.show()
        self.close()

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        label_nome = QLabel("Nome: " + self.controllore.get_nome_account())
        font_nome = label_nome.font()
        font_nome.setPointSize(17)
        label_nome.setFont(font_nome)
        self.info_layout.addWidget(label_nome)

        label_cognome = QLabel("Cognome: " + self.controllore.get_cognome_account())
        font_cognome = label_cognome.font()
        font_cognome.setPointSize(17)
        label_cognome.setFont(font_cognome)
        self.info_layout.addWidget(label_cognome)

        label_username = QLabel("Username: " + self.controllore.get_username_account())
        font_username = label_username.font()
        font_username.setPointSize(17)
        label_username.setFont(font_username)
        self.info_layout.addWidget(label_username)

        label_password = QLabel("Password: " + self.controllore.get_password_account())
        font_password = label_password.font()
        font_password.setPointSize(17)
        label_password.setFont(font_password)
        self.info_layout.addWidget(label_password)

        label_codice_fiscale = QLabel("Codice fiscale: " + self.controllore.get_codice_fiscale_account())
        font_codice_fiscale = label_codice_fiscale.font()
        font_codice_fiscale.setPointSize(17)
        label_codice_fiscale.setFont(font_codice_fiscale)
        self.info_layout.addWidget(label_codice_fiscale)
