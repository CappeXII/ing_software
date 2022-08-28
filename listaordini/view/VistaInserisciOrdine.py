from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from ordini.model.Ordine import Ordine


class VistaInserisciOrdine(QWidget):
    def __init__(self, controllore, callback, parent=None):
        super(VistaInserisciOrdine, self).__init__(parent)
        self.controllore = controllore
        self.callback = callback
        self.numero = 0
        v_layout = QVBoxLayout()
        for ordine in controllore.get_lista_ordini():
            if ordine.numero > self.numero:
                self.numero = ordine.numero
        self.numero += 1
        label_numero = QLabel("Numero previsto: " + self.numero)
        font = label_numero.font()
        font.setPointSize(18)
        label_numero.setFont(font)
        v_layout.addWidget(label_numero)
        add_btn = QPushButton("Aggiungi un nuovo ordine")
        add_btn.clicked.connect(self.aggiungi_ordine())
        v_layout.addWidget(add_btn)
        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("Inserisci Ordine")

    def aggiungi_ordine(self):
        self.controllore.add_ordine(Ordine(self.numero))
        self.callback()
        self.close()
