from sys import argv
from sys import exit

script, filename = argv

txt = open(filename, 'w')


def multiply(a, b):
    print(f"Transakcija: {a} * {b}")
    return a * b


print("DOBRODOSLI U 'shonexYEAH' menjacnicu, pravo mesto za klepanje!")
celokupan_iznos = input("Unesite iznos: ")
iznos = int(input(f"Trenutno stanje je {celokupan_iznos}, unesite tacan iznos za sl.transakciju: "))
prva = input("Iz koje valute? [EUR], [USD], [HUF], [RSD]: ").upper()
druga = input("U koju valutu? [EUR], [USD], [HUF], [RSD]: ").upper()


if prva == "EUR" and druga == "RSD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 117.5)
    print(f"Vas iznos je: {konverzija} RSD.")
if prva == "EUR" and druga == "USD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 1.09)
    print(f"Vas iznos je: {konverzija} USD.")
if prva == "EUR" and druga == "HUF" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 376.81)
    print(f"Vas iznos je: {konverzija} HUF.")

if prva == "RSD" and druga == "EUR" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.0085)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva == "RSD" and druga == "USD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.0092)
    print(f"Vas iznos je: {konverzija} USD.")
if prva == "RSD" and druga == "HUF" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 3.20)
    print(f"Vas iznos je: {konverzija} HUF.")

if prva == "USD" and druga == "EUR" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.92)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva.upper() == "USD" and druga.upper() == "HUF" and iznos >= 99 and iznos <= 1000000:
    konverzija = 0
    print("Nije moguce izvrsiti transakciju iz usd u HUF.")
if prva == "USD" and druga == "RSD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 108.20)
    print(f"Vas iznos je: {konverzija} RSD.")

if prva == "HUF" and druga == "EUR" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.0027)
    print(f"Vas iznos je: {konverzija} EUR.")
if prva == "HUF" and druga == "USD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.0029)
    print(f"Vas iznos je: {konverzija} USD.")
if prva == "HUF" and druga == "RSD" and iznos >= 99 and iznos <= 1000000:
    konverzija = multiply(float(iznos), 0.31)
    print(f"Vas iznos je: {konverzija} RSD.")
else:
    print("Najmanja suma za trans je 100, a najveca 1mil.")


print("\n")
txt.write("Dana 14.04.2022.")
txt.write("\n")
txt.write(f"***Uspesno ste promenili {iznos} {prva}. u {konverzija} {druga}.***")
txt.write("\n")
txt.write("\n")
txt.write("Hvala Vam sto koristite nasu menjacnicu!")
txt.close()

txt = open(filename)

print(txt.read())

print("Ne zaboravite Vas isecak!")
print("\n")
preostalo_stanje = float(celokupan_iznos) - float(iznos)
print(f"Preostalo stanje: {preostalo_stanje}")


while True:
    print("Da li zelite da nastavite? [da/ne]")
    odgovor = input(": ").lower()
    if odgovor == "da":
        odgovor == True
        print("Unesti zeljeni unos za transakciju: ")
    elif odgovor == "ne":
        odgovor == False
        print("Hvala ti sto si bio!")
        exit(0)





