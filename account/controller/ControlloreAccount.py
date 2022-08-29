from listaaccount.controller.ControlloreListaAccount import ControlloreListaAccount
from listaaccount.model.ListaAccount import ListaAccount
class ControlloreAccount():
    def __init__(self, account):
        super(ControlloreAccount, self).__init__()
        self.model = account

    def get_nome_account(self):
        return self.model.nome

    def get_cognome_account(self):
        return self.model.cognome

    def get_codice_fiscale_account(self):
        return self.model.codice_fiscale

    def get_username_account(self):
        return self.model.username

    def get_password_account(self):
        return self.model.password

    def account_is_admin(self):
        return self.model.isAdmin

    def update_nome_account(self, nome):
        if isinstance(nome, str):
            self.model.nome = nome
            return True
        else:
            return False

    def update_cognome_account(self, cognome):
        if isinstance(cognome, str):
            self.model.cognome = cognome
            return True
        else:
            return False

    def update_codice_fiscale_account(self, codice_fiscale):
        if isinstance(codice_fiscale, str):
            self.model.codice_fiscale = codice_fiscale
            return True
        else:
            return False

    def update_password_account(self, password):
        if isinstance(password, str):
            self.model.password = password
            return True
        else:
            return False

    def delete_account(self):
        lista = ControlloreListaAccount()
        lista_account = lista.get_lista_account()
        for account in lista_account:
            if account.codice_fiscale == self.model.codice_fiscale:
                lista_account.remove(account)
        lista.save_data()

    def save_data(self):
        lista = ControlloreListaAccount()
        for account in lista.get_lista_account():
            if account.username == self.model.username:
                account.nome = self.model.nome
                account.cognome = self.model.cognome
                account.codice_fiscale = self.model.codice_fiscale
                account.password = self.model.password
                account.isAdmin = self.model.isAdmin
        lista.save_data()

