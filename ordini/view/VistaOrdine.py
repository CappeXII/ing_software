from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, \
    QAbstractItemView, QLineEdit, QLabel

from listapizze.controller.ControlloreListaPizze import ControlloreListaPizze
from ordini.controller.ControlloreOrdine import ControlloreOrdine
from ordini.view.VistaEliminaOrdine import VistaEliminaOrdine


class VistaOrdine(QWidget):
    def __init__(self, ordine, elimina_callback, parent=None):

        super(VistaOrdine, self).__init__(parent)
        self.controllore = ControlloreOrdine(ordine)
        self.controller = ControlloreListaPizze()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        h_layout = QHBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        h_layout.addLayout(self.info_layout)

        btn_layout = QVBoxLayout()
        delete_btn = QPushButton("Elimina")
        delete_btn.clicked.connect(self.show_delete_ordine)
        btn_layout.addWidget(delete_btn)
        h_layout.addLayout(btn_layout)
        v_layout.addLayout(h_layout)

        add_layout = QHBoxLayout()
        pizza_name = QListWidget()
        for pizza in self.controller.get_lista_pizze():
            pasto = QListWidgetItem(pizza.nome)
            pizza_name.addItem(pasto)
        pizza_name.setSelectionMode(QAbstractItemView.SingleSelection)
        add_layout.addWidget(pizza_name)
        quantita = QLineEdit()
        quantita.setPlaceholderText("Quantità")
        add_layout.addWidget(quantita)
        add_btn = QPushButton()
        add_btn.clicked.connect( lambda: self.add_pizza(pizza_name.selectedItems(), quantita.text()))
        add_layout.addWidget(add_btn)
        v_layout.addLayout(add_layout)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Ordine " + str(self.controllore.get_numero()))

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.info_layout.addWidget(QLabel(str(self.controllore.get_numero())))
        if self.controllore.get_pizze():
            for pizza in self.controllore.get_pizze():
                self.info_layout.addWidget(QLabel(pizza[0].nome + " " + pizza[1]))

    def show_delete_ordine(self):
        self.vista_elimina_ordine = VistaEliminaOrdine(self.controllore.model, self.controllore.delete_ordine,
                                                       self.elimina_callback)
        self.vista_elimina_ordine.show()
        self.close()

    def add_pizza(self, materia, quantita):
        self.controllore.add_pizza(self.controller.get_pizza_by_nome(materia), quantita)
        self.update_ui()
