#1-------------------—
import palgad_moodul 
#def lisa_inimene_ja_palk(people, salaries):
# """Lisab uue inimese ja tema palga listidesse."""
# inimene = input("Sisestage uue inimese nimi: ")
# palk = float(input("Sisestage selle inimese palk: "))
# people.append(inimene)
# salaries.append(palk)

#3------------------—
#def suurim_palk(people, salaries):
#    """Leiab kõrgeima palgaga inimese."""
#    if not people:
#        print("Andmelist on tühi.")
#        return None, None
#    max_salary = max(salaries)
#    max_index = salaries.index(max_salary)
#    max_person = people[max_index]
#    return max_person, max_salary

#4--------------------------
#def vaikseim_palk(inimesed, palgad):
#    """Leiab miinimumpalga ja selle saaja."""
#    min_palk = min(palgad)
#    indeks = palgad.index(min_palk)
#    saaja = inimesed[indeks]
#    return min_palk, saaja

#6------------------------------
#def inimesed_sama_palgaga(inimesed, palgad):
#    """Leiab ja kuvab teavet samapalgaliste inimeste kohta."""
#    sama_palgaga = {}
#    for i in range(len(inimesed)):
#        inimene = inimesed[i]
#        palk = palgad[i]
#        if palk in sama_palgaga:
#            sama_palgaga[palk].append(inimene)
#        else:
#            sama_palgaga[palk] = [inimene]
    
#    for palk, inimesed in sama_palgaga.items():
#        if len(inimesed) > 1:
#            print(f"Palk: {palk},inimeste arv : {len(inimesed)}")
#            print("Inimesi:", end=" ")
#            for inimene in inimesed:
#                print(inimene, end=", ")
#            print()

#7---------------------
#def otsi_palk_nime_jargi(inimesed, palgad, nimi):
#    """Leiab ja väljastab kõik palgad konkreetse nime jaoks."""
#    leitud = False
#    for i in range(len(inimesed)):
#        if inimesed[i] == nimi:
#            if not leitud:
#                print(f"Palgad isikule nimega {nimi}:")
#                leitud = True
#            print(palgad[i])
#    if not leitud:
#        print(f"Nime {nimi} ei leitud nimekirjast.")

