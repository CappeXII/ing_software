class Pizza():
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
        self.ingredienti = []

    def __eq__(self, obj):
        if isinstance(obj, Pizza):
            return self.nome == obj.nome and self.prezzo == obj.prezzo and self.ingredienti == obj.ingredienti
        return False

    def add_ingrediente(self, materia, q):
        for ingrediente in self.ingredienti:
            if ingrediente[0].__eq__(materia):
                return False
        self.ingredienti.append([materia, q])
        return True

    def update_ingrediente(self, materia, q):
        for ingrediente in self.ingredienti:
            if ingrediente[0].__eq__(materia):
                ingrediente[1] = q
                return True
        return False

    def delete_ingrediente(self, materia):
        for ingrediente in self.ingredienti:
            if ingrediente[0].__eq__(materia):
                self.ingredienti.remove(ingrediente)
                return True
        return False
