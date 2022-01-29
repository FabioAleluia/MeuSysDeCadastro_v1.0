from time import sleep, time
from tkinter import W
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
        #tela_criar_login.aviso_login_criado.setText("Login criado com sucesso.")
        tela_criar_login.frame_1.show()
        #return GravaDadosNewUser()

class CadastroFisico:
    def __init__(self):
        #aviso = dados_pfisica.DadosPfisica()
    
        input_cpf = tela_formulario.input_cpf.text()
        input_nome = tela_formulario.input_nome.text()
        input_endereco = tela_formulario.input_endereco.text()
        input_cep = tela_formulario.input_cep.text()
        input_uf = tela_formulario.input_uf.text()
        input_cidade = tela_formulario.input_cidade.text()
        input_TelefoneFixo = tela_formulario.input_TelefoneFixo.text()
        input_TelefoneCelular = tela_formulario.input_TelefoneCelular.text()
        input_email = tela_formulario.input_email.text()

        send_db = dados_pfisica.DadosPfisica(cpf=input_cpf, nome=input_nome, endereco=input_endereco, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_TelefoneFixo, telefonecelular=input_TelefoneCelular, email=input_email)

class Notificacoes:
    def __init__(self):
        self.aviso_01 = tela_formulario.aviso_01.setText("*")
        
''''
def GravaDadosCadastro():
    #aviso = dados_pfisica.DadosPfisica()
    
    input_cpf = tela_formulario.input_cpf.text()
    input_nome = tela_formulario.input_nome.text()
    input_endereco = tela_formulario.input_endereco.text()
    input_cep = tela_formulario.input_cep.text()
    input_uf = tela_formulario.input_uf.text()
    input_cidade = tela_formulario.input_cidade.text()
    input_TelefoneFixo = tela_formulario.input_TelefoneFixo.text()
    input_TelefoneCelular = tela_formulario.input_TelefoneCelular.text()
    input_email = tela_formulario.input_email.text()

    send_db = dados_pfisica.DadosPfisica(cpf=input_cpf, nome=input_nome, endereco=input_endereco, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_TelefoneFixo, telefonecelular=input_TelefoneCelular, email=input_email)
    #send_db = data_base.WriteDb(cpf=input_cpf, nome=input_nome, endereco=input_endereco, cep=input_cep, uf=input_uf, cidade=input_cidade, telefonefixo=input_TelefoneFixo, telefonecelular=input_TelefoneCelular, email=input_email)
'''

def LimparCampos():        
    input_cpf = tela_formulario.input_cpf.clear()
    tela_formulario.aviso_dados_errados.setText("")
    tela_formulario.aviso_01.setText("")
    input_nome = tela_formulario.input_nome.clear()
    input_endereco = tela_formulario.input_endereco.clear()
    input_cep = tela_formulario.input_cep.clear()
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
tela_formulario.salva_infos.clicked.connect(CadastroFisico)
tela_login.line_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
tela_criar_login.line_new_pwd.setEchoMode(QtWidgets.QLineEdit.Password)

## Tamanho das Janelas
tela_login.setFixedSize(461,426)
tela_criar_login.setFixedSize(461,426)
tela_opcoes.setFixedSize(601,500)

tela_login.show()
app.exec()