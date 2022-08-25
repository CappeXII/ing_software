from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from pizza.controller.ControllorePizza import ControllorePizza

class VistaEliminaPizza(QWidget):
    def __init(self, pizza,elimina_pizza,  elimina_callback, parent=None):
        super(VistaEliminaPizza, self).__init(parent)
        self.controllore = ControllorePizza(pizza)
        self.elimina_pizza = elimina_pizza
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        label = QLabel("Vuoi eliminare la pizza" +pizza.nome+"?")
        font = label.font()
        font.setPointSize(18)
        label.setFont(font)
        v_layout.addWidget(label)

        delete_btn = QPushButton("Elimina")
        delete_btn.clicked.connect(self.elimina_pizza)
        v_layout.addWidget(delete_btn)

        self.setLayout(v_layout)
        self.resize(150, 300)
        self.windowTitle("Elimina pizza")

    def elimina_pizza(self):
        self.elimina_pizza()
        self.elimina_callback()
        self.close()

