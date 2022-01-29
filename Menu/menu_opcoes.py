from Menu import menu_opcoes
from Menu import print_menus
from Formulario import Form_Fisica
from Formulario import Form_Juridico
from Menu import sub_menu

def InicioErp():
    p_menus = print_menus.MenuOne()    
    
    opc = input('Opção: ')
    
    if not opc.isdecimal():
        return InicioErp()
    
    if opc.isdigit():
        opc = int(opc)
        
    if opc < 1 or opc > 4:
        return InicioErp()
        
    if opc == 1:
        print('\033c')
        ir_opcfj = sub_menu.MenuCliteFJ()
        #ir_pessoa_fisica = Form_Fisica.PessoaFisica()
        
        
    if opc == 2:
        print('Consulta Cliente')
        
    if opc == 3:
        print('Excluir registro')