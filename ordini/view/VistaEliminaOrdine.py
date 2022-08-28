from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from ordini.controller.ControlloreOrdine import ControlloreOrdine


class VistaEliminaOrdine(QWidget):
    def __init__(self, ordine,elimina_ordine,  elimina_callback, parent=None):
        super(VistaEliminaOrdine, self).__init__(parent)
        self.controllore = ControlloreOrdine(ordine)
        self.elimina_ordine = elimina_ordine
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()
        label = QLabel("Vuoi eliminare la ordine" +ordine.numero+"?")
        font = label.font()
        font.setPointSize(18)
        label.setFont(font)
        v_layout.addWidget(label)

        delete_btn = QPushButton("Elimina")
        delete_btn.clicked.connect(self.elimina_ordine)
        v_layout.addWidget(delete_btn)

        self.setLayout(v_layout)
        self.resize(150, 300)
        self.setWindowTitle("Elimina ordine")

    def elimina_ordine(self):
        self.elimina_ordine()
        self.elimina_callback()
        self.close()

