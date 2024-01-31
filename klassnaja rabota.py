#from datetime import date
#from random import randint

#arve_nr = date.today()  # datetime.now()
#tsekk = "Arve: " + str(arve_nr) + "\nToode Hind Kogus Summa\n"
#summa = 0
#tooded = ["Piim", "Leib", "Kommid"]  # len(tooded)=3

#for i in range(len(tooded)):
#    toode = tooded[i]
#    hind = randint(50, 150) / 100
#    ve = input("Toode: " + toode + " Hind: " + str(hind) + " Kas tahad osta?").lower()
    
#    if ve == "jah":
#        mitu = int(input("Mitu?"))
#        tsekk += toode + " " + str(hind) + " " + str(mitu) + "\n" + str(mitu * hind) + "\n"
#        summa += mitu * hind

#tsekk += "Kokku maksta: " + str(summa)
#print(tsekk)

#bussi_maht = int(input("Maht: "))  # 20

#Praktiline töö "Tsükkel"
#1------------------------
#nimi = input("Palun sisesta oma nimi: ")
#kordade_arv = int(input("Sisesta, mitu korda soovid tervitust kuulda: "))
#for kord in range(1, kordade_arv + 1):
#    print(f"Ole tervitatud, {nimi}, {kord}. korda.")

#2----------------------------
#1 variant while 
#summa_while = 0
#sisestus = input("Sisesta arv (vajuta Enter, et lõpetada): ")

#while sisestus != "":
#    arv = float(sisestus)
#    summa_while += arv
#    sisestus = input("Sisesta arv (vajuta Enter, et lõpetada): ")

#print(f"Arvude summa (while-tsükkel): {summa_while}")

#2 variant For
#summa_for = 0

#for _ in range(10):
#    sisestus = input("Sisesta arv (vajuta Enter, et lõpetada): ")
    
#    if sisestus == "":
#        break
    
#    arv = float(sisestus)
#    summa_for += arv

#print(f"Arvude summa (for-tsükkel): {summa_for}")

#3 -------------------------------------------------------
#from random import randint

#k = 0

#while True:
#    k+= 1
#    print(f"{k}. ülesanne")
#    a = randint(1, 50)
#    b = randint(1, 50)
#    p = 5
    
#    while p > 0:
#        v = int(input(f"{a} + {b} = "))
#        p-= 1

#        if v == a + b:
#            print("Õige vastus!")
#            break 
#        elif p == 0:
#            print(f"Õige vastus oli {a} + {b} = {a + b}")
#4------------------------------------------ 
#for i in range(1, 10):
#    print(f"\n{i}-nda arvu korrutustabel:")
#    for j in range(1, 10):
#        tulemus = i * j
#        print(f"{i} * {j} = {tulemus}")

#5------------------------------------------
#def loo_ruut(N):
#    for i in range(N):
#        rida = ""
#        for j in range(N):
#            if i == j or i + j == N - 1:
#                rida += "X "
#            else:
#                rida += "O "
#        print(rida)
#N = int(input("Sisesta arv N: "))
#loo_ruut(N)

#6--------------------------------
#sozdaem* 
#print("5x5 zvezdi:") 
#for i in range(5):
#    for j in range(5):
#        print("*", end=" ")
#    print()
# Treugolnik
#print("\nKasvav treugolnik:")
#for i in range(6):
#    for j in range(i):
#        print("*", end=" ")
#    print()
#treugolnik podrugomu
#print("\nKahanev treugolnik:")
#for i in range(5, 0, -1):
#    for j in range(i):
#        print("*", end=" ")
#    print()
#7-----------------------------
#import random
#loto_tulemus = ""
#for _ in range(5):
#    suvaline_number = random.randint(0, 9)
#    loto_tulemus += str(suvaline_number)

#print("Loto tulemus:", loto_tulemus)

#8----------------------------
#paaris_arvud = 0
#paaritu_arvud = 0

#for arv in range(1, 100):
#    if arv % 2 == 0:
#        print(f"{arv} on paaris arv.")
#        paaris_arvud += 1
#    else:
#        print(f"{arv} on paaritu arv.")
#        paaritu_arvud += 1

#print(f"\nPaaris arvud: {paaris_arvud}")
#print(f"Paaritu arvud: {paaritu_arvud}")

#9-------------------------------------
#for i in range(1, 10):
#    tulemus = 5 * i
#    print(f"5 x {i} = {tulemus}")
#10
#for arv in range(1, 100):
#    if arv % 5 == 0:
#        print(arv)

#11 


      