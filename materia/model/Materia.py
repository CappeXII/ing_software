class Materia:
    def __init__(self, nome, unita):
        self.nome = nome
        self.unita_misura = unita

    def __eq__(self, obj):
        if isinstance(obj, Materia):
            return self.nome == obj.nome and self.unita_misura == obj.unita_misura
        return False
