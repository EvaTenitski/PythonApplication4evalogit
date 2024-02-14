#from random import *
#from string import *
##6
#arvud=[1,2,3,4,5,6,122,44,5]
#print(arvud)
#max_=max(arvud)
#indeks=arvud.index(max_)
#max_=int(max_/len(arvud)) #round(max_/len(arvud))
#arvud[indeks]=max_
#print(arvud)

##5 Vahetus 
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#n=int(input("Mitu paari vahetada "))
#if len(rida)//2>=n:
#    for i in range(n):
#        abi=rida[i]
#        rida[i]=rida[len(rida)-1-i]
#        rida[len(rida)-1-i]=abi
#else:
#    print("Liiga vähe elemente")
#print(rida)

#4 Index
#Indeksid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]   
#while True:
#    indeks=input("Indeks: ")
#    if len(indeks)==5 and indeks.isdigit() and indeks[0]!="0":#int(indeks[0])!=0
#        print("Sa elad piirkonnas",Indeksid[int(indeks[0])-1])
#        if indeks[0]=="1" or indeks[0]=="2" or indeks[0]=="3": #indeks[0] in ["1","2","3"]:
#            print("Kodus")
#        else:
#            print("Maskid")
#        break 
#    else:
#        print("Sisesta indeks uuesti: ")

##3*************
#while True:
#    try:
#        N=int(input("Mitu rida loome? "))
#        break
#    except:
#        print("Vale tüüp")
#while True:
#    try:
#        S=input("Mis sümbol korrutame? ")
#        if S in punctuation:
#            break
#        else:
#            print("Vale sümbol")
#    except:
#        print("Vale sümbol")
#for i in range(N):
#    print(randint(1,25)*S)




##2
#nimed=[]
#for i in range(5):
#    nimi=input("Sisesta nimi: ")
#    nimed.append(nimi)
#print("Sisestatud: ",nimed)
#nimed.sort()
#print("Sorteeritud: ",nimed)
#print("Vimasena oli lisatud: ",nimi)
#nimi=input("Mis nimi on vaja asendada? ")#!!! Kodus
##indeks=nimed.index(nimi)
#uus_nimi=input("Uus nimi: ")
##nimed[indeks]=uus_nimi
#nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
#nimed=set(nimed)#!!! Kodus
#print(nimed)
#vanused=[]
#for i in range(5):
#    v=int(input("Vanus: "))
#    vanused.append(v)
#sum_=sum(vanused)
#min_=min(vanused)
#max_=max(vanused)
#kesk=sum_/len(vanused)
#print("Kesknime on {kesk}, \nSuurim on {max_}, \nVäiksem on {min_}, \nSumma on {sum_}")

##1

#vokaali=["a","u","i","o","e","ü","ä","ö","õ","y"]
#konsonanti="qwrtpsdfghklzxcvbnmj"
#märgid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta tekst: ") #"mama"
#print(tekst)
#tekst_list=list(tekst) #["m","a","m","a"]
#print(tekst_list)
#for element in tekst_list:
#    if element.lower() in vokaali:
#        v+=1
#    elif element.lower() in konsonanti:
#        k+=1
#    elif element in märgid:
#        m+=1
#    elif element==" ":
#        t+=1
#print("Vokaali:",v)
#print("Konsonanti:",k)
#print("Märgid:",m)
#print("Tühikud:",t)




 # Zadanie na ocenku----------------
 
#13 ----------------------------------------
#import random


#sõnad = ["eda", "kot", "petuh", "les", "utka", "doroga"]
#valitud_sõna = random.choice(sõnad)

#arvatud_tähed = ["_" for _ in valitud_sõna]
#katsete_arv = 0

#while "_" in arvatud_tähed:
#    print("Arva sõna:", " ".join(arvatud_tähed))

#    täht = input("Sisesta täht: ")
#    katsete_arv += 1
#    if täht in valitud_sõna:
#        for i, tähthaaval in enumerate(valitud_sõna):
#            if tähthaaval == täht:
#                arvatud_tähed[i] = täht
#    else:
#        print("Vale täht! Proovi uuesti.")

#print("Uraaaaa, otagadali!")
#print("Kolichestvo popitok:", katsete_arv)

#18-----------------------------------------------
#korterid = ["Kati", "Mati", "Mari", "Jüri", "Eva", "Peeter", "Liisa", "Toomas", "Anna"]

#while True:
#    korteri_number = input("Sisestage korteri number: ")

#    if len(korteri_number) == 5 and korteri_number.isdigit() and korteri_number[0] != "0":
#        nimi = korterid[int(korteri_number[0]) - 1] 
        
#        print("Selles korteris elab", nimi)
        
#        if korteri_number[0] in ["1", "2", "3"]: 
#            print("Soovitame jääda koju ja järgida ettevaatusabinõusid.")
#        else:
#            print("Soovitame kanda maske ja hoida sotsiaalset distantsi.")
        
#        break  
#    else:
#        print("Palun sisestage korrektne korteri number.")


#12
#from random import randint

#numbers = [randint(1, 100) for _ in range(10)]

#print("Algne loend:", numbers)
#min_num = max_num = numbers[0]
#min_index = max_index = 0
#for i, num in enumerate(numbers):
#    if num < min_num:
#        min_num = num
#        min_index = i
#    elif num > max_num:
#        max_num = num
#        max_index = i

#numbers[min_index] = max_num
#numbers[max_index] = min_num

#print("Muudetud loend:", numbers)