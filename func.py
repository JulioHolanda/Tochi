import csv

def login():
    
    existe = 0

    resposta=input(
        '\n  -+- Tochi -+-\n\nVocê já possui uma conta? \n[S]sim\t[N]não: '
        ).lower()
    
    while resposta != 's' and resposta !="n":
        print("\n *insira uma resposta válida*")
        resposta=input(
        '\n  -+- Tochi -+-\n\nVocê já possui uma conta? \n[S]sim\t[N]não: '
        ).lower()
    
    if resposta=='s':
        while existe == 0:
            cadastrado=input('\nInsira seu nome ou email:').upper()
            
            with open('contas.csv', 'r+', newline='') as arquivo:
                leia=csv.reader(arquivo)
                
                for linha in leia:
                        if cadastrado in linha:
                            print(f'\nOlá, {linha[1]}')
                            existe +=1
                            break
                if existe == 0:    
                        print(
                            '\nUsuário não encontrado.'
                            'Crie uma conta ou tente novamente.')
                arquivo.close()

    elif resposta=='n':
        print('\n - Criação de conta - ')

        email=input('Insira um email válido: ').upper()
        with open('contas.csv', 'r+', newline='') as arquivo:
            leia=csv.reader(arquivo)

            for linha in leia:
                while email in linha:
                    email=input(
                        'Este email já está cadastrado.'
                        'Por favor, insira outro: ').upper()

            arquivo.close()   
        
        with open('contas.csv', 'r+', newline='') as arquivo:
            leia=csv.reader(arquivo)

            nome_usuario=input('Insira um nome de usuário:').upper()            
            for linha in leia:
                while nome_usuario in linha:
                    nome_usuario=input(
                        'Este nome de usuário já existe.'
                        'Por favor, insira outro: ').upper()

            arquivo.close()   

        with open('contas.csv', 'r+', newline='') as arquivo:
            leia=csv.reader(arquivo)
    

            list=[email,nome_usuario]
            writer=csv.writer(arquivo)
            writer.writerow(list)
            print('\nSua conta foi criada com sucesso!')

            arquivo.close()

def pergunta_filtro():
    print("\nDeseja procurar por:")
    print("Nome [1]")
    print("Matrícula [2]\nTurma [3]")
    print("Nota 1 [4]\nNota 2 [5]")


def pergunta_filtro_prof():
    print("\nDeseja procurar por:")
    print("Nome [1]\nCadastro [2]\nMatéria [3]\nTurma [4]")


def resp_filtro(x):
    if x == 1:
        resp = input("Insira o nome: ").upper()
    elif x == 2:
        resp = input("insira o número da matrícula: ")
    elif x == 3:
        resp = input("insira a turma: ").upper()
    elif x == 4:
        resp = input("insira a NOTA 1 (com casa decimal): ")
    elif x == 5:
        resp = input("insira a Nota 2 (com casa decimal): ")
        print()

    return resp


def resp_filtro_prof(x):
    if x == 1:
        resp = input("Insira o nome: ").upper()
    elif x == 2:
        resp = input("insira o número dde cadastro: ")
    elif x == 3:
        resp = input("insira a matéria: ")
    elif x == 4:
        resp = input("insira a turma: ").upper()
        print()

    return resp


def procura():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 1 and i > 5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('studentData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        # realiza a leitura das linhas
        for line in reader:
            if line[i-1] == data_hunt:
                print(line)
                existe += 1

        readData_file.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")


def procura_prof():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro_prof()
    i = int(input())
    print()

    while i < 1 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro_prof()
        i = int(input())
        print()

    data_hunt = resp_filtro_prof(i)
# FILTRO TERMINA AQUI

    with open('profData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        # realiza a leitura das linhas
        for line in reader:
            if line[i-1] == data_hunt:
                print(line)
                existe += 1

        readData_file.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")


def novos_dados():
    print("\nInsira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ").upper()
    nota1 = float(input("1ª nota: "))
    nota2 =float(input("2ª nota: "))

    list = [nome, matrc, turma, nota1, nota2]

    with open('studentData.csv', 'a', newline='') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)

        data_adder.close()
    print("\n- Novo estudante cadastrado - ")


def novos_dados_prof():
    print("\nInsira os dados do novo professor(a):")
    nome = input("NOME: ").upper()
    cadastr = int(input("CADASTRO: "))
    materia = input("MATÉRIA: ").upper()
    turma = input("TURMA: ").upper()
    coment = input("COMENTÁRIO: ").upper()

    list = [nome, cadastr, materia, turma, coment]

    with open('profData.csv', 'a', newline='') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)

        data_adder.close()
    print("\n- Novo professor cadastrado -")


def del_data():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 1 and i > 5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('studentData.csv', 'r') as original:
        reader = csv.reader(original)

        with open('transferData.csv', 'w', newline='') as rewrite:
            writer = csv.writer(rewrite)

            with open('junkData.csv', 'a', newline='') as data_junk:
                junk = csv.writer(data_junk)

                # realiza a leitura das linhas
                for line in reader:
                    if line[i-1] == data_hunt:
                        junk.writerow(line)
                        existe += 1
                        print(f"DELETADO: {line}")
                    else:
                        writer.writerow(line)

                data_junk.close()
            rewrite.close()
        original.close()

    with open('transferData.csv', 'r') as give:
        transfer = csv.reader(give)

        with open('studentData.csv', 'w', newline='') as recieve:
            reciver = csv.writer(recieve)

            for line in transfer:
                reciver.writerow(line)

            recieve.close()
        give.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")


def del_data_prof():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro_prof()
    i = int(input())
    print()

    while i < 1 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro_prof()
        i = int(input())
        print()

    data_hunt = resp_filtro_prof(i)
# FILTRO TERMINA AQUI

    with open('profData.csv', 'r') as original:
        reader = csv.reader(original)

        with open('transferData.csv', 'w', newline='') as rewrite:
            writer = csv.writer(rewrite)

            with open('junkProfData.csv', 'a', newline='') as data_junk:
                junk = csv.writer(data_junk)

                # realiza a leitura das linhas
                for line in reader:
                    if line[i-1] == data_hunt:
                        junk.writerow(line)
                        existe += 1
                        print(f"DELETADO: {line}")
                    else:
                        writer.writerow(line)

                data_junk.close()
            rewrite.close()
        original.close()

    with open('transferData.csv', 'r') as give:
        transfer = csv.reader(give)

        with open('profData.csv', 'w', newline='') as recieve:
            reciver = csv.writer(recieve)

            for line in transfer:
                reciver.writerow(line)

            recieve.close()
        give.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")


def listagem():

    with open('studentData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        for line in reader:
            for i in range(len(line)):
                print(f"{line[i]:^13}", end='' )
            print()

        readData_file.close()


def listagem_prof():

    with open('profData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        for line in reader:
            for i in range(len(line)):
                print(f"{line[i]:^20}", end='' )
            print()

        readData_file.close()


def listagem_espec():

    with open('especData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        for line in reader:
            for i in range(len(line)):
                print(f"{line[i]:^20}", end='' )
            print()

        readData_file.close()
        
def  metodologias(caminho):
    
    fileName = "metodologia" + str(caminho) + ".txt"

    with open(fileName, 'r') as metodologia:
        metodologiasRead = metodologia.read()
        print(metodologiasRead)
