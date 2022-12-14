from listamaterie.controller.ControlloreListaMaterie import ControlloreListaMaterie
from listamaterie.model.ListaMaterie import ListaMaterie


class ControlloreMateria:
    def __init__(self, materia):
        self.model = materia

    def get_nome_materia(self):
        return self.model.nome

    def get_unita_misura_materia(self):
        return self.model.unita_misura

    def update_nome_materia(self, nome):
        self.model.nome = nome

    def update_unita_misura_materia(self, unita):
        self.model.unita_misura = unita

    def delete_materia(self):
        lista = ControlloreListaMaterie()
        lista_materie = lista.get_lista_materie()
        for materia in lista_materie:
            if materia.nome == self.model.nome:
                lista_materie.remove(materia)
        lista.save_data()

    def save_data(self):
        lista = ControlloreListaMaterie()
        for materia in lista.get_lista_materie():
            if materia.nome == self.get_nome_materia():
                materia.unita_misura= self.get_unita_misura_materia()
        lista.save_data()
