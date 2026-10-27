class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä):
        edetty_matka = self.tämänhetkinen_nopeus * tuntimäärä

        self.kuljettu_matka += edetty_matka

if __name__ == "__main__":
    auto = Auto("ABC-123", 142)

    auto.kuljettu_matka = 2000
    auto.tämänhetkinen_nopeus = 60

    auto.kulje(1.5)

    print(f"Uusi kuljettu matka: {auto.kuljettu_matka} km")