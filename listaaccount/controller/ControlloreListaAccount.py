import pickle
import os.path

from listaaccount.model.ListaAccount import ListaAccount


class ControlloreListaAccount:
    def __init__(self):
        super(ControlloreListaAccount, self).__init__()
        self.model = ListaAccount()
        if os.path.isfile('listaaccount/data/lista_account_salvata.pickle'):
            with open('listaaccount/data/lista_account_salvata.pickle', 'rb') as f:
                lista_account_salvata = pickle.load(f)
            self.model = lista_account_salvata

    def add_account(self, account):
        if self.model.add_account(account):
            with open('listaaccount/data/lista_account_salvata.pickle', 'wb') as handle:
                pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
                return True
        else:
            return False

    def get_lista_account(self):
        return self.model.get_lista_account()

    def get_account_by_codice_fiscale(self, codice):
        self.model.get_account_by_codice_fiscale(codice)

    def save_data(self):
        with open('listaaccount/data/lista_account_salvata.pickle', 'wb') as handle:
            pickle.dump(self.model, handle, pickle.HIGHEST_PROTOCOL)
