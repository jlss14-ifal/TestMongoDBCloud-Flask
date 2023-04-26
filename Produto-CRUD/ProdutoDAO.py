from unittest import result
from MongoDBConnection import mongoDBConnection

class ProdutoDAO:

    conexao = mongoDBConnection()

    def salvar_produto(self, nome, preco,descricao, comentario):
        produto = {'nome': nome,'preco': preco,'descricao':descricao, 'comentario': comentario}
        result = self.conexao.produto.insert_one(produto)
        return result.inserted_id

    def consultar_produto(id):
        produto = conexao.produto.find_one({"_id": ObjectId(id)})
        return produto

    def atualizar_produto(self,)