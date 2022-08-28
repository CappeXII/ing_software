from listaordini.model.ListaOrdini import ListaOrdini


class ControlloreOrdine:
    def __init__(self, ordine):
        self.model = ordine

    def get_numero(self):
        return self.model.numero

    def get_pizze(self):
        return self.model.pizze

    def add_pizza(self, pizza, num):
        return self.model.add_pizza(pizza, num)

    def delete_ordine(self):
        lista = ListaOrdini()
        lista_ordini = lista.get_lista_ordini()
        for ordine in lista_ordini:
            if ordine.numero == self.model.numero:
                lista_ordini.remove(ordine)
                return True
        return False
