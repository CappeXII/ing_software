import unittest
from listaaccount.controller.ControlloreListaAccount import ControlloreListaAccount
from account.controller.ControlloreAccount import ControlloreAccount
from account.model.Account import Account


class accountTest(unittest.TestCase):
    def __init__(self):
        super(accountTest, self).__init__()
        self.controllorelista = ControlloreListaAccount()
        self.key = 0
        for account in self.controllorelista.get_lista_account():
            self.key = account.username
        self.controlloreaccount = ControlloreAccount(self.controllorelista.get_account_by_username(self.key))

    def modificaTest(self):
        self.controlloreaccount.update_nome_account("Giuseppe")
        self.controlloreaccount.update_cognome_account("Verdi")
        self.controlloreaccount.update_password_account("verdi")
        self.controlloreaccount.update_codice_fiscale_account("GPP11PP")
        assert self.controlloreaccount.model.__eq__(Account("Giuseppe", "Verdi", "GPP11PP", self.key, "verdi",
                                                            self.controlloreaccount.account_is_admin()))

    def eliminaTest(self):
        self.controlloreaccount.delete_account()
        assert self.controllorelista.get_account_by_username(self.key) is None
