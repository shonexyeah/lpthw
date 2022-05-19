from sys import argv

script, filename = argv
txt = open(filename, 'w')


def multiply(a, b):
    print(f"Transakcija: {a} * {b}")
    return a * b


def pocetak():
    print("Dobrodosli u menjacnicu!")
    print("U narednim poljima uneti iznos, iz koje u koju valutu zelite da menjate")
    iznos = int(input("Zeljena suma: "))
    prva = input("Iz koje valute: ").lower()
    druga = input("U koju valutu: ").lower()

    if iznos <= 99 or iznos >= 1000000:
        return print("Druze minimum je 100eura, a max milionce!!")

    elif prva == "eur" and druga == "rsd":
        konverzija_eurrsd = multiply(float(iznos), 117.5)
        print(f"Vas iznos je: {konverzija_eurrsd} RSD.")
        kraj()
    elif prva == "rsd" and druga == "eur":
        konverzija_rsdeur = multiply(float(iznos), 0.0085)
        print(f"Vas iznos je: {konverzija_rsdeur} EUR.")
        kraj()
    elif prva == "usd" and druga == "huf":
        print("Nije moguce izvrsiti datu transakciju.")
        print("Molimo Vas promenite valutu.")
        pocetak()


def kraj():
    odgovor = input("Da li zelite da nastavite? [da/ne]: ").lower()

    if odgovor == "da":
        pocetak()
    else:
        print("Hvala Vam sto ste koristili menjacnicu!")


pocetak()
