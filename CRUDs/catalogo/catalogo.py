
class Catalogo:
    def __init__(self, titulo, descricao, criado_em, id = None):
        self.id        = id
        self.titulo    = titulo
        self.descricao = descricao
        self.criado_em = criado_em

    def to_dict(self):
        return {
            "titulo"   : self.titulo,
            "descricao": self.descricao,
            "criado_em": self.criado_em
        }