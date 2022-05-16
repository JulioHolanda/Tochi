import csv

with open('./studentData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    
    writer.writerow(["NOME","CPF","MATRICULA","TURMA","NOTA1","NOTA2"])
    writer.writerow([
        "JULIA",
        "100.240.224-69",
        203040,
        "#5B",
        7.0,
        6.5
    ])
    writer.writerow([
        "MATEUS",
        "100.240.000-33",
        102030,
        "#5A",
        5.0,
        8.0
    ])
    writer.writerow([
        "DANILO",
        "100.240.111-47",
        605070,
        "#7C",
        9.5,
        4.0
    ])
    writer.writerow([
        "GUILHRME",
        "20.294.224-17",
        6666666,
        "#7A",
        7.5,
        8.0
    ])