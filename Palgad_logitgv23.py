from PalgadeMoodul import *


palgad=[1200,2500,750,395,1200,2500]
inimesed=["A","B","C","D","E","D"]

while True:
    print("0-Andmed ekraanile\n1-Andmete lisamine\n2-Andmete eemaldamine\n3-Kellel on suurim palk\n4-sorteerimine\n")
    vastus=int(input())
    if vastus==0:
        naita_andmed(inimesed,palgad)
    elif vastus==1:
        inimesed,palgad=andmete_lisamine(inimesed,palgad)
    elif vastus==2:
        inimesed,palgad=andmete_kustutamine(inimesed,palgad)
    elif vastus==3:
        rikkad_inimesed=kellel_on_suurim_palk(inimesed, palgad)
        print(rikkad_inimesed)
    elif vastus==4:
        inimesed,palgad=sorteerimine(inimesed,palgad)
    elif vastus == 6:                                          #-----------------KODUTÖÖ----------------
            kellel_on_vordne_palk(inimesed, palgad)
    elif vastus == 7:
            palgaotsing_nime_jargi(inimesed, palgad)
    elif vastus==9:
        top(inimesed, palgad)
    elif vastus==10:
        keskmine(inimesed, palgad)
    elif vastus == 11:
        for i, palk in zip(inimesed, palgad):
            print(f"{i}: {tulumaks(palk)}")