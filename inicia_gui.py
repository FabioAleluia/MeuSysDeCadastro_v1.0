#from os import PRIO_USER
#from time import sleep, time
#from tkinter import W
#from urllib import request
from PyQt5 import uic,QtWidgets
import hashlib
import sqlite3
from Banco_db import data_base
from Banco_db import query_db
from Banco_db import teste
from Windows import Janelas
from Valid_Dados import dados_pfisica

def valida_login():
    tela_login.aviso_login.setText("")
    info_user = tela_login.line_user.text()
    if not info_user:
        tela_login.aviso_login.setText("Usuário ou senha incorreto.")
        return valida_login()
    else:
        
        info_pwd = tela_login.line_pwd.text()
        
        result_db = teste.TesteTt()
        join_up = str(info_user) + str(info_pwd)
        c_hash = hashlib.sha256(join_up.encode('utf-8')).hexdigest()

    if c_hash in result_db.result_tabela:
        TelaOpcoes()
    
    else:
        tela_login.aviso_login.setText("Usuário ou senha incorreto.")
    

def TelaOpcoes():
    tela_login.close()
    tela_opcoes.show()

def TelaFormulario():
    tela_opcoes.close()   
    tela_formulario.show()

def Volta_for_login():
    tela_login.aviso_login.clear()
    tela_opcoes.close()
    tela_login.line_user.clear()
    tela_login.line_pwd.clear()
    tela_login.show()

def Volta_for_login_Two():
    tela_login.aviso_login.clear()
    tela_criar_login.close()
    tela_login.line_user.clear()
    tela_login.line_pwd.clear()
    tela_login.show()

def Volta_for_opcoes():
    LimparCampos()
    tela_formulario.close()
    tela_opcoes.show()

def Criarlogin():
    tela_criar_login.aviso_01.clear()
    tela_criar_login.aviso_02.clear()
    tela_criar_login.frame_1.close()
    tela_criar_login.line_new_user.clear()
    tela_criar_login.line_new_pwd.clear()
    tela_criar_login.aviso_cadastro.setText("")
    tela_login.close()
    tela_criar_login.show()

def GravaDadosNewUser():
    tela_criar_login.frame_1.close()
    tela_criar_login.aviso_cadastro.clear()
    new_user = tela_criar_login.line_new_user.text()
    new_pwd = tela_criar_login.line_new_pwd.text()
    
    if not new_user:
        tela_criar_login.aviso_01.setText("*")
        tela_criar_login.aviso_02.setText("*")
        tela_criar_login.aviso_cadastro.setText("Preencha os campos corretamente")
        return GravaDadosNewUser()

    if not new_pwd:
        tela_criar_login.aviso_01.setText("*")
        tela_criar_login.aviso_02.setText("*")
        tela_criar_login.aviso_cadastro.setText("Preencha os campos corretamente")
        return GravaDadosNewUser()
    
    else:
        new_up = str(new_user) + str(new_pwd)
        new_hash = hashlib.sha256(new_up.encode('utf-8')).hexdigest()
        
        result_db = teste.TesteTt()
    
    if new_hash in result_db.result_tabela:
        tela_criar_login.aviso_cadastro.setText("Usuário já existente.")
        return GravaDadosNewUser()
    
    else:
        send_db = data_base.NovoUser(usuario=new_user, senha=new_hash)
        tela_criar_login.frame_1.show()

       
def GravaDadosCadastro():
    ## Valida dados do campo CPF
    input_cpf = tela_formulario.a_input_cpf.text()
    valida_cpf = input_cpf.strip()
    valida_cpf = valida_cpf.replace(" ","")
    
    if valida_cpf.isnumeric():
        valida_cpf = len(valida_cpf)
        valida_cpf = int(valida_cpf)
            
        if valida_cpf < 11 or valida_cpf > 11:
            tela_formulario.aviso_01.setText("*")
            erro_input_cpf = 0

        if valida_cpf == 11:
            input_cpf = str(input_cpf.strip())
            input_cpf = str(input_cpf.replace(" ",""))
            tela_formulario.aviso_01.setText("")
            tela_formulario.a_input_cpf.setText(input_cpf)
            erro_input_cpf = 1
        
        else:
            input_cpf = str(valida_cpf)
            
    else:
        tela_formulario.aviso_01.setText("*")
        erro_input_cpf = 0
   
    ## VALIDA DADOS DO CAMPO NOME
    input_nome = tela_formulario.a_input_nome.text()
    valida_nome = input_nome.replace(" ","")
    
    if valida_nome.isalpha():
        valida_nome = len(valida_nome)
        valida_nome = int(valida_nome)
        
        if valida_nome < 5 or valida_nome > 45:
            tela_formulario.aviso_02.setText("*")
            erro_input_nome = 0
        
        if valida_nome >= 5 or valida_nome <= 45:
            input_nome = str(input_nome.strip())
            
            tela_formulario.aviso_02.setText("")
            tela_formulario.a_input_nome.setText(input_nome)
            erro_input_nome = 1
    else:
        tela_formulario.aviso_02.setText("*")
        erro_input_nome = 0

    ## VALIDA DADOS DO CAMPO CEP
    input_cep = tela_formulario.a_input_cep.text()
    valida_cep = input_cep
    
    if input_cep.isnumeric():
        valida_cep = len(valida_cep)
        valida_cep = int(valida_cep)

        if valida_cep < 8 or valida_cep > 8:
            tela_formulario.aviso_03.setText("*")
            erro_input_cep = 0
        
        if valida_cep == 8:
            input_cep = str(input_cep.strip())
            tela_formulario.aviso_03.setText("")
            erro_input_cep = 1
        
        else:
            input_cep = str(input_cep)
    
    else:
        tela_formulario.aviso_03.setText("*")
        erro_input_cep = 0
    
    ## VALIDA DADOS DO CAMPO ENDEREÇO
    input_endereco = tela_formulario.input_endereco.text()
    valida_endereco = input_endereco.strip()
    valida_endereco = valida_endereco.replace(" ", "")
    
    if valida_endereco.isalnum():
        valida_endereco = len(valida_endereco)
        valida_endereco = int(valida_endereco)
        
        if valida_endereco <= 0 or valida_endereco > 200:
            tela_formulario.aviso_06.setText("*")
            erro_input_endereco = 0
        
        if valida_endereco >= 5 or valida_endereco <=200:
            tela_formulario.aviso_06.setText("")
            valida_endereco = str(input_endereco)
            erro_input_endereco = 1
    
    else:
        tela_formulario.aviso_06.setText("*")
        erro_input_endereco = 0
    
    ## VALIDA DADOS DO COMPO NUMERO
    input_numero = tela_formulario.input_numero.text()
    valida_numero = input_numero
    
    if valida_numero.isnumeric():
        valida_numero = len(valida_numero)
        valida_numero = int(valida_numero)
        
        if valida_numero < 1 or valida_numero > 10:
            tela_formulario.aviso_06.setText("*")
            erro_input_numero = 0
        
        if valida_numero >= 1 or valida_numero <= 15:
            input_numero = str(input_numero.strip())
            input_numero = input_numero.replace(" ","")
            tela_formulario.aviso_06.setText("")
            tela_formulario.input_numero.setText(input_numero)
            erro_input_numero = 1
    
    else:
        tela_formulario.aviso_06.setText("*")
        erro_input_numero = 0
        
    ## VALIDA DADOS DO CAMPO UF
    input_uf = tela_formulario.input_uf.text()
    
    valida_uf = input_uf.strip()
    valida_uf = valida_uf.replace(" ", "")
    
    if valida_uf.isalpha():
        valida_uf = len(valida_uf)
        valida_uf = int(valida_uf)
        
        if valida_uf < 2 or valida_uf > 2:
            tela_formulario.aviso_04.setText("*")
            erro_input_uf = 0
        
        if valida_uf == 2:
            input_uf = str(input_uf)
            tela_formulario.aviso_04.setText("")
            erro_input_uf = 1
    
    else:
        tela_formulario.aviso_04.setText("*")
        erro_input_uf = 0
        print('UF invalido')
    
    ## VALIDA DADOS DO CAMPO CIDADE
    input_cidade = tela_formulario.input_cidade.text()
    valida_cidade = input_cidade.strip()
    valida_cidade = valida_cidade.replace(" ", "")
    
    if valida_cidade.isalpha():
        valida_cidade = len(valida_cidade)
        valida_cidade = int(valida_cidade)
        
        if valida_cidade < 4 or valida_cidade > 45:
            tela_formulario.aviso_05.setText("*")
            erro_input_cidade = 0
            
        if valida_cidade >= 4 or valida_cidade <= 45:
            input_cidade = str(input_cidade)
            tela_formulario.aviso_05.setText("")
            erro_input_cidade = 1
    
    else:
        tela_formulario.aviso_05.setText("*")
        erro_input_cidade = 0

        
    ## VALIDA DADOS DO CAMPO TELEFONE FIXO
    input_TelefoneFixo = tela_formulario.input_TelefoneFixo.text()
    valida_telefonefixo = input_TelefoneFixo
    
    if valida_telefonefixo.isnumeric():
        valida_telefonefixo = len(valida_telefonefixo)
        valida_telefonefixo = int(valida_telefonefixo)
        
        if valida_telefonefixo < 11 or valida_telefonefixo > 11:
            tela_formulario.aviso_07.setText("*")
            erro_input_telefonefixo = 0
        
        if valida_telefonefixo == 11:
            input_TelefoneFixo = str(input_TelefoneFixo.strip())
            input_TelefoneFixo = input_TelefoneFixo.replace(" ", "")
            tela_formulario.aviso_07.setText("")
            tela_formulario.input_TelefoneFixo.setText(input_TelefoneFixo)
            erro_input_telefonefixo = 1
    else:
        tela_formulario.aviso_07.setText("*")
        erro_input_telefonefixo = 0
        
    ## VALIDA DADOS DO CAMPO TELEFONE CELULAR
    input_TelefoneCelular = tela_formulario.input_TelefoneCelular.text()
    valida_telefonecelular = input_TelefoneCelular
    
    if valida_telefonecelular.isnumeric():
        valida_telefonecelular = len(valida_telefonecelular)
        valida_telefonecelular = int(valida_telefonecelular)
        
        if valida_telefonecelular < 11 or valida_telefonecelular > 11:
            tela_formulario.aviso_08.setText("*")
            erro_input_telefonecelular = 0
        
        if valida_telefonecelular == 11:
            input_TelefoneCelular = str(input_TelefoneCelular.strip())
            input_TelefoneCelular = input_TelefoneCelular.replace(" ", "")
            tela_formulario.aviso_08.setText("")
            tela_formulario.input_TelefoneCelular.setText(input_TelefoneCelular)
            erro_input_telefonecelular = 1
    
    else:
        tela_formulario.aviso_08.setText("*")
        erro_input_telefonecelular = 0
            
    
    ## VALIDA DADOS DO CAMPO E-MAIL
    input_email = tela_formulario.input_email.text()
    valida_email = input_email
    
    

    # CHECAGEM DE ERROS DAS ENTRADAS DOS DADOS
    if erro_input_cpf == 0:
        tela_formulario.aviso_01.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next CPF')
    
    if erro_input_nome == 0:
        print('NOME INVALIDO')
        tela_formulario.aviso_02.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next NOME')
    
    if erro_input_endereco == 0:
        tela_formulario.aviso_06.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next ENDEREÇO')
    
    if erro_input_cep == 0:
        tela_formulario.aviso_06.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next CEP')

    if erro_input_numero == 0:
        tela_formulario.aviso_06.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next NUMERO')
    
    if erro_input_uf == 0:
        tela_formulario.aviso_04.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next UF')
    
    if erro_input_cidade == 0:
        tela_formulario.aviso_05.setText("*")
        return tela_formulario()
    
    else:
        pass
        print('Next CIDADE')
        
    if erro_input_telefonefixo == 0:
        tela_formulario.aviso_07.setText("*")
        return TelaFormulario()

    else:
        pass
        print('Next Telefone Fixo')
    
    if valida_telefonecelular == 0:
        tela_formulario.aviso_08.setText("*")
        return TelaFormulario()
    
    else:
        pass
        print('Next Telefone Celular')    
            
    send_db = data_base.WriteDb(cpf=input_cpf, nome=input_nome, endereco=input_endereco, numero=input_numero, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_TelefoneFixo, telefonecelular=input_TelefoneCelular, email=input_email)


def LimparCampos():
    input_cpf = tela_formulario.a_input_cpf.clear()
    tela_formulario.aviso_dados_errados.setText("")
    tela_formulario.aviso_01.setText("")
    tela_formulario.aviso_02.setText("")
    tela_formulario.aviso_03.setText("")
    tela_formulario.aviso_04.setText("")
    tela_formulario.aviso_05.setText("")
    tela_formulario.aviso_06.setText("")
    tela_formulario.aviso_07.setText("")
    tela_formulario.aviso_08.setText("")
    input_nome = tela_formulario.a_input_nome.clear()
    input_endereco = tela_formulario.input_endereco.clear()
    input_cep = tela_formulario.a_input_cep.clear()
    input_uf = tela_formulario.input_uf.clear()
    input_cidade = tela_formulario.input_cidade.clear()
    input_TelefoneFixo = tela_formulario.input_TelefoneFixo.clear()
    input_TelefoneCelular = tela_formulario.input_TelefoneCelular.clear()
    input_email = tela_formulario.input_email.clear()

        
app=QtWidgets.QApplication([])

## Janelas
Win = Janelas.GetJanelas()
tela_login = Win.win_login
tela_opcoes = Win.win_opcoes
tela_formulario = Win.win_formulario
tela_criar_login = Win.win_new_login

## Ações dos Butões
tela_login.Buttonlogin.clicked.connect(valida_login)
tela_opcoes.new_cadastros.clicked.connect(TelaFormulario)
tela_opcoes.volta_for_opcoes.clicked.connect(Volta_for_login)
tela_formulario.volta_for_opcoes.clicked.connect(Volta_for_opcoes)
tela_login.criar_login.clicked.connect(Criarlogin)
tela_criar_login.cadastra_user.clicked.connect(GravaDadosNewUser)
tela_criar_login.volta_for_login.clicked.connect(Volta_for_login_Two)
tela_formulario.salva_infos.clicked.connect(GravaDadosCadastro)
tela_login.line_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
tela_criar_login.line_new_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

## Tamanho das Janelas
tela_login.setFixedSize(461,426)
tela_criar_login.setFixedSize(461,426)
tela_opcoes.setFixedSize(601,500)

tela_login.show()
app.exec()