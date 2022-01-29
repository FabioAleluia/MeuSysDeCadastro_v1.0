from PyQt5 import uic,QtWidgets

class GetJanelas:
    def __init__(self):
        self.win_login = tela_login=uic.loadUi("Windows/tela_login.ui")
        self.win_opcoes = tela_opcoes=uic.loadUi("Windows/tela_opcoes.ui")
        self.win_formulario = tela_formulario=uic.loadUi("Windows/tela_formulario.ui")
        self.win_new_login = tela_criar_login=uic.loadUi("Windows/tela_criar_login.ui")


