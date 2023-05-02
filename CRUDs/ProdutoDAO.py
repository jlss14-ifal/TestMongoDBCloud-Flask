from unittest import result
from MongoDBConnection import mongoDBConnection
from Produto import Produto
from bson.objectid import ObjectId

class ProdutoDAO:

    def __init__(self, conexao):
        self.produtos = conexao.db['produtos']

    def salvar_produto(self, Produto):
        
        produto = {'nome': Produto.nome,'preco': Produto.preco,'descricao': Produto.descricao, 'avaliacao': Produto.avaliacao}
        result = self.produtos.insert_one(produto)
        return result.inserted_id
        print("Produto salvo!!")    

    def consultar_produto(self,id):
        produto = self.produtos.find_one({'_id': ObjectId(id)})
        return produto

    def atualizar_produto(self, novo_nome, novo_preco,nova_descricao, nova_avaliacao,id_produto):
        produto = self.produtos.update_one({'_id':ObjectId(id_produto)}, {'$set':{'nome':novo_nome,'preco':novo_preco,'descricao':nova_descricao,'avaliacao':nova_avaliacao}})
        print("Produto atualizado!!")
        return produto
    def deletar_produto(self,id):
         produto = self.produtos.delete_one({'_id': ObjectId(id)})
         print("Produto deletado!!")
         return produto

