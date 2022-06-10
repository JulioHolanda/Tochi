import func
import webbrowser
import os
os.system("cls")

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
    print('começo while')
    while caminho == 1:
        print('\n-- ESTUDANTES --\n'
            '[1] Pesquisar\n'
            '[2] Adicionar\n'
            '[3] Remover\n'
            '[0] voltar'
        )
        caminho = int(input())
        if caminho == 1:
            func.procura()
        elif caminho == 2:
            func.novos_dados()
        elif caminho == 3:
            func.del_data()
        elif caminho == 0:
            break
    while caminho == 2:
        print(
            '\n-- PROFESSORES --\n'
            '[1] Pesquisar\n'
            '[2] Adicionar\n'
            '[3] Remover\n'
            '[0] voltar'
        )
        caminho = int(input())
        if caminho == 1:
            func.procura_prof()
        elif caminho == 2:
            func.novos_dados_prof()
        elif caminho == 3:
            func.del_data_prof()
        elif caminho == 0:
            break
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
    while caminho == 4:
        print(
            '\n-- SUPORTE --\n'
            '[1] Associação Brasileira do Defict de Atenção (ABDA)\n'
            '[2] Formulário TDHA (SNAP - IV)\n'
            '[3] Contatos Profissionais da área\n'
            '[0] voltar'
        )
        caminho = int(input())
        if caminho == 1:
            webbrowser.open("https://tdah.org.br/")
        elif caminho == 2:
            webbrowser.open("https://tdah.org.br/diagnostico-criancas/")
        elif caminho == 3:
            print('contatos aqui')
        elif caminho == 0:
            break
    
    print("\n-- Menu Principal --\nO que gostaria de acessar?")
    print(
        "[1] Estudantes\n"
        "[2] Professores\n"
        "[3] Metodologias\n"
        "[4] Suporte\n"
        "[0] Sair"
    )
    caminho = int(input())

print("fim while  ")
