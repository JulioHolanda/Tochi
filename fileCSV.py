import csv

with open('projetos1-g12/studentData.csv', 'w', newline='') as data_file:
    writer = csv.writer(data_file, delimiter=',')
    
    writer.writerow(["NOME","MATRICULA","TURMA","NOTA1","NOTA2"])
    writer.writerow([
        "JULIA",
        203040,
        "5B",
        7.0,
        6.5
    ])
    writer.writerow([
        "MATEUS",
        102030,
        "5A",
        6.5,
        8.0
    ])
    writer.writerow([
        "DANILO",
        605070,
        "7C",
        9.5,
        4.0
    ])
    writer.writerow([
        "GUILHERME",
        6666666,
        "7A",
        7.5,
        5.0
    ])
    writer.writerow([
        "CADU",
        454545,
        "7A",
        3.0,
        10.0
    ])
    writer.writerow([
        "RODRIGO",
        505060,
        "7B",
        7.5,
        8.5
    ])
    writer.writerow([
        "JOSE",
        334453,
        "5A",
        8.5,
        9.0
    ])
    writer.writerow([
        "ROSA",
        551223,
        "5B",
        6.0,
        8.5
    ])

    data_file.close()

with open('projetos1-g12/junkData.csv', 'w', newline='') as data_junk:
    writer = csv.writer(data_junk, delimiter=',')
    
    writer.writerow(["NOME","MATRICULA","TURMA","NOTA1","NOTA2"])

    data_junk.close()