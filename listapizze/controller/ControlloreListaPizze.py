import pickle
import os.path

from listapizze.model.ListaPizze import ListaPizze


class ControlloreListaPizze:
    def __init__(self):
        super(ControlloreListaPizze, self).__init__()
        self.model = ListaPizze()
        if os.path.isfile('listapizze/data/lista_pizze_salvata.pickle'):
            with open('listapizze/data/lista_pizze_salvata.pickle', 'rb') as f:
                lista_pizze_salvata = pickle.load(f)
            self.model = lista_pizze_salvata

    def aggiungi_pizza(self, pizza):
        if self.model.add_pizza(pizza):
            with open('listapizze/data/lista_pizze_salvata.pickle', 'wb') as handle:
                pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
                return True
        return False

    def get_lista_pizze(self):
        return self.model.get_lista_pizze()

    def get_pizza_by_nome(self, nome):
        return self.model.get_pizza_by_nome(nome)

    def save_data(self):
        with open('listapizze/data/lista_pizze_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, not pickle.HIGHEST_PROTOCOL)
