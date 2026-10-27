import random

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
    autot = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippu = random.randint(100, 200)
        autot.append(Auto(rekisteri, huippu))

    kilpailu_käynnissä = True
    while kilpailu_käynnissä:
        for auto in autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)

            auto.kulje(1)

            if auto.kuljettu_matka >= 10000:
                kilpailu_käynnissä = False

    print(f"{'Rekisteri':<12} | {'Huippunopeus':<14} | {'Nykyinen nopeus':<16} | {'Kuljettu matka':<15}")
    print("-" * 67)
    for auto in autot:
        print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<10} km/h | {auto.tämänhetkinen_nopeus:<11} km/h | {auto.kuljettu_matka:<12} km")