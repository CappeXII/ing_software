class ListaOrdini:
    def __init__(self):
        super(ListaOrdini, self).__init__()
        self.lista_ordini = []

    def add_ordine(self, ordine):
        self.lista_ordini.append(ordine)

    def get_lista_ordini(self):
        return self.lista_ordini

    def get_ordine_by_numero(self, numero):
        for ordine in self.lista_ordini:
            if ordine.numero == numero:
                return ordine
