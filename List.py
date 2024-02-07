#sõna="Programmerimine" #str
#print(sõna)
#loetelu=list(sõna)
#n=len(loetelu)
#print(f"Sõnas {sõna} on {n} tähed")
#print(loetelu)
#from random import *
#nimed=["Kadri","Mirje","Maadis","Eva","Doris"]
#while True:
#    v=input("N-andmeta näitamine\nL-andmete lisamine\nK-andmete kustutamine\n").upper()
#    if v=="N":
#    elif v=="L":
#    elif v=="K":
#         v=input("Nimi järgi (n) või järjekorranubri järgi(j) ")   
#    #    v=input("Kas kõik?(k) või Juhuslik nimi(j)").lower()
#    #    if v=="k":
#    #        print(nimed)
#        elif v=="j":
    #        print(choice(nimed))
    #elif v=="L": 
        #v=input("Kas lõppu?(k) või positsioonile(p)").lower()
        #if v=="l":
        #    nimi=input("Sisesta nimi:")
        #    nimed.append(nimi)
        #elif v=="p":
#        #        nimi=input("Sisesta nimi:")
#                #indeks=int(input("Mis positsioonile:"))
#                #nimed.insert(indeks-1,nimi)

#from random import *
#nimed=["Kadri","Mirje","Maadis","Eva","Doris"]
#while True:
#    v=input("N-andmeta näitamine\nL-andmete lisamine\nK-andmete kustutamine\n").upper()
#   if v=="N":
#   elif v=="L":
#   elif v=="K"
#       v=input("Nimi järgi (n) või järjekorranubri järgi(j) ") 
#       if v=="J"
#            While True:
#                try:
#                     indeks=int(input("mis on järjekorranumber?"))
#                     if 1>indeks=>len(nimed):
#                         break 
#                     expept Valueerror:
#                     print("vale andmetüüp")
#            nimed.pop(indeks-1)
#       elif v=="n":
#           nimi=input("sisestanimi:")
#           mitu=nimed.count(nimi)
#           if mitu>0:
#           for i in range(mitu):
#               nimed.remove(nimi)
#           else:
#               print(f"{nimi} puudub")


#_______________________________________________________
#1
#from string import * 
#vokaali=["a", "u", "j", "o", "e", "ü", "ä", "ö", "ö", "y"]
#konsonanti="qwrtpsdfghklzxcvbnmj"
#märgid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta tekst: ") #"mama"
#print(tekst)
#tekst_list=list(tekst) #["m", "a", "m", "a"]
#print (tekst_list)
#for element in tekst_list:
#    if element. lower() in vokaali:
#        v+=1
#    elif element. lower() in konsonanti:
#        k+=1
#    elif element in märgid:
#        m+=1
#    elif element==" ":
#        t+=1
#print("Vokaali:" ,v)
#print("Konsonanti:",k)
#print("Märgid:",m)
#print("Tühikud:",t)
#2---------------------------------
nimed=[]
for i in range(5) :
    nimi=input ("Sisesta nimi: ")
    nimed.append(nimi)
print("Sisestatud: ", nimed)
nimed.sort()
print("Sorteeritud: ", nimed)
print("Vimasena oli lisatud: ", nimi)
nimi=input ("Mis nimi on vaja asendada? ")
indeks=nimed.index(nimi)
nimi=input ("Uus nimi: ")
#nimed[indeks]=nimi
uus_nimi=input("Uus nimi:")
#nimed[indeks]=uus_nimi
nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
nimed=set(nimed)
print(nimed) #
