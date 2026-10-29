import random

class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos: int):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimäärä: int):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tuntimäärä


class Kilpailu:
    def __init__(self, nimi: str, pituus_km: float, autot: list):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nTilanne kilpailussa: {self.nimi}")
        print(f"{'Tunnus':<10} | {'Huippunopeus':<13} | {'Nykyopeus':<10} | {'Matka (km)':<10}")
        print("-" * 55)
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:<13} | {auto.tämänhetkinen_nopeus:<10} | {auto.kuljettu_matka:<10.1f}")
        print("-" * 55)

    def kilpailu_ohi(self) -> bool:
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

if __name__ == "__main__":
    autolista = []
    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippu = random.randint(100, 200)
        autolista.append(Auto(rekisteri, huippu))

    kilpailu = Kilpailu("Suuri romuralli", 8000, autolista)
    
    tunnit = 0

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        tunnit += 1

        if tunnit % 10 == 0:
            print(f"\nAikaa kulunut: {tunnit} tuntia")
            kilpailu.tulosta_tilanne()

    print(f"\nKilpailu päättyi! Aikaa kului yhteensä {tunnit} tuntia.")
    kilpailu.tulosta_tilanne()