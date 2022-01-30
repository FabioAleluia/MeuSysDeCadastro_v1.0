import sqlite3

class WriteDb:
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
    
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"
    
        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()
        d = '12:00'

        '''
        cursor.execute(""" CREATE TABLE IF NOT EXISTS pessoafisica (
            user text,
            pwd text,
            hsh text,
            dt text
            )""")
        '''

        cursor.execute("INSERT INTO pessoafisica VALUES ('"+self.cpf+"', '"+self.nome+"', '"+self.endereco+"', '"+self.cep+"', '"+self.uf+"', '"+self.cidade+"', '"+self.telefonefixo+"', '"+self.telefonecelular+"', '"+self.email+"')")

        conexao_db.commit()
        conexao_db.close()


class NovoUser:
    
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
      
        # Local onde esta o arquivo do Banco de Dados.
        dir_db = "/mnt/Fabio_DB/Estudos/Python/Projetos/Software_de_Cadastro/cadastros_v.1.0_gui/Banco_db/Banco_dd.db"

        conexao_db = sqlite3.connect(dir_db) # Realizar conexão do arquivo do Banco de Dados
        cursor = conexao_db.cursor()
        d = '12:00'

        '''
        cursor.execute(""" CREATE TABLE IF NOT EXISTS validalogin (
            usuario text,
            senha text
  
            )""")
        '''
        
        cursor.execute("INSERT INTO validalogin VALUES ('"+self.usuario+"', '"+self.senha+"')")

        conexao_db.commit()
        conexao_db.close()
