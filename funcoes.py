import csv

def media(valor1, valor2):
    media = (valor1 + valor2)/2
    return media

def filtro():
    print("Deseja procurar por:")
    print("Nome [0]")
    print("CPF [1]")
    print("Matrícula [2]")
    print("Turma [3]")
    print("Nota 1 [4]")
    print("Nota 2 [5]")

def res_filtro(x):
    if x == 0:
        ansr = input("Insira o nome: ").upper()
    elif x == 1:
        ansr = int(input("insira o CPF: "))
    elif x == 2:
        ansr = int(input("insira o número da matrícula: "))
    elif x == 3:
        ansr = input("insira a turma: ")
    elif x == 4:
        ansr = float(input("insira a NOTA 1: "))
    elif x == 5:
        ansr = float(input("insira a Nota 2: "))
    return ansr

def procura():
    i = 1
    
    filtro()
    i = int(input())

    while i<0 and i>5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        filtro()
        i = int(input())
    search = res_filtro(i)

    with open('./studentData.csv','r') as csv_file:
        reader = csv.reader(csv_file)

        ## pula a linha
        next(reader)

        ## realiza a leitura das linhas
        for line in reader:
            print(line[])

def addstd(nome,cpf,matricula,turma,nota1,nota2):
    
    list = [nome,cpf,matricula,turma,nota1,nota2]

    with open('./studentData.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(list)
        f_object.close()

def dados():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    cpf = input("CPF: ")
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ")
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    addstd(nome,cpf,matrc,turma,nota1,nota2)