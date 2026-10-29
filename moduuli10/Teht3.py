class Hissi:
    def __init__(self, alin_kerros: int, ylin_kerros: int):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(f"Hissi on kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(f"Hissi on kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kohde_kerros: int):
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print(f"Kerrosta {kohde_kerros} ei ole olemassa.")
            return

        while self.nykyinen < kohde_kerros:
            self.kerros_ylos()
        while self.nykyinen > kohde_kerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros: int, ylin_kerros: int, hissien_lkm: int):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = []
        
        for i in range(hissien_lkm):
            uusi_hissi = Hissi(alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissiä(self, hissin_numero: int, kohde_kerros: int):
        if hissin_numero < 1 or hissin_numero > len(self.hissit):
            print(f"Talossa ei ole hissiä numero {hissin_numero}.")
            return
            
        print(f"\n[Ajetaan hissiä {hissin_numero} kerrokseen {kohde_kerros}]")
        valittu_hissi = self.hissit[hissin_numero - 1]
        valittu_hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        print("\n!!! PALOHÄLYTYS !!! Kaikki hissit ajetaan pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit, start=1):
            print(f"\n[Palohälytys: Siirretään hissi {i}]")
            hissi.siirry_kerrokseen(self.alin)

if __name__ == "__main__":
    talo = Talo(1, 7, 3)
    talo.aja_hissiä(1, 5)
    talo.aja_hissiä(2, 7)
    talo.aja_hissiä(3, 3)
    talo.palohälytys()