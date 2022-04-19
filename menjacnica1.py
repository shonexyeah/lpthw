odgovor = input("Da li zelite da nastavite? [da/ne]: ")

menja_pare = True

while menja_pare == True:
    neki_input = input("Da li zelite da nastavite?")
    if neki_input == "da":
        menja_pare = True
    else:
        menja_pare = False
        break

print("izasao iz petlje")
exit(0)
# KLJUCNI DEO PROGRAMA

def upitna_funkcija():
    iznos = input(f"Trenutno stanje je {celokupan_iznos}, unesite tacan iznos za sl.transakciju: ")
    prva = input("Iz koje valute? [EUR], [USD], [HUF], [RSD]: ")
    druga = input("U koju valutu? [EUR], [USD], [HUF], [RSD]: ")
    return prva, druga, iznos

while korisnik_zeli_da_menja == True:
    prva, druga, iznos = upitna_funkcija()
    logika_konverzije(prva_valuta = prva, druga_valuta = druga, iznos = iznos)
    upisivanje_u_bazu()

def logika_konverzije(prva_valuta, druga_valuta, iznos):
    if prva_valuta == 'EUR':
        if iznos <= 100:
            return "PUSI KURAC"

    multiply(float(iznos), 117.5)

def upisivanje_u_bazu():
    # nesto radi
    pass

menja_pare = ""
while menja_pare == True:
    menja_pare = input("Da li zelite da nastavite? [da/ne]: ")
    if menja_pare.lower() == "da":
        menja_pare = True
    else:
        menja_pare = False
        exit()
