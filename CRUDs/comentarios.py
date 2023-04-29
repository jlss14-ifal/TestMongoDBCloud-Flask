from unittest import result
from conexao_comentarios import ConexãoComentarios
from bson import ObjectId

conexao = ConexãoComentarios()
class Comentarios:

    def salvar_comentario(conteudo, usuario_id,nome_usuario,criado_em):
        comentario = {'conteudo': conteudo,'usuario_id': usuario_id, 'nome_usuario': nome_usuario ,'criado_em':criado_em}
        comentario = conexao.comentarios.insert_one(comentario)
        return comentario
    
    def consultar_comentario(id):
        comentario = conexao.comentarios.find_one({"_id": ObjectId(id)})
        return comentario
    
    def atualizar_comentario(conteudo, usuario_id,nome_usuario,criado_em,id):
        comentario = {'conteudo': conteudo,'usuario_id': usuario_id, 'nome_usuario': nome_usuario , 'criado_em':criado_em}
        comentario = conexao.comentarios.find_one_and_update({"_id": ObjectId(id)},{"$set": comentario},)
        return comentario
    
    def deletar_comentario(id):
        comentario = conexao.comentarios.find_one_and_delete({"_id": ObjectId(id)})
        return comentario

    
