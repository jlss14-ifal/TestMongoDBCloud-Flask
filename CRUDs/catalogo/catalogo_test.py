
from conexao.conexao_mongodb import ConexaoMongoDB

from Produto import Produto

from catalogo.catalogo              import Catalogo
from catalogo.catalogo_dao          import CatalogoDAO
from catalogo.catalogo_produtos     import CatalogoProdutos
from catalogo.catalogo_produtos_dao import CatalogoProdutosDAO

from datetime import datetime

class CatalogoTest:

    def __init__(self, conexao: ConexaoMongoDB):
        self.catalogos          = CatalogoDAO(conexao)
        self.catalogos_produtos = CatalogoProdutosDAO(conexao)

    def listarCatalgos(self):
        print("Catalogos cadastrados:")
        for catalogo in self.catalogos.listar().items():
            print(catalogo.to_dict())
        print("\n")

    def consultarCatalogo(self, catalogo_id):
        print("---------------Ofertas desse catalogo:---------------")
        for ofertas in self.catalogos_produtos.listar(catalogo_id).items():
            print(ofertas.to_dict())
        print("-----------------------------------------------------\n")

    def cadastrarCatalogo(self):
        print("Cadastrar novo catalogo: ")

        titulo    = input("Titulo do catalogo: ")
        descricao = input('Descricao: ')
        criado_em = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        self.catalogos.salvar(Catalogo(titulo, descricao, criado_em))
        
        print("Salvo com sucesso!\n")

    def preencherCatalogo(self):
        print("Adicionar produtos ao catalogo: ")
        
        catalogo_id     = input("Id do catalogo: ")
        catalogo        = CatalogoDAO(self.conexao).consultar(catalogo_id)
        catalogo_titulo = catalogo.titulo
        
        continuar = 1
        while (continuar != 0):
            print("[1] - Adicionar novo produto ao catalogo;")
            print("[0] - Sair da adicao de produtos ao catalogo;")
            
            continuar = int(input("Opcao: "))

            if (continuar == 1):
                produto_id    = input("Id do produto: ")
                produto       = Produto("produto1", 66, "descricao", 5) # Aqui seria uma consultado produto, esse eh so um exemplo para teste
                produto_nome  = produto.nome
                produto_preco = produto.preco
                self.catalogos_produtos.salvar(CatalogoProdutos(catalogo_id, catalogo_titulo, produto_id, produto_nome, produto_preco))
                print("Produto adicionado com sucesso!\n")

    def deletarCatalogo(self, catalogo_id):
        self.catalogos         .deletar(catalogo_id) # Deleta o catalogo
        self.catalogos_produtos.deletar(catalogo_id) # Deleta os produtos associados
        print("\n")