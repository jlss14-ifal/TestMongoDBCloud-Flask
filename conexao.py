from pymongo import MongoClient
      
class mongoDBConnection:
        mongoURL = MongoClient('mongodb+srv://lmsl:lmsl12345@cluster0.2wxo5df.mongodb.net/Teste-python?retryWrites=true&w=majority')
        db = mongoURL['database']
        comentarios = db['comentarios']
        
        