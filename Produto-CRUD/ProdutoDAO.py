from unittest import result
from MongoDBConnection import mongoDBConnection

class ProdutoDAO:

    conexao = mongoDBConnection()

    def salvar_produto(self, nome, preco, comentario):
        produto = {'nome': nome,'preco': preco, 'comentario': comentario}
        result = self.conexao.produto.insert_one(produto)
        return result.inserted_id