import unittest

from testiranje_borko_nebojsa import NepravilnaValuta, NedovoljanIznos, MenjacnicaBorko, MenjacnicaSone, NepoznataValuta


class TestMenjacnicaBorko(unittest.TestCase):

    mb = MenjacnicaBorko("Moneta Grujica Medic", "Sveti Trifun 15")
    ms = MenjacnicaSone("Moneta Shonex Yeah", "Sveti Trifun 18")

    def test_nepravilna_valuta(self):

        valuta_1 = "EUR"
        valuta_2 = "USD"
        iznos = 1000

        with self.assertRaises(NepravilnaValuta) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "Ne menjamo USD u EUR direktno")

    def test_ista_valuta(self):

        valuta_1 = "USD"
        valuta_2 = "USD"
        iznos = 1000

        with self.assertRaises(NepravilnaValuta) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "Ne moze se menjati ista valuta")

    def test_nedovoljan_iznos(self):
        valuta_1 = "USD"
        valuta_2 = "RSD"
        iznos = 100

        with self.assertRaises(NedovoljanIznos) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "Druze minimum je 100, a max milionce!!")

    def test_velikog_slova(self):
        valuta_1 = 'usd'
        valuta_2 = 'rsd'
        iznos = 100
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(10000, konvertovan_iznos)

    def test_nema_valute(self):
        valuta_1 = "HUF"
        valuta_2 = "RSD"
        iznos = 100

        with self.assertRaises(NepoznataValuta) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "NEPOZNATA VALUTA")

    def test_nema_valute_jedan(self):
        valuta_1 = 'USD'
        valuta_2 = 'HUF'
        iznos = 100

        with self.assertRaises(NepoznataValuta) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "NEPOZNATA VALUTA")

    def test_nema_valute_dva(self):
        valuta_1 = 'EUR'
        valuta_2 = 'HUF'
        iznos = 100

        with self.assertRaises(NepoznataValuta) as error:
            self.mb.konverzija(valuta_1, valuta_2, iznos)

        self.assertEqual(error.exception.args[0], "NEPOZNATA VALUTA")


    def test_konverzija_uspeh_jedan(self):
        valuta_1 = "USD"
        valuta_2 = "RSD"
        iznos = 100
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(10000, konvertovan_iznos)

    def test_konverzija_uspeh_dva(self):
        valuta_1 = "RSD"
        valuta_2 = "USD"
        iznos = 100
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(500, konvertovan_iznos)

        konvertovan_iznos = self.ms.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(1000, konvertovan_iznos)

    def test_konverzija_uspeh_tri(self):
        valuta_1 = "RSD"
        valuta_2 = "USD"
        iznos = 100
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(500, konvertovan_iznos)

    def test_konverzija_uspeh_cetiri(self):
        valuta_1 = "EUR"
        valuta_2 = "RSD"
        iznos = 100
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, iznos)
        self.assertEqual(10000, konvertovan_iznos)

    def test_novi_kurs(self):
        valuta_1 = "CHF"
        valuta_2 = "RSD"
        kurs = 114.27
        konvertovan_iznos = self.mb.konverzija(valuta_1, valuta_2, kurs)
        self.assertEqual(11427, konvertovan_iznos)



if __name__ == '__main__':
    unittest.main()