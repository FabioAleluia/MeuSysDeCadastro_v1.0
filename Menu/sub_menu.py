from Menu import print_menus
from Formulario import Form_Fisica

def MenuCliteFJ():
    menu_two = print_menus.MenuTwo()
    
    opc = input('Opção: ')
    if not opc.isdecimal():
        return MenuCliteFJ()
    
    if opc.isdigit():
        opc = int(opc)
    
    if opc < 1 or opc > 4:
        return MenuCliteFJ()
    
    if opc == 1:
        print('\033c')
        p_fisica = Form_Fisica.PessoaFisica()
    
    if opc == 2:
        print('\033c')
        #p_juridica = Form_Juridica.PessoaJuridica()
    
    if opc == 3:
        pass
        #ttt = opcoes.OpcoesInicias.teste()