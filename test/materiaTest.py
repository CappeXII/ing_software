import unittest
from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from materia.controller.ControlloreMateria import ControlloreMateria
from materia.model.Materia import Materia


class materiaTest(unittest.TestCase):
    def __init__(self):
        super(materiaTest, self).__init__()
        self.controllorelista = ControlloreListaMaterie()
        self.key = 0
        for materia in self.controllorelista.get_lista_materie():
            self.key = materia.nome
        self.controlloremateria = ControlloreMateria(self.controllorelista.get_materia_by_nome(self.key))

    def modificaTest(self):
        self.controlloremateria.update_unita_misura_materia("lt")
        assert(self.controlloremateria.__eq__(Materia(self.key, "lt")))

    def eliminaTest(self):
        self.controlloremateria.delete_materia()
        assert(self.controllorelista.get_materia_by_nome(self.key) is None)
