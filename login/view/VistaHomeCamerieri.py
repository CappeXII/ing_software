from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from listaordini.view.VistaListaOrdini import VistaListaOrdini


class VistaHomeCamerieri(QWidget):
    def __init__(self):
        super(VistaHomeCamerieri, self).__init__()
        v_layout = QVBoxLayout()
        ordini_btn = QPushButton("Ordini")
        ordini_btn.clicked.connect(self.go_vista_lista_ordini)
        v_layout.addWidget(ordini_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Home Camerieri")

    def go_vista_lista_ordini(self):
        self.vista_lista_ordini = VistaListaOrdini()
        self.vista_lista_ordini.show()
