import csv

with open('./studentData.csv','r') as csv_file:
    reader = csv.reader(csv_file)

    ## pula a linha
    next(reader)

    ## realiza a leitura das linhas
    for line in reader:
        print(line)