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
#nimed=[]
#for i in range(5) :
#    nimi=input ("Sisesta nimi: ")
#    nimed.append(nimi)
#print("Sisestatud: ", nimed)
#nimed.sort()
#print("Sorteeritud: ", nimed)
#print("Vimasena oli lisatud: ", nimi)
#nimi=input ("Mis nimi on vaja asendada? ")
#indeks=nimed.index(nimi)
#nimi=input ("Uus nimi: ")
##nimed[indeks]=nimi
#uus_nimi=input("Uus nimi:")
##nimed[indeks]=uus_nimi
#nimed=[uus_nimi if vana_nimi==nimi else vana_nimi for vana_nimi in nimed]
#nimed=set(nimed)
#print(nimed) #

#3----------------------------------------
#values = [10, 12, 20, 30, 40, 10]
#for value in values:
#    print('*' * value)

##4----------------------------------
#postiindeks = input("Napishi postiideks: ")

#if len(postiindeks) != 5 or not postiindeks.isdigit():
#    print("Nepravilnij postiindeks ! Palun napishi 5 numbriline postiindeks.")
#else:
#    maakonna_number = int(postiindeks[0])

#    if maakonna_number == 1:
#        print("Tallinn")
#        print("Ostavaetes doma!")
#    elif maakonna_number == 2:
#        print("Narva, Narva-Jõesuu")
#        print("Ostavaetes doma!")
#    elif maakonna_number == 3:
#        print("Kohtla-Järve")
#        print("Ostavaetes doma!")
#    elif maakonna_number == 5:
#        print("Tartu linn")
#        print("Nosite maski!")
#    elif maakonna_number in [4, 6, 7, 8, 9]:
#        print("Teistes Eesti piirkondades")
#        print("Nosite maski")
  
#5--------------------------------------------
#sisend = input("Napishi elementi razdelite probelob: ").split()
#if len(sisend) < 2:
#    print("Napishi minimum 2 elementa!")
#else:
#    kogus = int(input("Skolko elementov hotite pomenjat (kuni {})? ".format(len(sisend))))
#    if kogus > len(sisend):
#        print("slishkom dlinnoe.")
#    else:
#        for i in range(kogus // 2):
#            sisend[i], sisend[-i - 1] = sisend[-i - 1], sisend[i]
#        print("Novij porjadok:", sisend)
#6-----------------------------------------------------------
#arvude_loend = [10, 20, 30, 40, 50]
#maksimum_arv = max(arvude_loend)
#mõttetu_arv = maksimum_arv / len(arvude_loend)
#maksimum_arvu_indeks = arvude_loend.index(maksimum_arv)
#arvude_loend[maksimum_arvu_indeks] = mõttetu_arv
#print("Uus loend mõttetu arvuga:", arvude_loend) #nado dodelat

##7-------------------------------------------------------
#numbers_input = input("Sisestage numbrid koma abil eraldatult: ")
#numbers = [int(num.strip()) for num in numbers_input.split(',')]
#order = input("Kas soovite numbrid sorteerida kasvavas järjekorras (sisestage 'kasvav') või kahanevas järjekorras (sisestage 'kahanev')? ").strip()

#if order == 'kasvav':
#    sorted_numbers = sorted(numbers, key=abs)
#    print("Kasvavas järjekorras:", sorted_numbers)
#elif order == 'kahanev':
#    sorted_numbers = sorted(numbers, key=abs, reverse=True)
#    print("Kahanevas järjekorras:", sorted_numbers)
#else:
#    print("Sorteerimisjärjekord on valesti määratud. Palun sisestage 'kasvav' või 'kahanev'.")
#    exit()

#8---------------------------------------------------------------
#input_strings = [
#    'krot', 'belks', 'enot',
#    'a', 'aa', 'aaa', 'aaaa', 'aaaaa',
#    'qweasdqweas', 'q', 'rteww', 'ewqqqqq'
#]
#max_length = max(len(s) for s in input_strings)

#output_strings = [s.ljust(max_length, '_') for s in input_strings]
#for s in output_strings:
#    print(s)

#9----------------------------------------------------------------
#nimi = input("sisesta oma nimi: ")
#if nimi.isalpha():
#    print("Tere,", nimi.capitalize())  
#    print("Tähtede arv nimis:", len(nimi))

#    vokaalid = set("asdfghjkl") 
#    konsonandid = set("qwertyuioppäööü") 
#    vokaalide_arv = sum(1 for täht in nimi if täht.lower() in vokaalid)
#    konsonantide_arv = sum(1 for täht in nimi if täht.lower() in konsonandid)

#    print("Häälikute arv nimis:", vokaalide_arv)
#    print("Konsonantide arv nimis:", konsonantide_arv)
#    sorteeritud_tähed = sorted(set(nimi.lower())) 
#    print("Nime tähtede väljastamine tähestikulises järjekorras:", ", ".join(sorteeritud_tähed))
#else:
#    print("Nimis peaksid olema ainult tähed.")

#11------------------------------------------------------------
#tähestik = []
#for i in range(26):
#    tähestik.append(chr(ord('a') + i))
#suurenevad_tähed = []
#for i in range(len(tähestik)):
#    suurenevad_tähed.append(tähestik[i] * (i + 1))

#print("Inglise tähestik väiketähtedega:")
#print(tähestik)

#print("\nSuurenevate tähtede list:")
#print(suurenevad_tähed)

#12-----------------------------------------------------------
#from random import randint

#numbrid = [randint(1, 100) for _ in range(10)]

#min_number = min(numbrid)
#max_number = max(numbrid)

#min_index = numbrid.index(min_number)
#max_index = numbrid.index(max_number)

#numbrid[min_index], numbrid[max_index] = numbrid[max_index], numbrid[min_index]

#print("Algne loend:", numbrid)

#13-------------------------------------------------
#import random

## Список слов
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

#14--------------------------------------------------
#euroopa_pealinnad = ["London", "Moskva", "Tallinn", "Milan", "Oslp", "Riga", "Berlin", "Vena",]
#print("Evropeiskie snolitsq:")
#print("\n".join(euroopa_pealinnad))

## Добавляем две новые столицы
#uued_linna = input("dve novjie stolitsi cherez zapjatuju: ").split(',')
#euroopa_pealinnad.extend([linn.strip() for linn in uued_linna])

## Сортируем и выводим столицы с их номерами
#print("v alfavitnom porjadke:")
#for index, linn in enumerate(sorted(euroopa_pealinnad), start=1):
#    print(f"{index}. {linn}")

## Выводим общее количество столиц в списке
#print(f"V spiske {len(euroopa_pealinnad)} evropeiskih stolits.")

#15---------------------------------------------
#arvud = [1, 2, 3, 4]
#eesti = ["üks", "kaks", "kolm", "neli"]
#inglise = ["one", "two", "three", "four"]
#itaalia = ["uno", "due", "tre", "quattro"]

#print("Arv - Eesti - Inglise - Itaalia")
#for arv, e, i, it in zip(arvud, eesti, inglise, itaalia):
#    print(f"{arv} - {e} - {i} - {it}")

#arvud += [5, 6]
#eesti += ["viis", "kuus"]

#print("Sõna 'tre' eksisteerib itaalia sõnade järjendis." if 'tre' in itaalia else "Sõna 'tre' ei eksisteeri itaalia sõnade järjendis.")

#print("\nArvud tähestikulises järjekorras:", *sorted(arvud))
#print("Eesti sõnad tähestikulises järjekorras:", *sorted(eesti))
#print("Inglise sõnad tähestikulises järjekorras:", *sorted(inglise))
#print("Itaalia sõnad tähestikulises järjekorras:", *sorted(itaalia))

#16-----------------------------------------------------------------
#import random
#vastused = ["jah, kindlasti!", "jah!", "võib-olla!", "ei!"]

#print("Tere! Küsi jah/ei küsimus ja ma annan vastuse.")


#while True:
  
#    küsimus = input("Kas soovite midagi küsida? (jah/ei): ").lower()
    
#    if küsimus == "ei":
#        print("Aitäh, et külastasid meid!")
#        break
#    if küsimus != "jah":
#        print("Palun vastake 'jah' või 'ei'.")
#        continue
    
#    vastus = random.choice(vastused)
#    print("Minu vastus on:", vastus)

#17-----------------------------------------------
#sõnad = ["slovo", "kot", "auto", "tiktok", "listik", "bulka", "fon", "fonk", "salo", "komp"]

#otsingusõna = input("Sisestage otsitav sõna: ")
#for sõna in sõnad:
#    if otsingusõna in sõna:
#        print(sõna)

#18
#predmetid = []
#for i in range(5):
#    predmet = input("Sisesta predmet: ")
#    predmetid.append(predmet)

#print("Sisestatud: ", predmetid)
#predmetid.sort()
#print("Sorteeritud: ", predmetid)
#asendatav_predmet = input("Mis predmet on vaja asendada? ")
#indeks = predmetid.index(asendatav_predmet)
#uus_predmet = input("Uus predmet: ")
#predmetid[indeks] = uus_predmet
#predmetid = set(predmetid)
#print(predmetid)
