import math

def laske_yksikkohinta(halkaisija_cm, hinta_euroa):
    """
    Laskee ja palauttaa pizzan yksikköhinnan muodossa euroa / neliömetri.
    """

    sade_m = (halkaisija_cm / 100) / 2

    pinta_ala_m2 = math.pi * (sade_m ** 2)

    yksikkohinta = hinta_euroa / pinta_ala_m2
    return yksikkohinta


def paaohjelma():
    """
    Kysyy kahden pizzan tiedot, hyödyntää laskentafunktiota ja
    ilmoittaa, kumpi pizza antaa paremman vastineen rahalle.
    """
    print("--- Pizzojen hintavertailu ---")

    halkaisija1 = float(input("Syötä 1. pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä 1. pizzan hinta (€): "))

    halkaisija2 = float(input("Syötä 2. pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä 2. pizzan hinta (€): "))

    hinta_per_m2_pizza1 = laske_yksikkohinta(halkaisija1, hinta1)
    hinta_per_m2_pizza2 = laske_yksikkohinta(halkaisija2, hinta2)
    
    print(f"\n1. pizzan yksikköhinta: {hinta_per_m2_pizza1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {hinta_per_m2_pizza2:.2f} €/m²")

    if hinta_per_m2_pizza1 < hinta_per_m2_pizza2:
        print("\nEnsimmäinen pizza antaa paremman vastineen rahalle!")
    elif hinta_per_m2_pizza2 < hinta_per_m2_pizza1:
        print("\nToinen pizza antaa paremman vastineen rahalle!")
    else:
        print("\nMolemmat pizzat antavat tismalleen saman vastineen rahalle!")

if __name__ == "__main__":
    paaohjelma()