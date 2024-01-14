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



#1 Ülesandeid: Juku
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
#from random import randint
#alghind = randint(0, 100000) / 100 #0.00 - 1000.00 
#if alghind > 700:
#    soodustus = alghind * 0.3
#    alghind-=soodustus
#alghind*=0.7
#print("Uus hind on ", alghind)

#5 Temperatuur
#temperatuur = float(input("Palun sisestage temperatuur kraadides:"))
#if temperatuur > 18:
#    print("Temperatuur on üle 18 kraadi, see on toasoojusest kõrgem.")
#else:
#    print("Temperatuur on 18 kraadi või madalam, see võib olla sobiv toasoojus talvel.")

#6 Pikkus
#pikkus = float(input("Palun sisestage oma pikkus meetrites: "))
#if pikkus<1.4:
#    print("Te olete lühike.")
#elif 1.4<=pikkus<1.6:
#    print("Teie pikkus on keskmine.")
#else:
#    print("Te olete pikk.")

#7  Pikkus ja sugu
#pikkus = float(input("Palun sisestage oma pikkus meetrites: "))
#sugu = input("Palun sisestage oma sugu ('mees' või 'naine'): ")
#if sugu=='mees':
#    if pikkus<1.85:
#        print("Te olete lühike mees.")
#    elif 1.85<=pikkus<1.97:
#        print("Teie pikkus on keskmine mehe kohta.")
#    else:
#        print("Te olete pikk mees.")
#elif sugu=='naine':
#    if pikkus<1.68:
#        print("Te olete lühike naine.")
#    elif 1.68<=pikkus<1.78:
#        print("Teie pikkus on keskmine naise kohta.")
#    else:
#        print("Te olete pikk naine.")
#else:
#    print("Palun sisestage 'mees' või 'naine' oma soo kohta.")

#8 Poes
#from random import uniform
#tooted = {
#    "bulka": 1.20,
#    "kefir": 1.30,
#    "moloko": 0.90
#}
#ostukorv = {}  # Ostukorv toodete ja kogustega
##Küsi, milliseid tooteid soovitakse osta ja mitu tükki
#for toode, hind in tooted.items():
#    vastus = input(f"Kas soovite osta {toode}? (jah/ei): ")
#    if vastus.lower() == 'jah':
#        kogus = int(input(f"Mitu tükki {toode} soovite osta? "))
#        ostukorv[toode] = {"hind": hind, "kogus": kogus}
##Arvuta kogusumma ja kuva ostutšekk
#kokku = 0
#print("\nOstutšekk:")
#print("-" * 20)
#for toode, andmed in ostukorv.items():
#    summa = andmed["hind"] * andmed["kogus"]
#    kokku += summa
#    print(f"{toode}: {andmed['kogus']} x {andmed['hind']} = {summa:.2f} eurot")
#print("-" * 20)
#print(f"Kokku: {kokku:.2f} eurot")

#11 juubel 
#sünnipaev = input("14.01.2003:")
#paev,kuu = map(int, sünnipaev.split('.'))

#if paev == 1 and kuu == 1:
#    print("Õnnitleme! Täna on uusaasta ja see võib olla juubel!")
#elif paev == 1:
#    print(f"Õnnitleme! Täna on {kuu}-kuu esimene päev ja see võib olla juubel!")
#elif kuu == 1:
#    print(f"Õnnitleme! Täna on {paev}. jaanuar ja see võib olla juubel!")
#else:
#    print("Täna ei ole juubelipäev. Palju õnne siiski!")

#12 Müük
#toote_hind = float(input("Palun sisesta toote hind eurodes: "))
#if toote_hind <= 10:
#    allahindlus_protsent = 10
#else:
#    allahindlus_protsent = 20
#allahindlus_summa = (allahindlus_protsent / 100) * toote_hind
#loplik_hind = toote_hind - allahindlus_summa
#print(f"Algselt {toote_hind}€ maksnud toote lõplik hind pärast {allahindlus_protsent}% allahindlust on {loplik_hind:.2f}€.")

#13 Jalgpall
#soo_valik = input("Kas olete mees või naine? (sisesta 'mees' või 'naine'): ").lower()
#if soo_valik == 'mees':
#    #vanust
#    vanus = int(input("Palun sisesta oma vanus: "))
#    if 16 <= vanus <= 18:
#        print("Palju õnne! Olete vastuvõetud jalgpalli meeskonda.")
#    else:
#        print("Kahjuks ei sobi teie vanus antud meeskonda.")
#elif soo_valik == 'naine':
#    print("Palju õnne! Olete vastuvõetud jalgpalli meeskonda.")
#else:
#    print("Vabandust, aga hetkel võtame vastu ainult meeskandidaate.")

#14 Busside logistika
#arv ja busside suurust
#inimeste_arv = int(input("Sisesta inimeste arv: "))
#bussi_suurus = int(input("Sisesta bussi suurus: "))
#busside_arv = inimeste_arv // bussi_suurus
#viimase_bussi_inimesed = inimeste_arv % bussi_suurus
#print(f"Vaja on {busside_arv} bussi.")
#print(f"Viimases bussis on {viimase_bussi_inimesed} inimest.")



