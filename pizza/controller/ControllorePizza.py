from listapizze.model.ListaPizze import ListaPizze

class ControllorePizza():
    def __init__(self, pizza):
        self.model = pizza

    def get_nome_pizza(self):
        return self.model.nome

    def get_prezzo_pizza(self):
        return self.model.prezzo

    def get_ingredient_pizza(self):
        return self.model.ingredienti

    def update_nome_pizza(self, nome):
        self.model.nome = nome

    def update_prezzo_pizza(self, prezzo):
        self.model.prezzo = prezzo

    def delete_pizza(self):
        lista = ListaPizze()
        lista_pizze = lista.get_lista_pizze()
        for pizza in lista_pizze:
            if pizza.nome == self.model.nome:
                lista_pizze.remove(pizza)
                return True
        return False

    def add_ingrediente(self, materia, q):
        return self.model.add_ingrediente(materia, q)

    def update_ingrediente(self, materia, q):
        return self.model.update_ingrediente(materia, q)

    def delete_ingrediente(self, materia):
        return self.model.delete_ingrediente(materia)



