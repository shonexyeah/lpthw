class NepravilnaValuta(Exception):
    pass

class NedovoljanIznos(Exception):
    pass

class NepoznataValuta(Exception):
    pass

class Izjedneujednu(Exception):
    pass

class Menjacnica:
    USD_TO_EUR = 0.95
    EUR_TO_USD = 1.05
    EUR_TO_RSD = 117.48
    RSD_TO_EUR = 0.0085
    USD_TO_RSD = 112.04
    RSD_TO_USD = 0.0089
    CHF_TO_RSD = 114.27

    def __init__(self, ime, adresa):
        self.ime = ime
        self.adresa = adresa

    def multiply(self, kurs, iznos):
        konvertovan_iznos = kurs * iznos
        return konvertovan_iznos

    def konverzija(self, valuta_jedan, valuta_dva, iznos):


        # TODO promeniti
        if iznos <= 99 or iznos >= 1000000:
            raise NedovoljanIznos("Druze minimum je 100, a max milionce!!")
        if valuta_jedan in ['USD', 'EUR'] and valuta_dva in ['USD', 'EUR']:
            raise NepravilnaValuta("Ne menjamo USD u EUR direktno")
        # TODO videti da je to to
        if valuta_jedan == valuta_dva:
            raise NepravilnaValuta("Ne moze se menjati ista valuta")



        # TODO PRONACI NACIN ZA KURS
        atribut = f"{valuta_jedan.upper()}_TO_{valuta_dva.upper()}"
        try:
            pravi_kurs = getattr(self, atribut)
        except AttributeError:
            raise NepoznataValuta("NEPOZNATA VALUTA")

        konvertovan_iznos = self.multiply(kurs=pravi_kurs, iznos=iznos)

        return konvertovan_iznos


class MenjacnicaBorko(Menjacnica):
    RSD_TO_USD = 5
    USD_TO_RSD = 100
    RSD_TO_EUR = 100
    EUR_TO_RSD = 100
    CHF_TO_RSD = 100
class MenjacnicaSone(Menjacnica):
    RSD_TO_USD = 10
    USD_TO_RSD = 100
