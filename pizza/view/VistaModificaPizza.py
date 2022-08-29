from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from pizza.controller.ControllorePizza import ControllorePizza


class VistaModificaPizza(QWidget):
    def __init__(self, pizza, modifica_prezzo, modifica_ingrediente, elimina_ingrediente,
                 elimina_callback, parent=None):
        super(VistaModificaPizza, self).__init__(parent)
        self.controllore = ControllorePizza(pizza)
        self.controller = ControlloreListaMaterie()
        self.modifica_prezzo = modifica_prezzo
        self.modifica_ingrediente = modifica_ingrediente
        self.elimina_ingrediente = elimina_ingrediente
        self.elimina_callback = elimina_callback
        self.lista_ingredienti = []
        self.index = 0

        self.v_layout = QVBoxLayout()


        self.font = QFont()
        self.font.setPointSize(18)

        prezzo_box = QHBoxLayout()
        label_prezzo = QLabel("Prezzo:")
        label_prezzo.setFont(self.font)
        prezzo_box.addWidget(label_prezzo)
        self.text_prezzo = QLineEdit()
        self.text_prezzo.setText(self.controllore.get_prezzo_pizza())
        prezzo_box.addWidget(self.text_prezzo)
        self.v_layout.addLayout(prezzo_box)

        for ingrediente in self.controllore.get_ingredienti_pizza():
            ingrediente_box = QHBoxLayout()
            label_ingrediente = QLabel(ingrediente[0].nome + ":")
            label_ingrediente.setFont(self.font)
            ingrediente_box.addWidget(label_ingrediente)
            text_ingrediente = QLineEdit()
            text_ingrediente.setText(ingrediente[1])
            text_ingrediente.setPlaceholderText(ingrediente[0].nome)
            self.lista_ingredienti.append(text_ingrediente)
            ingrediente_box.addWidget(self.lista_ingredienti[self.index])
            delete_button = QPushButton("Elimina")
            delete_button.clicked.connect(lambda: self.elimina(self.index))
            ingrediente_box.addWidget(delete_button)
            self.v_layout.addLayout(ingrediente_box)
            self.index += 1

        update_btn = QPushButton("Modifica")
        update_btn.clicked.connect(self.modifica)
        self.v_layout.addWidget(update_btn)

        self.setLayout(self.v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Modifica pizza")

    def modifica(self):
        if self.text_prezzo.isModified():
            self.modifica_prezzo(self.text_prezzo.text())
        for ingrediente in self.lista_ingredienti:
            if ingrediente.isModified():
                self.modifica_ingrediente(self.controller.get_materia_by_nome(ingrediente.placeholderText()),
                                          ingrediente.text())
        self.controllore.save_data()
        self.elimina_callback()
        self.close()

    def elimina(self, index):
        self.elimina_ingrediente(self.controller.get_materia_by_nome(self.lista_ingredienti[index].placeholderText()))
        self.controllore.save_data()
        self.elimina_callback()
        self.close()


