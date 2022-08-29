from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from listapizze.controller.ControlloreListaPizze import ControlloreListaPizze
from listapizze.view.VistaInserisciPizza import VistaInserisciPizza
from pizza.view.VistaPizza import VistaPizza


class VistaListaPizze(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPizze, self).__init__(parent)
        self.controllore = ControlloreListaPizze()

        v_layout = QVBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        v_layout.addLayout(self.info_layout)

        add_btn = QPushButton("Nuovo")
        add_btn.clicked.connect(self.show_new_pizza)
        v_layout.addWidget(add_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Lista Pizze")

    def show_new_pizza(self):
        self.vista_inserisci_pizza = VistaInserisciPizza(self.controllore, self.update_ui)
        self.vista_inserisci_pizza.show()

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for pizza in self.controllore.get_lista_pizze():
            h_box = QHBoxLayout()
            label = QLabel(pizza.nome)
            font = label.font()
            font.setPointSize(18)
            label.setFont(font)
            h_box.addWidget(label)

            show_btn = QPushButton("Apri")
            show_btn.clicked.connect(lambda: self.show_selected_info(pizza))
            h_box.addWidget(show_btn)
            self.info_layout.addLayout(h_box)

    def show_selected_info(self, pizza):
        self.vista_pizza = VistaPizza(pizza, self.update_ui)
        self.vista_pizza.show()
