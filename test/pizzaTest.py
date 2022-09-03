import unittest
from listapizze.controller.ControlloreListaPizze import ControlloreListaPizze
from pizza.controller.ControllorePizza import ControllorePizza
from pizza.model.Pizza import Pizza


class pizzaTest(unittest.TestCase):
    def __init__(self):
        super(pizzaTest, self).__init__()
        self.controllorelista = ControlloreListaPizze()
        self.key = 0
        for pizza in self.controllorelista.get_lista_pizze():
            self.key = pizza.nome
        self.controllorepizza = ControllorePizza(self.controllorelista.get_pizza_by_nome(self.key))

    def modificaTest(self):
        self.controllorepizza.update_prezzo_pizza(15.50)
        assert self.controllorepizza.model.__eq__(Pizza(self.key, 15.50))

    def eliminaTest(self):
        self.controllorepizza.delete_pizza()
        assert self.controllorelista.get_pizza_by_nome(self.key) is None
