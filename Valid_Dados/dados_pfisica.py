from re import S
from PyQt5 import uic,QtWidgets
from Banco_db import data_base

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

        if self.cpf.isdigit():
            cpf_oneze = (self.cpf[:11])
            print(cpf_oneze)
            print('Sim')
            
            print(type(self.cpf))
            send_db = data_base.WriteDb(cpf=self.cpf, nome=self.nome, endereco=self.endereco, cep=self.cep, uf=self.uf, cidade=self.cidade, telefonefixo=self.telefonefixo, telefonecelular=self.telefonecelular, email=self.email)
            
        else:
            print('Nao')
        
        
            #send_db = data_base.WriteDb(cpf=self.cpf, nome=self.nome, endereco=self.endereco, cep=self.cep, uf=self.uf, cidade=self.cidade, telefonefixo=self.TelefoneFixo, telefonecelular=self.TelefoneCelular, email=self.email)
