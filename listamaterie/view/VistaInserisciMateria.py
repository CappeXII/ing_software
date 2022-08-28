from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton, QMessageBox

from materia.model.Materia import Materia


class VBoxLayout:
    pass


class VistaInserisciMateria(QWidget):
    def __init__(self, controllore, callback):
        super(VistaInserisciMateria, self).__init__()
        self.controllore = controllore
        self.callback = callback

        v_layout = QVBoxLayout()
        self.nome_text = QLineEdit(self)
        self.nome_text.setPlaceholderText("Nome")
        v_layout.addWidget(self.nome_text)

        self.um_text = QLineEdit(self)
        self.um_text.setPlaceholderText("Unit' di misura")
        v_layout.addWidget(self.um_text)

        add_btn = QPushButton("Inserisci")
        add_btn.clicked.connect(self.inserisci_materia)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle('Insersci Materia')

    def inserisci_materia(self):
        nome = self.nome_text.text()
        um = self.um_text.text()

        if nome == "" or um == "":
            QMessageBox.critical(self, 'Errore', 'Inserire tutte le informazioni', QMessageBox.Ok, QMessageBox.Ok)
        else:
            check = False
            for materia in self.controllore.get_lista_materie():
                if nome == materia.username:
                    check = True
            if check:
                QMessageBox.critical(self, 'Errore', 'Nome già presente', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.controllore.add_materia(Materia(nome, um))
                self.callback()
                self.close()
