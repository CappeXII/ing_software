from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from listaaccount.view.VistaListaAccount import VistaListaAccount
from listaordini.view.VistaListaOrdini import VistaListaOrdini
from listapizze.view.VistaListaPizze import VistaListaPizze
from listamaterie.view.VistaListaMaterie import VistaListaMaterie


class VistaHomeAdmin(QWidget):
    def __init__(self):
        super(VistaHomeAdmin, self).__init__()
        v_layout = QVBoxLayout()
        ordini_btn = QPushButton("Ordini")
        ordini_btn.clicked.connect(self.go_vista_lista_ordini)
        v_layout.addWidget(ordini_btn)

        account_btn = QPushButton("Account")
        account_btn.clicked.connect(self.go_vista_lista_account)
        v_layout.addWidget(account_btn)

        pizze_btn = QPushButton("Pizze")
        pizze_btn.clicked.connect(self.go_vista_lista_pizze)
        v_layout.addWidget(pizze_btn)

        materie_btn = QPushButton("Materie")
        materie_btn.clicked.connect(self.go_vista_lista_materie)
        v_layout.addWidget(materie_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Home Camerieri")

    def go_vista_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.show()

    def go_vista_lista_account(self):
        self.vista_lista_account = VistaListaAccount()
        self.vista_lista_account.show()

    def go_vista_lista_pizze(self):
        self.vista_lista_pizze = VistaListaPizze()
        self.vista_lista_pizze.show()

    def go_vista_lista_materie(self):
        self.vista_lista_materie = VistaListaMaterie()
        self.vista_lista_materie.show()
