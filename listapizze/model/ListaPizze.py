class ListaPizze:
    def __init__(self):
        super(ListaPizze, self).__init__()
        self.lista_pizze = []

    def add_pizza(self, pizza):
        for search in self.lista_pizze:
            if search.nome == pizza.nome:
                return False
        self.lista_pizze.append(pizza)
        return True

    def get_pizza_by_nome(self, nome):
        for search in self.lista_pizze:
            if search.nome == nome:
                return search

    def get_lista_pizze(self):
        return self.lista_pizze
