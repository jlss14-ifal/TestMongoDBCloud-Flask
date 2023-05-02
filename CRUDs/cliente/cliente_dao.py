
from cliente.cliente import Cliente

from bson import ObjectId

class ClienteDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.db      = self.conexao.db['clientes']

    def listar(self) -> dict[str, Cliente]:
        clientes = {}
        for documento in self.db.find():
            clientes[documento._id] = Cliente(documento.nome, documento.email, id = documento._id)
        return clientes
    
    def consultar(self, cliente_id) -> Cliente:
        documento = self.db.find({"_id": ObjectId(cliente_id)})
        return Cliente(documento.nome, documento.email, id = documento._id)

    def salvar(self, cliente):
        resultado = self.db.insert_one(cliente.to_dict())
        if (resultado):
            return resultado.inserted_id()
        else:
            print("Ocorreu um erro ao tentar salvar!")

    def deletar(self, cliente_id):
        resultado = self.db.delete_one({"_id": ObjectId(cliente_id)})
        return resultado.deleted_count # Deve ser 1