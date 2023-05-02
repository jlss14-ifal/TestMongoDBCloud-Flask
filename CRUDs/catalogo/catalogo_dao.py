
from catalogo.catalogo import Catalogo

from bson import ObjectId

class CatalogoDAO:
    def __init__(self, conexao):
        self.conexao = conexao
        self.db      = self.conexao.db['catalogos']

    def listar(self) -> dict[str, Catalogo]:
        catalogos = {}
        for documento in self.db.find():
            catalogos[documento._id] = Catalogo(documento.titulo, documento.descricao, documento.criado_em, id = documento._id)
        return catalogos

    def consultar(self, catalogo_id) -> Catalogo:
        documento = self.db.find({"_id": ObjectId(catalogo_id)})
        return Catalogo(documento.titulo, documento.descricao, documento.criado_em, id = documento._id)

    def salvar(self, catalogo):
        resultado = self.db.insert_one(catalogo.to_dict())
        if (resultado):
            return resultado.inserted_id()
        else:
            print("Ocorreu um erro ao tentar salvar!")

    def deletar(self, catalogo_id):
        resultado = self.db.delete_one({"_id": ObjectId(catalogo_id)})
        return resultado.deleted_count # Deve ser 1