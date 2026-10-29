import random

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

class Kilpailu:
    def __init__(self, nimi, pituus_km, autolista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autolista

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu: {self.nimi} | Pituus: {self.pituus_km} km")
        print(f"{'Rekisteri':<12} | {'Huippunopeus':<14} | {'Tämänhetkinen':<14} | {'Kuljettu matka':<15}")
        print("-" * 65)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<10} km/h | {auto.tamenhetkinen_nopeus:<10} km/h | {auto.kuljettu_matka:<12.1f} km")
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

if __name__ == "__main__":
    osallistujat = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippu = random.randint(100, 200)
        osallistujat.append(Auto(rekisteri, huippu))

    romuralli = Kilpailu("Suuri romuralli", 8000, osallistujat)

    tunnit = 0
    while not romuralli.kilpailu_ohi():
        romuralli.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            print(f"--- TILANNE AJASSA {tunnit} TUNTIA ---")
            romuralli.tulosta_tilanne()

    print(f"================ KILPAILU PÄÄTTYNYT AJASSA {tunnit} TUNTIA ================")
    romuralli.tulosta_tilanne()