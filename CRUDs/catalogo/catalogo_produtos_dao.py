
from conexao.conexao_mongodb    import ConexaoMongoDB
from catalogo.catalogo_produtos import CatalogoProdutos

from bson import ObjectId

class CatalogoProdutosDAO:
    def __init__(self, conexao: ConexaoMongoDB):
        self.conexao = conexao
        self.db      = self.conexao.db['catalogos_produtos']

    def listar(self, catalogo_id) -> dict[str, CatalogoProdutos]:
        catalogos_produtos = {}
        for documento in self.db.find({"catalogo_id": catalogo_id}):
            catalogos_produtos[documento._id] = CatalogoProdutos(documento.catalogo_id, documento.catalogo_titulo, documento.produto_id, documento.produto_nome, documento.produto_preco)
        return catalogos_produtos
    
    def salvar(self, catalogo_produtos: CatalogoProdutos):
        resultado = self.db.insert_one(catalogo_produtos.to_dict())
        if (resultado):
            return resultado.inserted_id()
        else:
            print("Ocorreu um erro ao tentar salvar!")

    def deletar(self, catalogo_id):
        # Deve deletar de acordo com o id do catalogo
        resultado = self.db.delete_many({"_id": ObjectId(catalogo_id)})
        return resultado.deleted_count # Deve ser 1 ou mais
