from pymongo import MongoClient
from urllib.parse import quote_plus
import ssl

class ConexaoMongoDB:
    def __init__(self, username, password, cluster):
        self.nome_usuario = quote_plus(username)
        self.senha        = quote_plus(password)
        self.cluster      = cluster
        self.cliente      = None

    def conectar(self):
        uri          = 'mongodb+srv://' + self.nome_usuario + ':' + self.senha + '@' + self.cluster + '/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
        self.cliente = MongoClient(uri)
        self.db      = self.cliente["Catalogo_de_produtos"] # Acessa a collection "Catalogo_de_produtos" que contem todas as tabelas

    def desconectar(self):
        self.cliente.close()

    def encontrar(self, db_nome, coluna_nome):
        resultado = self.cliente[db_nome][coluna_nome].find()
        return resultado
