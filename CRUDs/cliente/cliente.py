
class Cliente:

    def __init__(self, nome, email, id = None):
        self.id    = id
        self.nome  = nome
        self.email = email

    def to_dict(self):
        return {
            "nome" : self.nome,
            "email": self.email
        }