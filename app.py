import os

restaurantes = [{'nome':'pizza', 'categoria':'Massa', 'ativo':False},
                {'nome':'Smash', 'categoria':'Lanche', 'ativo':True},
                {'nome':'Burguer King', 'categoria':'Lanche', 'ativo':False}]

def exibir_nome_do_programa():
    os.system('cls')
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar Estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo ('Finalizando App.')

def voltar_ao_menu_principal():
    input('\n digite uma tecl para voltar ao menu: ')
    main()

def opcao_invalida():
    print('opção Invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadatrar_novo_restaurante():
    '''essa função é responsavel por cadastrar um novo restaurante'''
        
    exibir_subtitulo('Cadastro de Novos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que você deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o Restaurante {nome_do_restaurante} foi cadasatrado com sucesso')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')
    
    print(f'{'Nome do Restaurnte'.ljust(22)} | {'categoria'.ljust(20)} | {'Status'}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'ativo' if restaurante ['ativo'] else 'inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()
        
    
    
def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando estado do Restaurante')
    nome_restaurante = input('Digite o nome do Restaurante que deseja Alternar o Estado: ')
    restaurante_encontrado = False
        
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'o Restaurante {nome_restaurante} foi ativado com Sucesso' if restaurante['ativo'] else f'o Restaurante {nome_restaurante} foi destivado Com sucesso.'
            print(mensagem)
                
    if not restaurante_encontrado:
        print('O Restaurante Não foi encontrado')     

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadatrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app() 
        else: 
            opcao_invalida()
    except:
        opcao_invalida()
    

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()