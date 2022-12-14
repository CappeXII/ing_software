import pickle
import os.path

from listaordini.model.ListaOrdini import ListaOrdini


class ControlloreListaOrdini:
    def __init__(self):
        super(ControlloreListaOrdini, self).__init__()
        self.model = ListaOrdini()
        if os.path.isfile('listaordini/data/lista_ordini_salvata.pickle'):
            with open('listaordini/data/lista_ordini_salvata.pickle', 'rb') as f:
                lista_ordini_salvata = pickle.load(f)
            self.model = lista_ordini_salvata

    def aggiungi_ordine(self, ordine):
        self.model.add_ordine(ordine)
        with open('listaordini/data/lista_ordini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)

    def get_ordine_by_numero(self, num):
        return self.model.get_ordine_by_numero(num)

    def get_lista_ordini(self):
        return self.model.get_lista_ordini()

    def save_data(self):
        with open('listaordini/data/lista_ordini_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
