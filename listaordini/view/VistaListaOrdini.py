from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel

from listaordini.controller.ControlloreListaOrdini import ControlloreListaOrdini
from ordini.view.VistaOrdine import VistaOrdine


class VistaListaOrdini(QWidget):
    def __init__(self, parent=None):
        super(VistaListaOrdini, self).__init__(parent)
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
            if child.widget():
                child.widget().deleteLater()
        for ordine in self.controllore.get_lista_ordini():
            h_box = QHBoxLayout()
            label = QLabel(ordine.numero)
            font = label.font()
            font.setPointSize(18)
            label.setFont(font)
            h_box.addWidget(label)

            show_btn = QPushButton("Apri")
            show_btn.clicked.connect(self.show_selected_info(ordine))
            h_box.addWidget(show_btn)
            self.info_layout.addLayout(h_box)

    def show_selected_info(self, ordine):
        self.vista_pizza = VistaOrdine(ordine, self.update_ui)
        self.vista_pizza.show()
