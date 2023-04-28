from pymongo import MongoClient

class mongoDBConnection:
    def __init__(self):
        self.cliente = MongoClient('mongodb+srv://lmsl:lmsl12345@cluster0.2wxo5df.mongodb.net/Teste-python?retryWrites=true&w=majority')
        self.db = self.cliente['Teste-python']
        self.produtos = self.db['produtos']
        self.cliente.close()
