from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QMessageBox

from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from pizza.model.Pizza import Pizza


class VistaInserisciPizza(QWidget):
    def __init__(self, controllore, callback, parent=None):
        super(VistaInserisciPizza, self).__init__(parent)
        self.controllore = controllore
        self.callback = callback
        self.ingredienti = ControlloreListaMaterie()

        v_layout = QVBoxLayout()
        self.nome_text = QLineEdit()
        self.nome_text.setPlaceholderText("Nome")
        v_layout.addWidget(self.nome_text)

        self.prezzo_text = QLineEdit()
        self.prezzo_text.setPlaceholderText("Prezzo")
        v_layout.addWidget(self.prezzo_text)

        self.setLayout(v_layout)
        self.resize(600, 300)
        self.setWindowTitle("InserisciPizza")

    def aggiungi_pizza(self):
        nome = self.nome_text.text()
        prezzo = self.prezzo_text.text()
        if nome == "" or prezzo == "":
            QMessageBox.critical(self, 'Errore', 'Inserire tutti i parametri richiesti', QMessageBox.Ok, QMessageBox.Ok)
        else:
            try:
                float(prezzo)
                self.controllore.add_pizza(Pizza(nome, prezzo))
                self.callback()
                self.close()
            except ValueError:
                QMessageBox.critical(self, 'Errore', 'Errore formato prezzo (XX.XX)', QMessageBox.Ok, QMessageBox.Ok)
