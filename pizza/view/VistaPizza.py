from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem, \
    QAbstractItemView, QLineEdit, QLabel

from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from pizza.controller.ControllorePizza import ControllorePizza
from pizza.view.VistaEliminaPizza import VistaEliminaPizza
from pizza.view.VistaModificaPizza import VistaModificaPizza


class VistaPizza(QWidget):
    def __init__(self, pizza, elimina_callback, parent=None):
        super(VistaPizza, self).__init__(parent)
        self.controllore = ControllorePizza(pizza)
        self.controller = ControlloreListaMaterie()
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        h_layout = QHBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        h_layout.addLayout(self.info_layout)

        btn_layout = QVBoxLayout()
        update_btn = QPushButton("Modifica")
        update_btn.clicked.connect(self.show_update_pizza)
        btn_layout.addWidget(update_btn)

        delete_btn = QPushButton("Elimina")
        delete_btn.clicked.connect(self.show_delete_pizza)
        btn_layout.addWidget(delete_btn)
        h_layout.addLayout(btn_layout)
        v_layout.addLayout(h_layout)

        add_layout = QHBoxLayout()
        materia_name = QListWidget()
        for ingrediente in self.controller.get_lista_materie():
            materia = QListWidgetItem(ingrediente.nome)
            materia_name.addItem(materia)
        materia_name.setSelectionMode(QAbstractItemView.SingleSelection)
        add_layout.addWidget(materia_name)
        quantita = QLineEdit()
        quantita.setPlaceholderText("Quantità")
        add_layout.addWidget(quantita)
        add_btn = QPushButton("Aggiungi")
        add_btn.clicked.connect(lambda: self.add_ingrediente(materia_name.selectedItems(), quantita.text()))
        add_layout.addWidget(add_btn)
        v_layout.addLayout(add_layout)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Pizza " + self.controllore.get_nome_pizza())

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.info_layout.addWidget(QLabel(self.controllore.get_nome_pizza()))
        self.info_layout.addWidget(QLabel("Prezzo: " + self.controllore.get_prezzo_pizza() + '€'))
        self.info_layout.addWidget(QLabel("Ingredienti:"))
        if self.controllore.get_ingredienti_pizza():
            for ingrediente in self.controllore.get_ingredienti_pizza():
                if ingrediente[1]!='':
                    self.info_layout.addWidget(QLabel(ingrediente[0].nome + " " + ingrediente[1]))

    def show_update_pizza(self):
        self.vista_modifica_pizza = VistaModificaPizza(self.controllore.model,
                                                       self.controllore.update_prezzo_pizza,
                                                       self.controllore.update_ingrediente,
                                                       self.controllore.delete_ingrediente, self.update_ui)
        self.vista_modifica_pizza.show()

    def show_delete_pizza(self):
        self.vista_elimina_pizza = VistaEliminaPizza(self.controllore.model, self.controllore.delete_pizza,
                                                     self.close)
        self.vista_elimina_pizza.show()
        self.close()

    def add_ingrediente(self, materia, quantita):
        self.controllore.add_ingrediente(self.controller.get_materia_by_nome(materia[0].text()), quantita)
        self.controllore.save_data()
        self.update_ui()
