import sqlite3

class TesteT:
    def __init__(self):
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT pwd FROM pessoafisica")
        self.result_tabela = str(cursor.fetchall())

class TesteTt:
    def __init__(self):
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"
        conexao = sqlite3.connect(dir_db)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT senha FROM validalogin")
        self.result_tabela = str(cursor.fetchall())