from Produto import Produto
from ProdutoDAO import ProdutoDAO
from comentarios import Comentarios

from conexao.conexao_mongodb import ConexaoMongoDB

from catalogo.catalogo_test import CatalogoTest
from cliente.cliente_test   import ClienteTest

conexao = ConexaoMongoDB("<username>", "<password>", "<cluster>")
conexao.conectar() # Abre conexao

cont = 1

def imprime_e_executa_opcoes(opcoes, opcao_nome):
     opcao_escolhida = -1
     while (opcao_escolhida != 0):
          print(f"Opções de {opcao_nome}:")
          list(map(lambda opcao: print(f"{opcao}"), opcoes.keys()))

          opcao_escolhida = int(input("Digite a sua opção: "))

           # Verifica e retorna todos que comecam com "[opcao]"
          opcoesPrefixo = [opcao for key, opcao in opcoes.items() if key.startswith(f"[{opcao_escolhida}]")]

          if opcoesPrefixo:
               opcoesPrefixo[0]() # Executa a primeira ocorrencia
          else:
               print(f"_______Opcao desconhecida: {opcao_escolhida}_______\n")

while(cont!=0):
    print("[1] - Clientes")
    print("[2] - Catálogos")
    print("[3] - Produtos")
    print("[4] - Comentários")
    print("[0] - Sair")
    cont = int(input("Digite a sua opção: "))

    if (cont == 0):
        conexao.desconectar() # Fecha conexao

    if (cont == 1):
         """
          -------------------- Cliente --------------------
         """  
         clienteTest = ClienteTest(conexao)

         opcoesCliente = {
             "[1] - Cadastrar cliente" : clienteTest.cadastrarCliente,
             "[2] - Consultar cliente" : clienteTest.consultarCliente,
             "[3] - Listar clientes"   : clienteTest.listarClientes,
             "[4] - Deletar cliente"   : clienteTest.deletarCliente,
             "[0] - Sair."             : lambda: print("Saindo das opcoes de cliente...\n")
         }

         imprime_e_executa_opcoes(opcoesCliente, "Cliente")

    if (cont == 2):
        """
          -------------------- Catalogo --------------------
        """   
        catalogoTest = CatalogoTest(conexao)

        opcoesCatalogo = {
             "[1] - Cadastrar catalogo": catalogoTest.cadastrarCatalogo,
             "[2] - Preencher catalogo": catalogoTest.preencherCatalogo,
             "[3] - Consultar catalogo": catalogoTest.consultarCatalogo,
             "[4] - Listar catalgos"   : catalogoTest.listarCatalgos,
             "[5] - Deletar catalogo"  : catalogoTest.deletarCatalogo,
             "[0] - Sair."             : lambda: print("Saindo das opcoes de catalogo...\n")
        }

        imprime_e_executa_opcoes(opcoesCatalogo, "Catalogo")

    if(cont==3):
        print("[1] - Cadastrar produto")
        print("[2] - Consultar produto")
        print("[3] - Atualizar produto")
        print("[4] - Deletar produtos")

        opcaoP = int(input("Digite a sua opcao: "))

        if(opcaoP==1):
                print("Cadastrar produto:")
                nome_produto = input("Nome do produto: ")
                preco_produto = input("Preco: ")
                descricao_produto = input('Descricao: ')
                avaliacao_produto = input("Avalie (0 - 5): ")
                produto = Produto(nome_produto,preco_produto,descricao_produto,avaliacao_produto)
                ProdutoDAO(conexao).salvar_produto(produto)

        if(opcaoP==2):
             print("Consulta produto:")
             #id = "644b668c8cf47495651db7c4"
             id_produto = input("Digite o id: ")
             
             produtos = ProdutoDAO(conexao).consultar_produto(id_produto) # id
             print("Nome:", produtos['nome'], "|Preco:", produtos['preco'], "|Descricao:", produtos['descricao'], "|Avaliacao:", produtos['avaliacao'])

        if(opcaoP==3):
             print("Atualizar produto:")
             #id="644b668c8cf47495651db7c4"
             id = input("Digite o id: ")

             novo_nome = input("Digite o novo nome: ")
             novo_preco = input("Digite o  novo preco: ")
             nova_desc = input("Digite a nova descricao: ")
             nova_avaliacao = input("Digite a nova a valiacao (0-5): ")

             produto = ProdutoDAO(conexao).atualizar_produto(novo_nome,novo_preco, nova_desc, nova_avaliacao,id)
        if(opcaoP==4):
             print("Deletar produto:")
             produto_delet = "644b668c8cf47495651db7c4"
             produto = ProdutoDAO(conexao).deletar_produto(produto_delet)
    if(cont==4):
        print("[1] - Cadastrar comentario")
        print("[2] - Consultar comentario")
        print("[3] - Atualizar comentario")
        print("[4] - Listar comentarios")
        print("[5] - Deletar comentario")

        opcaoP = int(input("Digite a sua opcao: "))

        if(opcaoP==1):
                print("Cadastrar comentario :")
                Comentarios(conexao).salvar_comentario(input("conteudo: "),input("id do usuario: "),input("id do catalogo: "),input("nome do usuario: "),input("data de criação: "))
        if(opcaoP==2):
             print("Consultar comentario:")
             #id = "644d82977a6b8f1b720dede0"
             id = input("Digite o id: ")
             
             comentario = Comentarios(conexao).consultar_comentario(id)
             print("conteudo: ", comentario['conteudo'], "id do usuario: ", comentario['usuario_id'],'id do catalogo: ',comentario['catalogo_id'], "nome do usuario: ", comentario['nome_usuario'], "data de criação:", comentario['criado_em'])

        if(opcaoP==3):
             print("Atualizar comentario:")
             #id="644b668c8cf47495651db7c4"
             id = input("Digite o id: ")
             Comentarios(conexao).atualizar_comentario(input("conteudo: "),input("id do usuario: "),input("id do catalogo: "),input("nome do usuario: "),input("data de criação: "),id)
             print("comentario atualizado")

        if(opcaoP==4):
             Comentarios(conexao).listar_comentario()
             
        if(opcaoP==5):
             print("Deletar comentario:")
             id = input("Digite o id: ")
             Comentarios(conexao).deletar_comentario(id)   
             print("comentario deletado")
     