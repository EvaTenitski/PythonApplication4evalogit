print("Tere! Olen sinu uus sõber Python!")
nimi=input("siseta nimi")
print(nimi + ", oi kui ilus nimi!")
indeksi_küsimus = nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "
vastus_indeksi = input(indeksi_küsimus)
if vastus_indeksi == "1":
     try:
            pikkus = float(input("Sisesta oma pikkus (cm): "))
            mass = float(input("Sisesta oma mass (kg): "))
     except ValueError:
            print("Vigane sisend. Palun sisesta arvud korrektselt.")
            exit()
indeks = mass / ((0.01 * pikkus) ** 2)


