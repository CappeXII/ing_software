from account.controller.ControlloreAccount import ControlloreAccount
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QLineEdit


class VistaModificaAccount(QWidget):
    def __init__(self, account, modifica_nome, modifica_cognome, modifica_password,
                 modifica_codice_fiscale, elimina_callback):
        super(VistaModificaAccount, self).__init__()
        self.controller = ControlloreAccount(account)
        self.modifica_nome = modifica_nome
        self.modifica_cognome = modifica_cognome

        self.modifica_password = modifica_password
        self.modifica_codice_fiscale = modifica_codice_fiscale
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        h_layout1 = QHBoxLayout()

        label_nome = QLabel("Nome:")
        font_nome = label_nome.font()
        font_nome.setPointSize(17)
        label_nome.setFont(font_nome)
        h_layout1.addWidget(label_nome)

        text_nome = QLineEdit()
        text_nome.setText(self.controller.get_nome_account())
        h_layout1.addWidget(text_nome)

        v_layout.addLayout(h_layout1)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        h_layout2 = QHBoxLayout()
        label_cognome = QLabel("Cognome:")
        font_cognome = label_cognome.font()
        font_cognome.setPointSize(17)
        label_cognome.setFont(font_nome)
        h_layout2.addWidget(label_cognome)

        text_cognome = QLineEdit()
        text_cognome.setText(self.controller.get_cognome_account())
        h_layout2.addWidget(text_cognome)

        v_layout.addLayout(h_layout2)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        h_layout3 = QHBoxLayout()
        label_password = QLabel("Password:")
        font_password = label_password.font()
        font_password.setPointSize(17)
        label_password.setFont(font_password)
        h_layout3.addWidget(label_password)

        text_password = QLineEdit()
        text_password.setEchoMode(QLineEdit.Password)
        text_password.setText(self.controller.get_password_account())
        h_layout3.addWidget(text_password)

        v_layout.addLayout(h_layout3)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        h_layout4 = QHBoxLayout()
        label_codice_fiscale = QLabel("Codice Fiscale:")
        font_codice_fiscale = label_codice_fiscale.font()
        font_codice_fiscale.setPointSize(17)
        label_codice_fiscale.setFont(font_codice_fiscale)
        h_layout4.addWidget(label_codice_fiscale)

        text_codice_fiscale = QLineEdit()
        text_codice_fiscale.setText(self.controller.get_codice_fiscale_account())
        h_layout4.addWidget(text_codice_fiscale)

        v_layout.addLayout(h_layout4)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        update_btn = QPushButton("Modifica")
        update_btn.clicked.connect(
                lambda: self.modifica(text_nome, text_cognome, text_password, text_codice_fiscale))
        v_layout.addWidget(update_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Modifica account')

    def modifica(self, text_nome, text_cognome, text_password, text_codice_fiscale):
        if text_nome.isModified():
            self.modifica_nome(text_nome.text())
        if text_cognome.isModified():
            self.modifica_cognome(text_cognome.text())
        if text_password.isModified():
            self.modifica_password(text_password.text())
        if text_codice_fiscale.isModified():
            self.modifica_codice_fiscale(text_codice_fiscale.text())
        self.controller.save_data()
        self.elimina_callback()
        self.close()
