from re import S
from signal import pause
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

        
        ## Valida dados do Campo CPF
        valida_cpf = self.cpf
        if valida_cpf.isnumeric():
            print(valida_cpf)
            valida_cpf = valida_cpf[0:11]
            valida_cpf = len(valida_cpf)
            print(valida_cpf)
            
            if valida_cpf < 11 or valida_cpf > 11:
                print('cpf muinto grande')
            else:
                valida_cpf = str(valida_cpf)
                print('CPF VALIDO')
            
        else:
            print('CPF Invalido')
        
        ## Valida dados do Campo Nome
        if not self.nome:
            pass
        
        ## Valida dados do Campo Endereço
        if self.endereco.isdigit():
            pass
        
        if self.cep.isdigit():
            pass
        
        if self.uf.isdigit():
            pass
        
        if self.cidade.isdigit():
            pass
        
        if self.telefonefixo.isdigit():
            pass
        
        if self.telefonecelular.isdigit():
            pass
        
        if self.email.isdigit():
            pass
        
            
        send_db = data_base.WriteDb(cpf=valida_cpf, nome=self.nome, endereco=self.endereco, cep=self.cep, uf=self.uf, cidade=self.cidade, telefonefixo=self.telefonefixo, telefonecelular=self.telefonecelular, email=self.email)