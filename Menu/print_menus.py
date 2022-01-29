class MenuOne:
    def __init__(self):
        print('\033c')

        print('\033[1;33m: Menu de Opções :\033[0;0m')
        print('''
        [1] Cadastra Cliente:
        [2] Consulta Cliente:
        [3] Editar Registro:
        [4] Sair:
            ''')

class MenuTwo:
    def __init__(self): 
        print('\033c')

        print('\033[1;32m: Opções :\033[0;0m')
        print('''
        [1] Pessoa Fisica
        [2] Pessoa Juridica
        [3] Menu Principal
        [4] Sair
            ''')
