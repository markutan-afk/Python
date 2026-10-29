class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamenhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamenhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamenhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamenhetkinen_nopeus = 0
        else:
            self.tamenhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamenhetkinen_nopeus * tuntimaara

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko

if __name__ == "__main__":
    sahko = Sahkoauto("ABC-15", 180, 52.5)
    polttis = Polttomoottoriauto("ACD-123", 165, 32.3)
    sahko.kiihdyta(120)
    polttis.kiihdyta(100)
    sahko.kulje(3)
    polttis.kulje(3)
    print(f"Sähköauton ({sahko.rekisteritunnus}) matkamittari: {sahko.kuljettu_matka} km")
    print(f"Polttomoottoriauton ({polttis.rekisteritunnus}) matkamittari: {polttis.kuljettu_matka} km")