from re import S
from PyQt5 import uic,QtWidgets

class DadosPfisica:
    def __init__(self, cpf, nome, endereco, cep, uf, cidade, telefonefixo, telefonecelular, email):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.uf = uf
        self.cidade = cidade
        self.telefonefixo = telefonefixo
        self.telefonecelular = telefonecelular
        self.email = email

        if not self.cpf:
            print('CPF vazio')