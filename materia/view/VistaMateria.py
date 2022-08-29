from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

from materia.controller.ControlloreMateria import ControlloreMateria
from materia.view.VistaEliminaMateria import VistaEliminaMateria
from materia.view.VistaModificaMateria import VistaModificaMateria


class VistaMateria(QWidget):
    def __init__(self, materia, elimina_callback, parent=None):
        super(VistaMateria, self).__init__(parent)
        self.controllore = ControlloreMateria(materia)
        self.elimina_callback = elimina_callback
        h_layout = QHBoxLayout()

        self.info_layout = QVBoxLayout()
        self.update_ui()
        h_layout.addLayout(self.info_layout)

        button_layouts = QVBoxLayout()
        update_button = QPushButton("Modifica")
        update_button.clicked.connect(self.show_update_materia)
        button_layouts.addWidget(update_button)

        delete_button = QPushButton("Elimina")
        delete_button.clicked.connect(self.show_delete_materia)
        button_layouts.addWidget(delete_button)
        h_layout.addLayout(button_layouts)

        self.setLayout(h_layout)
        self.resize(600, 300)
        self.setWindowTitle('Materia ' + self.controllore.get_nome_materia())

    def show_update_materia(self):
        self.vista_modifica = VistaModificaMateria(self.controllore.model, self.controllore.update_nome_materia,
                                                   self.controllore.update_unita_misura_materia, self.update_ui)
        self.vista_modifica.show()

    def show_delete_materia(self):
        self.vista_elimina = VistaEliminaMateria(self.controllore.model, self.controllore.delete_materia,
                                                 self.close)
        self.vista_elimina.show()
        self.close()

    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        label_nome = QLabel("Nome: " + self.controllore.get_nome_materia())
        font_nome = label_nome.font()
        font_nome.setPointSize(17)
        label_nome.setFont(font_nome)
        self.info_layout.addWidget(label_nome)

        label_um = QLabel("Unita misura: " + self.controllore.get_unita_misura_materia())
        font_um = label_um.font()
        font_um.setPointSize(17)
        label_um.setFont(font_nome)
        self.info_layout.addWidget(label_um)
