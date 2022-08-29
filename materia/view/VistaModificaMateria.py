from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QLineEdit

from materia.controller.ControlloreMateria import ControlloreMateria


class VistaModificaMateria(QWidget):
    def __init__(self, account, modifica_nome, modifica_um, elimina_callback):
        super(VistaModificaMateria, self).__init__()
        self.controller = ControlloreMateria(account)
        self.modifica_nome = modifica_nome
        self.modifca_um = modifica_um
        self.elimina_callback = elimina_callback

        v_layout = QVBoxLayout()

        h_layout2 = QHBoxLayout()
        label_um = QLabel("Unita' di misura:")
        font_um = label_um.font()
        font_um.setPointSize(17)
        label_um.setFont(font_um)
        h_layout2.addWidget(label_um)

        self.text_um = QLineEdit()
        self.text_um.setText(self.controller.get_unita_misura_materia())
        h_layout2.addWidget(self.text_um)

        v_layout.addLayout(h_layout2)
        v_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        update_btn = QPushButton("Modifica")
        update_btn.clicked.connect(self.modifica)
        v_layout.addWidget(update_btn)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Modifica account')

    def modifica(self):

        if self.text_um.isModified():
            self.modifca_um(self.text_um.text())
        self.controller.save_data()
        self.elimina_callback()
        self.close()
