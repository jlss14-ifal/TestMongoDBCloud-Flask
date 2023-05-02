
class CatalogoProdutos:
    def __init__(self, catalogo_id, catalogo_titulo, produto_id, produto_nome, produto_preco):
        self.catalogo_id     = catalogo_id
        self.catalogo_titulo = catalogo_titulo
        self.produto_id      = produto_id
        self.produto_nome    = produto_nome
        self.produto_preco   = produto_preco

    def to_dict(self):
        return {
            "catalogo_id"     : self.catalogo_id,
            "catalogo_titulo" : self.catalogo_titulo,
            "produto_id"      : self.produto_id,
            "produto_nome"    : self.produto_nome,
            "produto_preco"   : self.produto_preco
        }