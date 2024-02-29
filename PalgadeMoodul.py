def andmete_lisamine(i:list,p:list)->any:
    """
    """
    while True:
        try:
            n=int(input("Mitu inimest"))
            if n>0: break
        except:
            print("Viga. Proovi uuesti!")
    for j in range(n):
        nimi=input("Nimi: ")
        palk=int(input("Palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p
def naita_andmed(i:list,p:list):
    """
    """
    for j in range(len(i)):
        print(i[j],"-",p[j])
def andmete_kustutamine(i:list,p:list)->any:
    """
    """
    nimi=input("Keda kustutada ära?(nimi) ")
    if nimi not in i:
        print(f"{nimi} puudub")
    else:
        for j in range(len(i)):
            if nimi in i:
                p.pop(i.index(nimi))
                i.remove(nimi)                
    return i,p
def kellel_on_suurim_palk(i:list,p:list)->list:
    """
    """
    nimed=[]
    max_palk=max(p)
    ind=p.index(max_palk)
    for palk in p:
        if max_palk==palk:
            nimi=i[p.index(palk,ind)]
            nimed.append(nimi)
            ind+=1
    return nimed
def sorteerimine(i:list,p:list)->any:
    """
    """
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if p[n]>p[m]:
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return i,p


#kodutöö-------------------------------------------------
#6-----------------
def kellel_on_vordne_palk(i:list, p:list) -> None:
    """
    Leitakse inimesed, kes saavad sama suurt palka, ja nende andmed kuvatakse ekraanil.
    """
    unikaalsed_palga_suurused = set(p)  # Leiame ainulaadsed palga suurused
    for palk in unikaalsed_palga_suurused:
        # Leiame inimesed, kellel on praegune palk
        inimesed_sama_palgaga = [i[indeks] for indeks, palga_suurus in enumerate(p) if palga_suurus == palk]
        if len(inimesed_sama_palgaga) > 1:
            print(f"Palk {palk} saavad:")
            for inimene in inimesed_sama_palgaga:
                print(inimene)
            print(f"Kokku selliseid inimesi: {len(inimesed_sama_palgaga)}\n")

#7----------------
def palgaotsing_nime_jargi(i:list, p:list) -> None:
    """
    Otsib palga inimese nime järgi ja kuvab selle ekraanil.
    """
    nimi = input("Sisesta nimi, kelle palga kohta soovid infot: ")
    palgad_inimestel = [p[index] for index, n in enumerate(i) if n == nimi]
    
    if palgad_inimestel:
        print(f"{nimi} palgad: {palgad_inimestel}")
    else:
        print(f"{nimi} ei leitud või tema palka ei ole määratud.")

#9--------------------------------------
def top(i:list,p:list):
    """
    Näitab kõige vaesemaid ja kõige rikkamaid inimesi.
    """
    sorted_indexes = sorted(range(len(p)), key=p.index)
    print("Kõige vaesemad:")
    for index in sorted_indexes[:3]:
        print(f"{i[index]} - {p[index]}")
    
    print("\nKõige rikkamad:")
    for index in sorted_indexes[-3:]:
        print(f"{i[index]} - {p[index]}")

#10----------------------------
def keskmine(i: list, p: list):
    """
    Arvutab keskmise palga ja kuvab inimese nime, kes seda saab.
    """
    keskmine_palga_suurus = sum(p) / len(p)
    print(f"Keskmine palk: {keskmine_palga_suurus}")
    
    erinevused = [abs(palk - keskmine_palga_suurus) for palk in p]
    min_erinevus = min(erinevused)
    indeks = erinevused.index(min_erinevus)
    
    keskmisele_lahim_inimene = i[indeks]
    print(f"Inimene, kes saab lähima keskmise palga: {keskmisele_lahim_inimene}")

#11-------------------------------------
def tulumaks(palk: float) -> float:
    """
    Funktsioon arvutab palga, mida inimene kätte saab pärast tulumaksu mahaarvamist Eestis.
    """
    if palk <= 5000:
        tulumaks = palk * 0.2
    elif palk <= 10000:
        tulumaks = 5000 * 0.2 + (palk - 5000) * 0.3
    else:
        tulumaks = 5000 * 0.2 + 5000 * 0.3 + (palk - 10000) * 0.4
    
    return palk - tulumaks