from MyModule import kontrolli_kasutajanimi, loo_parool, kontrolli_parooli_tugevust

kasutajad = []
kasutaja_paroolid = {}

while True:
    print("\nValikud:")
    print("1. Registreeri")
    print("2. Logi sisse")
    print("3. Lõpeta")
    valik = input("Vali tegevus: ")

    if valik == "1":  # Registreeri
        nimi = input("Sisesta kasutajanimi: ")
        if kontrolli_kasutajanimi(nimi, kasutajad):
            print("Kasutajanimi on juba võetud!")
        else:
            parooli_valik = input("Kas soovid luua oma parooli (sisesta 'oma') või lasta programmil genereerida (sisesta 'automaatne')? ")
            if parooli_valik.lower() == 'oma':
                parool = input("Sisesta parool: ")
                if not kontrolli_parooli_tugevust(parool):
                    print("Parool ei vasta nõuetele! Parool peab sisaldama vähemalt ühte tähte, numbrit, suurtähte, väiketähte ja sümbolit.")
                    continue
            elif parooli_valik.lower() == 'automaatne':
                parool = loo_parool()
                print("Automaatselt genereeritud parool:", parool)
            else:
                print("Vigane sisend!")
                continue
                
            kasutajad.append(nimi)
            kasutaja_paroolid[nimi] = parool
            print("Kasutaja registreeritud edukalt!")
    
    elif valik == "2":  # Logi sisse
        nimi = input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            parool = input("Sisesta parool: ")
            if kasutaja_paroolid.get(nimi) == parool:
                print("Sisselogimine õnnestus!")
            else:
                print("Vale parool!")
        else:
            print("Kasutajat ei leitud!")
    
    elif valik == "3":  # Lõpeta
        print("Programm lõpetatakse.")
        break
    
    else:
        print("Vigane valik!")