import csv

with open('studentData.csv', 'w', newline='') as data_file:
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

with open('junkData.csv', 'w', newline='') as data_junk:
    writer = csv.writer(data_junk, delimiter=',')
    
    writer.writerow(["NOME","MATRICULA","TURMA","NOTA1","NOTA2"])

    data_junk.close()

with open('profData.csv', 'w', newline='') as data_file:
    writer = csv.writer(data_file, delimiter=',')
    
    writer.writerow(["NOME","CADASTRO","MATÉRIA","TURMA","COMENTÁRIOS"])
    writer.writerow([
        "LESSA",
        203040,
        "CIÊNCIAS DA NATUREZA",
        "5B",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "ADRÉIA",
        102030,
        "CIÊNCIAS DA NATUREZA",
        "5A",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "DENNIS",
        605070,
        "MATEMÁTICA",
        "7C",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "RAFAEL",
        6666666,
        "CIÊNCIAS HUMANAS",
        "7A",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "MARCOS",
        454545,
        "CIÊNCIAS HUMANAS",
        "7A",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "ELIANA",
        505060,
        "CIÊNCIAS HUMANAS",
        "7B",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])
    writer.writerow([
        "ELIZATEBE",
        334453,
        "LINGUÁGENS",
        "5A",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ])

    data_file.close()

with open('junkProfData.csv', 'w', newline='') as data_junk:
    writer = csv.writer(data_junk, delimiter=',')
    
    writer.writerow(["NOME","MATÉRIA","CADASTRO","TURMA","COMENTÁRIOS"])

    data_junk.close()