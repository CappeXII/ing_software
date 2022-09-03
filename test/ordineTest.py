import unittest
from ordini.controller.ControlloreOrdine import ControlloreOrdine
from listaordini.controller.ControlloreListaOrdini import ControlloreListaOrdini


class ordineTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.controlloreLista = ControlloreListaOrdini()
        self.index = 0
        for ordine in self.controlloreLista.get_lista_ordini():
            self.index = ordine.numero
        self.controllore = ControlloreOrdine(self.controlloreLista.get_ordine_by_numero(self.index))

    def elimina_test(self):
        self.controllore.delete_ordine()
        assert (self.controlloreLista.get_ordine_by_numero(self.index) is None)
