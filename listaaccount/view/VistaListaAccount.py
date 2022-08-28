from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QHBoxLayout, QLabel

from account.view.VistaAccount import VistaAccount
from listaaccount.controller.ControlloreListaAccount import ControlloreListaAccount
from listaaccount.view.VistaInserisciAccount import VistaInserisciAccount


class VistaListaAccount(QWidget):
    def __init__(self, parent=None):
        super(VistaListaAccount, self).__init__(parent)

        v_layout = QVBoxLayout()
        self.controllore = ControlloreListaAccount()
        self.info_layout = QVBoxLayout()
        self.update_ui()
        v_layout.addLayout(self.info_layout)

        v_layout.addWIdget(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        insert_button = QPushButton("Inserisci un nuovo account")
        insert_button.clicked.connect(self.show_add_account)
        v_layout.addWidget(insert_button)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Account')


    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for account in self.controllore.get_lista_account():
            h_box = QHBoxLayout()
            label = QLabel(account.username+", alias "+account.cognome+" "+account.nome)
            font = label.font()
            font.setPointSize(18)
            label.setFont(font)
            h_box.addWidget(label)

            open_btn = QPushButton("Apri")
            open_btn.clicked.connect(self.show_selected_info(account))
            h_box.addWidget(open_btn)
            self.info_layout.addLayout(h_box)



    def show_selected_info(self, account):
        self.vista_account = VistaAccount(account, self.update_ui)
        self.vista_account.show()

    def show_add_account(self):
        self.vista_inserisci_account = VistaInserisciAccount(self.controllore, self.update_ui)
        self.vista_inserisci_account.show()
