import random

def laske_pii_likiarvo():
    try:
        N = int(input("Anna arvottavien pisteiden kokonaismäärä (esim. 1000000): "))
        if N <= 0:
            print("Pisteiden määrän täytyy olla positiivinen kokonaisluku.")
            return
    except ValueError:
        print("Syötteen täytyy olla kokonaisluku.")
        return

    n = 0 # 

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            n += 1

    pii_likiarvo = 4 * n / N

    print(f"\nArvottuja pisteitä yhteensä (N): {N}")
    print(f"Ympyrän sisälle osui (n): {n}")
    print(f"Laskettu piin likiarvo: {pii_likiarvo}")

if __name__ == "__main__":
    laske_pii_likiarvo()