from pymongo import MongoClient
      
class ConexãoComentarios:
        mongoURL = MongoClient('mongodb+srv://vinicius:12345@cluster0.ybfirvh.mongodb.net/banco')
        db = mongoURL['banco']
        comentarios = db['comentarios']
        
        