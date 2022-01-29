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

        if self.cpf.isdigit(): # Contem algum digitio ?
            cpf_onze = (self.cpf[:11])
            cpf_onze = len(cpf_onze)
            if cpf_onze < 11 or cpf_onze > 11:
                print('Cpf invalido')
            
            else:
                print('Cpf valido')
            
                
            #send_db = data_base.WriteDb(cpf=self.cpf, nome=self.nome, endereco=self.endereco, cep=self.cep, uf=self.uf, cidade=self.cidade, telefonefixo=self.telefonefixo, telefonecelular=self.telefonecelular, email=self.email)
            
        if self.nome.isdigit():
            self.nome = (self.nome[:50])
            self.nome = len(self.nome)
            if self.nome < 50 or self.nome > 50:
                print('Nome muito extenso')
            
            if self.nome.isnumeric():
                print('Não tem Numero')
            
            else:
                print('Contem Numero')
        
        
