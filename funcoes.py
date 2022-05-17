def media(valor1, valor2):
    media = (valor1 + valor2)/2
    return media

def addstd(nome,cpf,matricula,turma,nota1,nota2):
    from csv import writer
    
    list = [nome,cpf,matricula,turma,nota1,nota2]

    with open('./studentData.csv', 'a') as f_object:
        writer_object = writer(f_object)
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