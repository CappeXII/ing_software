from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PyQt5.sip import delete

from listaordini.controller.ControlloreListaOrdini import ControlloreListaOrdini
from listaordini.view.VistaInserisciOrdine import VistaInserisciOrdine
from ordini.view.VistaOrdine import VistaOrdine


class VistaListaOrdini(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)
        self.vista_pizza = None
        self.controllore = ControlloreListaOrdini()

        v_layout = QVBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        v_layout.addLayout(self.info_layout)

        add_btn = QPushButton("Nuovo")
        add_btn.clicked.connect(self.show_new_pizza)
        v_layout.addWidget(add_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Ordini")

    def show_new_pizza(self):
        self.vista_inserisci_ordine = VistaInserisciOrdine(self.controllore, self.update_ui)
        self.vista_inserisci_ordine.show()

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.layout():
                delete(child)
        if self.controllore.get_lista_ordini():
            for ordine in self.controllore.get_lista_ordini():
                h_box = QHBoxLayout()
                label = QLabel(str(ordine.numero))
                font = label.font()
                font.setPointSize(18)
                label.setFont(font)
                h_box.addWidget(label)

                show_btn = QPushButton("Apri "+str(ordine.numero))
                show_btn.clicked.connect(self.show_selected_info)
                h_box.addWidget(show_btn)
                self.info_layout.addLayout(h_box)
                self.info_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def show_selected_info(self):
        ordine = self.controllore.get_ordine_by_numero(int(self.sender().text()[5:]))
        self.vista_pizza = VistaOrdine(ordine, self.close)
        self.vista_pizza.show()
