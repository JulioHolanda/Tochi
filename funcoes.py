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
    return resp

def procura():

    existe = 0

    pergunta_filtro()
    i = int(input())
    print()

    while i<0 and i>4:
        print("\nINSIRA UM VALOR VÁLIDO\n")
        pergunta_filtro()
        i = int(input())
        print()

    data_hunt = resp_filtro(i)
    print()

    with open('projetos1-g12/studentData.csv','r') as readData_file:
        reader = csv.reader(readData_file)

        ## realiza a leitura das linhas
        for line in reader:
            if line[i] == data_hunt:
                print(line)
                existe +=1
        
        if existe == 0:
            print("Dado errado ou não cadastrado\n")

        readData_file.close()
    print()

# addstd = add student
def addstd(nome,matricula,turma,nota1,nota2):
    
    list = [nome,matricula,turma,nota1,nota2]

    with open('projetos1-g12/studentData.csv', 'a') as data_adder:
        writer_object = csv.writer(data_adder)
        writer_object.writerow(list)
        
        data_adder.close()

def novos_d():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ").upper()
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    addstd(nome,matrc,turma,nota1,nota2)

