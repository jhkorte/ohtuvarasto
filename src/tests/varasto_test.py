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

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

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

    def test_lisataan_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(100)

        # lisättiin liikaa, pitäisi olla nyt maksimissa
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_otetaan_neg_maara(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_luodaan_varasto_neg_tilavuudella_ja_alkusaldolla(self):
        self.varasto2 = Varasto(-10, -10)
        
        self.assertAlmostEqual(self.varasto2.paljonko_mahtuu(), 0)

    def test_luodaan_varasto_kunnollisella_saldolla(self):
        self.varasto3 = Varasto(10,3)
        self.assertAlmostEqual(self.varasto3.paljonko_mahtuu(), 7)

    def test_luodaan_varasto_liian_isolla_alkusaldolla(self):
        self.varasto4 = Varasto(10,100)
        self.assertAlmostEqual(self.varasto4.paljonko_mahtuu(), 0)

    def test_lisataan_neg_maara(self):
        paljonko_mahtuu_ennen = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(-1)
        paljonko_mahtuu_jalkeen = self.varasto.paljonko_mahtuu()

        self.assertAlmostEqual(paljonko_mahtuu_ennen, paljonko_mahtuu_jalkeen)

    def test_otetaan_varastosta_liikaa(self):
        varasto_sisalto_ennen = 10 - self.varasto.paljonko_mahtuu()
        otettu_maara = self.varasto.ota_varastosta(100)
        varasto_sisalto_jalkeen = 10 - self.varasto.paljonko_mahtuu()

        self.assertAlmostEqual(varasto_sisalto_jalkeen, 0)
        self.assertAlmostEqual(varasto_sisalto_ennen, otettu_maara)

    def test_str_muoto(self):
        self.varasto.lisaa_varastoon(100)
        lause = str(self.varasto)
        lause_oikea = "saldo = 10, vielä tilaa 0"
        self.assertAlmostEqual(lause, lause_oikea)
