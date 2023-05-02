
from conexao.conexao_mongodb import ConexaoMongoDB

from cliente.cliente     import Cliente
from cliente.cliente_dao import ClienteDAO

from datetime import datetime

class ClienteTest:

    def __init__(self, conexao: ConexaoMongoDB):
        self.conexao = conexao
        self.dao     = ClienteDAO(self.conexao)

    def listarClientes(self):
        print("----Clientes cadastrados:--------")
        for _, cliente in self.dao.listar().items():
            print(cliente.to_dict())
        print("---------------------------------\n")

    def consultarCliente(self, cliente_id) -> Cliente:
        return self.dao.consultar(cliente_id)

    def cadastrarCliente(self):
        print("Cadastrar novo cliente: ")

        nome  = input("Nome: ")
        email = input('Email: ')
        
        self.dao.salvar(Cliente(nome, email))
        
        print("Salvo com sucesso!\n")

    
    def deletarCliente(self):
        cliente_id = input("Digite o id: ")
        self.dao.deletar(cliente_id)
        print("Deletado!\n")