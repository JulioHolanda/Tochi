import csv

def media(valor1, valor2):
    media = (valor1 + valor2)/2

    return media


def pergunta_filtro():
    print("Deseja procurar por:")
    print("Nome [0]")
    print("Matrícula [1]\nTurma [2]")
    print("Nota 1 [3]\nNota 2 [4]")


def resp_filtro(x):
    if x == 0:
        resp = input("Insira o nome: ").upper()
    elif x == 1:
        resp = input("insira o número da matrícula: ")
    elif x == 2:
        resp = input("insira a turma: ").upper()
    elif x == 3:
        resp = input("insira a NOTA 1 (com casa decimal): ")
    elif x == 4:
        resp = input("insira a Nota 2 (com casa decimal): ")
        print()

    return resp


def procura():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 0 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('projetos1-g12/studentData.csv', 'r') as readData_file:
        reader = csv.reader(readData_file)

        # realiza a leitura das linhas
        for line in reader:
            if line[i] == data_hunt:
                print(line)
                existe += 1

        readData_file.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()

# addstd = add student
def addstd(nome, matricula, turma, nota1, nota2):

    list = [nome, matricula, turma, nota1, nota2]

    with open('projetos1-g12/studentData.csv', 'a') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)

        data_adder.close()


def novos_dados():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ").upper()
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))

    addstd(nome, matrc, turma, nota1, nota2)


def del_data():

    # FILTRO COMEÇA AQUI
    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i < 0 and i > 4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
# FILTRO TERMINA AQUI

    with open('projetos1-g12/studentData.csv', 'r') as original:
        reader = csv.reader(original)

        with open('projetos1-g12/transferData.csv', 'w', newline='') as rewrite:
            writer = csv.writer(rewrite)

            with open('projetos1-g12/junkData.csv', 'a', newline='') as data_junk:
                junk = csv.writer(data_junk)

                # realiza a leitura das linhas
                for line in reader:
                    if line[i] == data_hunt:
                        junk.writerow(line)
                        existe += 1
                        print(f"DELETADO: {line}")
                    else:
                        writer.writerow(line)

                data_junk.close()
            rewrite.close()
        original.close()

    with open('projetos1-g12/transferData.csv', 'r') as give:
        transfer = csv.reader(give)

        with open('projetos1-g12/studentData.csv', 'w', newline='') as recieve:
            reciver = csv.writer(recieve)

            for line in transfer:
                reciver.writerow(line)

            recieve.close()
        give.close()

        if existe == 0:
            print("\nDado errado ou não cadastrado")
    print()
