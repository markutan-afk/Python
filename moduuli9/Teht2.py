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

if __name__ == "__main__":
    uusi_auto = Auto("ABC-123", 142)

    uusi_auto.kiihdytä(30)
    uusi_auto.kiihdytä(70)
    uusi_auto.kiihdytä(50)

    print(f"Auton nopeus kiihdytysten jälkeen: {uusi_auto.tämänhetkinen_nopeus} km/h")

    uusi_auto.kiihdytä(-200)

    print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.tämänhetkinen_nopeus} km/h")