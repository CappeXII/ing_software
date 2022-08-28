from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QPushButton, QHBoxLayout, QLabel

from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from listamaterie.view.VistaInserisciMateria import VistaInserisciMateria
from materia.view.VistaMateria import VistaMateria


class VistaListaMateria(QWidget):
    def __init__(self, parent=None):
        super(VistaListaMateria, self).__init__(parent)

        v_layout = QVBoxLayout()
        self.controllore = ControlloreListaMaterie()
        self.info_layout = QVBoxLayout()
        self.update_ui()
        v_layout.addLayout(self.info_layout)

        v_layout.addWIdget(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        insert_button = QPushButton("Inserisci una nuova materia")
        insert_button.clicked.connect(self.show_add_materia)
        v_layout.addWidget(insert_button)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Lista Materie')


    def update_ui(self):
        while self.info_layout.count():
            child = self.info_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        for materia in self.controllore.get_lista_materie():
            h_box = QHBoxLayout()
            label = QLabel(materia.nome)
            font = label.font()
            font.setPointSize(18)
            label.setFont(font)
            h_box.addWidget(label)

            open_btn = QPushButton("Apri")
            open_btn.clicked.connect(self.show_selected_info(materia))
            h_box.addWidget(open_btn)
            self.info_layout.addLayout(h_box)



    def show_selected_info(self, materia):
        self.vista_materia = VistaMateria(materia, self.update_ui)
        self.vista_materia.show()

    def show_add_materia(self):
        self.vista_inserisci_materia = VistaInserisciMateria(self.controllore, self.update_ui)
        self.vista_inserisci_materia.show()
