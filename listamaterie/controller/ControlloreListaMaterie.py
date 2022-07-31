import pickle
import os.path

from listamaterie.model.ListaMaterie import ListaMaterie
class ControlloreListaMaterie():
    def __init__(self):
        super(ControlloreListaMaterie, self).__init__()
        self.model = ListaMaterie()
        if os.path.isfile('listamaterie/data/lista_materie_salvata'):
            with open('listamaterie/data/lista_materie_salvata', 'rb') as f:
                lista_materie_salvata = pickle.load(f)
            self.model = lista_materie_salvata

    def add_materia(self, materia):
        if self.model.add_materia(materia):
            with open('listamaterie/data/lista_materie_salvata', 'wb') as handle:
                pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
            return True
        return False

    def get_lista_materie(self):
        return self.model.get_lista_materie()

    def get_materia_by_nome(self, nome):
        return self.model.get_materia_by_nome(nome)

    def save_data(self):
        with open('listamaterie/data/lista_materie_salvata', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)