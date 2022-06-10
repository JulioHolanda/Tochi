import os
os.system("cls")

i = 1

while i<10:
    i+=1
    print("fora")
    while i >2 and i <8:
        i+=1
        print("dentro")
        if i==5:
            break

            