from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from account.controller.ControlloreAccount import ControlloreAccount


class VistaEliminaAccount(QWidget):
    def __init__(self, account, elimina_account, elimina_callback):
        super(VistaEliminaAccount, self).__init__()
        self.controllore = ControlloreAccount(account)
        self.elimina_account = elimina_account
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel("Vuoi eliminare l'account " + self.controllore.get_username_account() + "?")
        font_nome = label_nome.font()
        font_nome.setPointSize(18)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Eliminazione account')

    def elimina(self):
        self.elimina_account()
        self.elimina_callback()
        self.close()
