class Ordine():
    def __init(self, numero):
        super(Ordine, self).__init()
        self.numero = numero
        self.pizze = []

    def add_pizza(self, pizza, numero):
        for pasto in self.pizze:
            if pasto[0].nome == pizza.nome:
                return False
        self.pizze.append([pizza, numero])
        return True



    