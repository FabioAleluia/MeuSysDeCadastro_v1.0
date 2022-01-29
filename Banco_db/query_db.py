import hashlib
import sqlite3

class QueryDb:
    def __init__(self, user, pwd, consu_hash):
        self.user = user
        self.pwd = pwd
        self.consu_hash = consu_hash
              
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT hsh FROM pessoafisica")
        self.result_tabela = str(cursor.fetchall())
        
        if self.consu_hash in self.result_tabela:
            print('User já existe')
        else:
            print('Não existe')

class QueryTeste:
    def __init__(self, user, pwd, consu_hash):
        self.user = user
        self.pwd = pwd
        self.consu_hash = consu_hash
              
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT hsh FROM validalogin")
        self.result_tabela = str(cursor.fetchall())
        
        if self.consu_hash in self.result_tabela:
            print('User já existe')
        else:
            print('Não existe')
