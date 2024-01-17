#1-------------------------
#1variant
#k=0
#mitu=0
#while k<15:
#    k+=1
#    n=float(input("Siseta arv nr."+str(k)))
#    if int(n)==float(n):
#        mitu+=1
 



##2variant
#k=0
#mitu=0
#while True:
#    k+=1
#    n=float(input("Siseta arv nr."+str(k)))
#    if int(n)==float(n):
#        mitu+=1
#    if k==5: break 




##3variant
#mitu=0
#for k in range(1,16):
#    n=float(input("siseta arv nr."+str(k)))
#    if int(n)==float(n):
#        mitu+=1
#print("Täisarvude kogus: ",mitu)
 
#2-------------------------------
 #1 variant 
#A = int(input("Siseta arv A: "))
#summa = 0

#for i in range(1, A + 1):
#    summa += i

#print("Kõigi naturaalarvude summa vahemikus 1 kuni", A, "võrdne", summa)

 #2 variant 
#A = int(input("Siseta arv A: "))
#summa = 0
#i = 1
#while i <=A:
#    summa += i 
#    i+=1
#print("Kõigi naturaalarvude summa vahemikus 1 kuni", A, "võrdne", summa)

 #3 variant
#A = int(input("Siseta arv A: "))
#summa = 0
#i = 1

#while True:
#    summa+= i
#    i+=1

#    if i>A:
#        break
#print("Kõigi naturaalarvude summa vahemikus 1 kuni", A, "võrdne", summa)

#3-------------------------
#1 variant
#proizvedenie=1
#for in range (8):
#    number=float (input("siseta arv:"))
#    if number >0:
#        proizvedenie*=number 
#print("Positiivsete arvude korrutis on võrdne:", proizvedenie)


#2 variant 
#korrutis = 1
#loendur = 0

#while loendur < 8:
#    number = float(input("Sisesta number: "))
    
#    if number > 0:
#        korrutis *= number
#        loendur += 1

#print("Positiivsete arvude korrutis on:", korrutis)

#3 variant 
#korrutis = 1
#loendur = 0

#while True:
#    number = float(input("Sisesta number: "))
    
#    if number > 0:
#        korrutis *= number
#        loendur += 1

#    if loendur == 8:
#        break

#print("Positiivsete arvude korrutis on:", korrutis)

#4-----------------------------------------

#1 Variant 
#for i in range(10, 21):
#    kvadraat = i ** 2
#    print(f"{i} ruut on {kvadraat}")

#2 variant 
#arv = 10

#while arv <= 20:
#    kvadraat = arv ** 2
#    print(f"{arv} ruut on {kvadraat}")
#    arv += 1

#5---------------------------------------- 
#1 Variant
#N = int(input("Sisesta arv N: "))
#summa = 0
#loendur = 0

#while loendur < N:
#    arv = float(input("Sisesta arv: "))
    
#    if arv < 0:
#        summa += arv

#    loendur += 1

#print("Negatiivsete arvude summa on:", summa)
 
#2 variant 
#N = int(input("Sisesta arv N: "))
#summa = 0

#for _ in range(N):
#    arv = float(input("Sisesta arv: "))
    
#    if arv < 0:
#        summa += arv

#print("Negatiivsete arvude summa on:", summa)




#for i in range(0,10,-2): #1.i=0; 2.i=1;...10.i=9
#    print(i)

#for i in range(15):
#    print(i,"samm")

#for i in range(10):
#    n=input("nimi:")
#    print("\tTere",n)







#vastus=""
#while vastus.lower()!="komme":
#    vastus=input("tahad komme!")

#print()

#while True: 
#    vastus=input("Tahad komme!")
#    if vastus.lower()=="komm":
#        break
#    else:
#        print("Kõik räägivad"+vastus)





#while True:
#    try:
#        pikkus=int(input("Pikkus:"))
#        laius=int(input("Laius:"))
#        if pikkus>0 and laius>0:
#            print("Pindala:",pikkus*laius)
#            print("Pikkus ja laius on sisetanud ja pindala on leinud")
#        else:
#            print("on vaja andmeid suurem kui 0")
#        break
#    except : 
#        print("On vaja int formaat kasutada!")

#print("Töö lõpp")

