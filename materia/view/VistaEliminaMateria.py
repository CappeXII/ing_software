from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QPushButton

from materia.controller.ControlloreMateria import ControlloreMateria


class VistaEliminaMateria(QWidget):
    def __init__(self, materia, elimina_materia, elimina_callback):
        super(VistaEliminaMateria, self).__init__()
        self.controllore = ControlloreMateria(materia)
        self.elimina_materia = elimina_materia
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        label_nome = QLabel("Vuoi eliminare la materia" + self.controllore.get_nome_materia() + "?")
        font_nome = label_nome.font()
        font_nome.setPointSize(30)
        label_nome.setFont(font_nome)
        v_layout.addWidget(label_nome)

        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        btn_elimina = QPushButton("Elimina")
        btn_elimina.clicked.connect(self.elimina_materia)
        v_layout.addWidget(btn_elimina)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Eliminazione materia')

    def elimina_materia(self):
        self.elimina_materia()
        self.elimina_callback()
        self.close()
