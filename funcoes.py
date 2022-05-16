def media(valor1, valor2):
    media = (valor1 + valor2)/2
    return media

def addstd(nome,cpf,matricula,turma,nota1,nota2):
    import csv

    with open('./studentData.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
    
        writer.writerow([nome,cpf,matricula,turma,nota1,nota2])

def dados():
    print("Insira os dados do novo estudante:")
    nome = input("NOME: ").upper()
    cpf = input("CPF: ")
    matrc = int(input("MATRÍCULA: "))
    turma = input("TURMA: ")
    nota1 = float(input("1ª nota: "))
    nota2 = float(input("2ª nota: "))
    addstd(nome,cpf,matrc,turma,nota1,nota2)