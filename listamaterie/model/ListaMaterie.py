class ListaMaterie():
    def __init__(self):
        self.lista_materie = []

    def add_materia(self, materia):
        for materie in self.lista_materie:
            if materia.nome == materie.nome:
                return False
        self.lista_materie.append(materia)
        return True

    def get_lista_materie(self):
        return self.lista_materie

    def get_materia_by_nome(self, nome):
        for materie in self.lista_materie:
            if materie.nome == nome:
                return materie
