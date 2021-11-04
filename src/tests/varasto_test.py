import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_negatiivinen_tilavuus(self):
        self.varasto = Varasto(-10)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_konstruktori_kielletty_alkusaldo(self):
        self.varasto = Varasto(10, -200)
        self.assertAlmostEqual(self.varasto.saldo, 0)

        self.varasto = Varasto(10, 200)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_olematonta_ei_voi_lisata(self):
        self.varasto.lisaa_varastoon(0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liikaa_mahdoton_lisata(self):
        self.varasto.lisaa_varastoon(100)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_olematonta_ei_voi_ottaa(self):
        otettu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(otettu_maara, 0)

        otettu_maara = self.varasto.ota_varastosta(-20)
        self.assertAlmostEqual(otettu_maara, 0)

    def test_liikaa_ei_voi_ottaa(self):
        self.varasto.lisaa_varastoon(10)
        otettu_maara = self.varasto.ota_varastosta(333)

        self.assertAlmostEqual(otettu_maara, 10)

    def test_palauttaa_oikean_kuvauksen(self):
        self.varasto.lisaa_varastoon(8)
        saatu_kuvaus = str(self.varasto)
        self.assertEqual(saatu_kuvaus, "saldo = 8, vielä tilaa 2")
