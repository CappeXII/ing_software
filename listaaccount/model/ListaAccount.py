class ListaAccount:
    def __init__(self):
        super(ListaAccount, self).__init__()
        self.lista_account = []

    def add_account(self, account):
        for search in self.lista_account:
            if account.codice_fiscale == search.codice_fiscale:
                return False
        self.lista_account.append(account)
        return True

    def get_lista_account(self):
        return self.lista_account

    def get_account_by_codice_fiscale(self, codice):
        for account in self.lista_account:
            if account.codice_fiscale == codice:
                return account
