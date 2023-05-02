from unittest import result
from conexao_comentarios import ConexãoComentarios
from bson import ObjectId

#conexao = ConexãoComentarios()
class Comentarios:

    def __init__(self, conexao):
        self.comentarios = conexao.db['comentarios']

    def salvar_comentario(self, conteudo, usuario_id,catalogo_id,nome_usuario,criado_em):
        comentario = {'conteudo': conteudo,'usuario_id': usuario_id,'catalogo_id': catalogo_id, 'nome_usuario': nome_usuario ,'criado_em':criado_em}
        comentario = self.comentarios.insert_one(comentario)
        return comentario
    
    def consultar_comentario(self, id):
        comentario = self.comentarios.find_one({"_id": ObjectId(id)})
        return comentario
    
    def atualizar_comentario(self, conteudo, usuario_id,catalogo_id,nome_usuario,criado_em,id):
        comentario = {'conteudo': conteudo,'usuario_id': usuario_id,'catalogo_id': catalogo_id, 'nome_usuario': nome_usuario , 'criado_em':criado_em}
        comentario = self.comentarios.find_one_and_update({"_id": ObjectId(id)},{"$set": comentario},)
        return comentario
    
    def deletar_comentario(self, id):
        comentario = self.comentarios.find_one_and_delete({"_id": ObjectId(id)})
        return comentario

    
