from Produto import Produto
from ProdutoDAO import ProdutoDAO


cont = 1

while(cont!=0):
    print("[1] - Clientes")
    print("[2] - Catálogos")
    print("[3] - Produtos")
    print("[4] - Comentários")
    print("[0] - Sair")
    cont = int(input("Digite a sua opção: "))

    
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
                ProdutoDAO().salvar_produto(produto)

        if(opcaoP==2):
             print("Consulta produto:")
             id = "644b668c8cf47495651db7c4"
             #id_produto = input("Digite o id: ")
             
             produtos = ProdutoDAO().consultar_produto(id)
             print("Nome:", produtos['nome'], "|Preco:", produtos['preco'], "|Descricao:", produtos['descricao'], "|Avaliacao:", produtos['avaliacao'])

        if(opcaoP==3):
             print("Atualizar produto:")
             id="644b668c8cf47495651db7c4"

             novo_nome = input("Digite o novo nome: ")
             novo_preco = input("Digite o  novo preco: ")
             nova_desc = input("Digite a nova descricao: ")
             nova_avaliacao = input("Digite a nova a valiacao (0-5): ")

             produto = ProdutoDAO().atualizar_produto(novo_nome,novo_preco, nova_desc, nova_avaliacao,id)
        if(opcaoP==4):
             print("Deletar produto:")
             produto_delet = "644b668c8cf47495651db7c4"
             produto = ProdutoDAO().deletar_produto(produto_delet)
        


       
    
