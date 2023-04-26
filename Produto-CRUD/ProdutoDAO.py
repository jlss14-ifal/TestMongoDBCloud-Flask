from unittest import result
from MongoDBConnection import mongoDBConnection

class ProdutoDAO:

    conexao = mongoDBConnection()

    def salvar_produto(self, nome, preco,descricao, avaliacao):
        produto = {'nome': nome,'preco': preco,'descricao':descricao, 'comentario': avaliacao}
        result = self.conexao.produto.insert_one(produto)
        return result.inserted_id

    def consultar_produto(self,id):
        produto = self.conexao.produto.find_one({"_id": ObjectId(id)})
        return produto

    def atualizar_produto(self,):

