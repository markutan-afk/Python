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

if __name__ == "__main__":
    h = Hissi(1, 10)
    print("--- Siirrytään kerrokseen 5 ---")
    h.siirry_kerrokseen(5)
    print("\n--- Siirrytään takaisin alimpaan kerrokseen ---")
    h.siirry_kerrokseen(1)