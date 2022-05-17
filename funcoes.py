import csv

def media(valor1, valor2):
    media = (valor1 + valor2)/2
    return media

def pergunta_filtro():
    print("Deseja procurar por:")
    print("Nome [0]\nCPF [1]")
    print("Matrícula [2]\nTurma [3]")
    print("Nota 1 [4]\nNota 2 [5]")
    

def res_filtro(x):
    if x == 0:
        ansr = input("Insira o nome: ").upper()
    elif x == 1:
        ansr = input("insira o CPF: ")
    elif x == 2:
        ansr = input("insira o número da matrícula: ")
    elif x == 3:
        ansr = input("insira a turma: ")
    elif x == 4:
        ansr = input("insira a NOTA 1 (com casa decimal): ")
    elif x == 5:
        ansr = input("insira a Nota 2 (com casa decimal): ")
    return ansr

def procura():

    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i<0 and i>5:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    search = res_filtro(i)
    print()

    with open('./studentData.csv','r') as csv_file:
        reader = csv.reader(csv_file)

        ## realiza a leitura das linhas
        for line in reader:
            if line[i] == search:
                print(line)
                existe +=1
        
        if existe == 0:
            print("Dado errado ou não cadastrado\n")

        csv_file.close()
    print()

def addstd(nome,cpf,matricula,turma,nota1,nota2):
    
    list = [nome,cpf,matricula,turma,nota1,nota2]

    with open('./studentData.csv', 'a') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(list)
        
        f_object.close()

def novos_dados():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    cpf = input("CPF: ")
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ")
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    addstd(nome,cpf,matrc,turma,nota1,nota2)