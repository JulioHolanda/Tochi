import func
import webbrowser
import os
os.system("cls")

"""adiciona_pessoa=open('conta.txt', 'a')
ler_pessoa=open('conta.txt', 'r')
resposta=input('Você já possui uma conta? \n[S]sim\t[N]não: ').lower()
if resposta=='s':
    cadastrado=input('Insira seu nome ou email:')
    if cadastrado in ler_pessoa:
        print(f'Bem vindo(a) {cadastrado}')
    else:
        print('Nome ou email não encontrado. Crie uma conta ou tente novamente.')
if resposta=='n':
    resposta2=input('Deseja criar uma conta? \n[s]sim\t[n]não: ').lower()
    if resposta2=='n':
        print('Tochi agradece sua visita. Até a próxima!')
    elif resposta2=='s':
        cadastro=adiciona_pessoa.writelines(input('Insira um email válido: '))
        Nome_Usuário=adiciona_pessoa.writelines(input('Insira um nome de usuário: '))
        if Nome_Usuário in ler_pessoa:
            Nome_Usuário=input('Este nome de usuário já existe. Por favor, insira outro nome: ')
        print('Sua conta foi criada com sucesso!')
adiciona_pessoa.close()
ler_pessoa.close()"""

print("Bem vindo ao TOCHI!\n\n-- Menu Principal --\nO que gostaria de acessar?")
print(
    "[1] Estudantes\n"
    "[2] Professores\n"
    "[3] Metodologias\n"
    "[4] Suporte\n"
    "[0] Sair"
)

caminho = int(input())

while caminho > 0 and caminho < 5:
    
    while caminho == 1:
        print('\n-- ESTUDANTES --\n'
            '[1] Vizualizar Todos\n'
            '[2] Pesquisar\n'
            '[3] Adicionar\n'
            '[4] Remover\n'
            '[0] voltar'
        )
        caminho = int(input())
        
        if caminho == 1:
            func.listagem()
        elif caminho == 2:
            func.procura()
        elif caminho == 3:
            func.novos_dados()
        elif caminho == 4:
            func.del_data()
        elif caminho == 0:
            break
        
        caminho = 1

    while caminho == 2:
        print(
            '\n-- PROFESSORES --\n'
            '[1] Vizualizar Todos\n'
            '[2] Pesquisar\n'
            '[3] Adicionar\n'
            '[4] Remover\n'
            '[0] voltar'
        )
        caminho = int(input())
        
        if caminho == 1:
            func.listagem_prof()
        elif caminho == 2:
            func.procura_prof()
        elif caminho == 3:
            func.novos_dados_prof()
        elif caminho == 4:
            func.del_data_prof()
        elif caminho == 0:
            break
        
        caminho = 2
    
    while caminho == 3:
        print(
            '\n-- METODOLIGAS --\n'
            '[1] Metodologia 1\n'
            '[2] Metodologia 2\n'
            '[3] Metodologia 3\n'
            '[0] voltar'
        )
        caminho = int(input())
        
        if caminho == 1:
            print('metodologia 1 aqui')
        elif caminho == 2:
            print('metodologia 2 aqui')
        elif caminho == 3:
            print('metodologia 3 aqui')
        elif caminho == 0:
            break
        
        caminho = 3
    
    while caminho == 4:
        print(
            '\n-- SUPORTE --\n'
            '[1] Associação Brasileira do Defict de Atenção (ABDA)\n'
            '[2] Formulário TDHA (SNAP - IV)\n'
            '[3] Contatos Profissionais da Área\n'
            '[0] voltar'
        )
        caminho = int(input())
        
        if caminho == 1:
            webbrowser.open("https://tdah.org.br/")
        elif caminho == 2:
            webbrowser.open("https://tdah.org.br/diagnostico-criancas/")
        elif caminho == 3:
            func.listagem_espec()
        elif caminho == 0:
            break
        
        caminho =3
    
    print("\n-- Menu Principal --\nO que gostaria de acessar?")
    print(
        "[1] Estudantes\n"
        "[2] Professores\n"
        "[3] Metodologias\n"
        "[4] Suporte\n"
        "[0] Sair"
    )
    caminho = int(input())

print("\n-+- PROGRAMA ENCERRADO -+-\n")
