#from random import * 


#a=randit(-100,200)
#if a%2==0: 
#    print("juhuslik arv on",a)
#    print(a,"paaris arv")
#if a>0:
#    print(a,"suurem kui 0")
#else:
#    print(a,"väikesem kui 0 või võrdne 0-ga")

#a=int(input("Protsent:"))
##<0,>100 ei soobi, 0-59-"2",60-75-"3",76-90-"4", 91-100-"5"
#if a<0 or a>100:
#    print("Viga tulemustega!")
#elif a>=0 and a<60:
#    print("Hinne 2")
#elif a>=60 and a<76:
#    print("Hinna 3")
#elif a>=76 and a<91:
#    print("Hinna 4")
#else:
#    print("Hinna 5")



#1Ülesandeid: Juku
#nimi = input("Mis on sinu nimi?")  # upper()-"JUKU", lower()-"juku", capitalize()-"Juku"

#if nimi.upper() == "JUKU":
#    print("Lähme kinno")
#    vanus = int(input("Kui vana sa oled?"))
#    if vanus < 0 or vanus >= 120:
#        print("Viga vanusega")
#    elif vanus < 6:
#        vastus = "tasuta pilet"
#        print("On vaja Jukule osta", vastus)
#    elif vanus < 14:
#        vastus = "lastepilet"
#        print("On vaja Jukule osta", vastus)
#    elif vanus < 65:
#        vastus = "täispilet"
#        print("On vaja Jukule osta", vastus)
#    else:
#        vastus = "sooduspilet"
#        print("On vaja Jukule osta", vastus)
#else:
#    print("Joonistame")

#2 Pinginaabrid
# "A", "B"
#n1 = input("Esimene nimi: ")
#n2 = input("Teine nimi: ")
#if (n1.upper() == "A" and n2.upper() == "B") or (n1.upper() == "B" and n2.upper() == "A"):
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")
#if n1.upper() in ["A", "B"] and n2.upper() in ["A", "B"]:
#    print("Pinginaabrid")
#else:
#    print("Nad ei ole naabrid")

#3
#pikkus=float(input ("Pöranda pikkus: "))
#laius=float(input ("Pôranda laius: "))
#pindala=pikkus*laius
#print ("Toa pôranda pindala on: ",pindala)
#valik=input("Kas tahad remondi teha? ")
#if valik.lower()=="jah":
#    hind=float(input ("Kui palju maksab ruutmeeter? "))
#    summa=hind*pindala
#    print("Poranda vahetamise summa on" , summa)

#4 Allahindus
alghind=randint(0,100000)/100 #0.00 - 1000.00 aif alghind>700:
soodustus=alghind*0.3
alghind×=0.7



