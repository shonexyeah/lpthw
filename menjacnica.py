valuta = input("Dobar dan, koju valutu zelite da menjate? ")
print("Odlicno, vasa izabrana valuta je " + valuta)
iznos_menjanja = input("Unesti iznos koji zelite da menjate: ")
euri = int(iznos_menjanja) * 117.5
print("Vasa iznos je: " + str(euri))

ne_moze = str(9)

if iznos_menjanja < ne_moze:
    print("Druze minimum je 10 da se menja !")

# broj koji unosim za transakciju je ceo,euri = int(iznos_menjanja) * 117.5