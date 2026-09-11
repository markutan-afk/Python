vuodenajat = (
    "talvi", "talvi", "kevät", "kevät", "kevät", "kesä",
    "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"
)

kuukausi_str = input("Anna kuukauden numero (1-12): ")

try:
    kuukausi_nro = int(kuukausi_str)

    if 1 <= kuukausi_nro <= 12:

        vuodenaika = vuodenajat[kuukausi_nro - 1]
        print(f"Kuukautta {kuukausi_nro} vastaava vuodenaika on {vuodenaika}.")
    else:
        print("Virhe: Kuukauden numeron täytyy olla välillä 1-12.")

except ValueError:
    print("Virhe: Syötteen täytyy olla kokonaisluku.")