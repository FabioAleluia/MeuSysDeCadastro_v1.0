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
        if not self.cpf:
            print('Preencha o campo CPF')
            
        
        if self.cpf.isdigit(): # Contem algum digitio ?
            cpf_onze = (self.cpf[:11])
            cpf_onze = len(cpf_onze)
        
            if cpf_onze < 11 or cpf_onze > 11:
                print('Cpf invalido')
            
            else:
                print('Cpf valido')
             
        else:
            print('Preencha o campo CPF')
            
        
        ## Valida dados do Campo Nome
        if not self.nome:
            print('Preencha o campo Nome')
            
        
        if self.nome.isdigit():
            self.nome = (self.nome[:10])
            self.nome = len(self.nome)
        
            if self.nome < 5 or self.nome > 10:
                print('Nome Curto')
            
            else:
                print('Nome muito Grande')
            
            if self.nome.isalpha():
                print('Não tem Numero')
            
            else:
                print('Contem Numero')
        else:
            print('Preencha o Campo Nome')
            
        
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
    
        send_db = data_base.WriteDb(cpf=self.cpf, nome=self.nome, endereco=self.endereco, cep=self.cep, uf=self.uf, cidade=self.cidade, telefonefixo=self.telefonefixo, telefonecelular=self.telefonecelular, email=self.email)