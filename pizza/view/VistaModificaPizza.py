from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from pizza.controller.ControllorePizza import ControllorePizza
from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie

class VistaModificaPizza(QWidget):
    def __init__(self, pizza, modifica_nome, modifica_prezzo, modifica_ingrediente, elimina_ingrediente, elimina_callback, parent=None):
        super(VistaModificaPizza, self).__init__(parent)
        self.controllore = ControllorePizza(pizza)
        self.modifica_nome = modifica_nome
        self.modifica_prezzo = modifica_prezzo
        self.modifica_ingrediente = modifica_ingrediente
        self.elimina_ingrediente = elimina_ingrediente
        self.elimina_callback = elimina_callback

        self.v_layout = QVBoxLayout()

        nome_box = QHBoxLayout()
        label_nome = QLabel("Nome:")
        self.font = QFont()
        self.font.setPointSize(18)
        label_nome.setFont(self.font)
        nome_box.addWidget(label_nome)
        self.text_nome = QLineEdit()
        self.text_nome.setText(self.controllore.get_nome_pizza())
        nome_box.addWidget(self.text_nome)
        self.v_layout.addLayout(nome_box)

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
            label_ingrediente = QLabel(ingrediente.nome+":")
            label_ingrediente.setFont(self.font)
            ingrediente_box.addWidget(label_ingrediente)
            text_ingrediente = QLineEdit()
            text_ingrediente.setText(self.controllore.get_ingredienti_pizza())
            ingrediente_box.addWidget(text_ingrediente)
            delete_button = QPushButton("Elimina")
            delete_button.clicked.connect(self.elimina_ingrediente(ingrediente))
            ingrediente_box.addWidget(delete_button)
            self.v_layout.addLayout(ingrediente_box)

        update_btn = QPushButton("Modifica")
        update_btn.clicked.connect(self.modifica)

        self.setLayout(self.v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Modifica pizza")

    def modifica(self):
        if(self.text_nome.isModified()):
            self.modifica_nome(self.text_nome.text())
        if(self.text_prezzo.isModified()):
            self.modifica_prezzo(self.text_prezzo.text())
        for i in range (0, self.v_layout.count()):
            if i>=2:
                child = self.v_layout.takeAt(i)
                text_ing = child.takeAt(1)
                text = text_ing.text()
                materia = child.takeAt(0)
                name = materia.text()
                if text.isModified():
                    controller = ControlloreListaMaterie()
                    self.modifica_ingrediente(controller.get_materia_by_nome(name), text.text())

        self.elimina_callback()
        self.close()



