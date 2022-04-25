pocet_hodnot = int(input("Pocet hodnot : "))
smer = input("S/estupne V/zestupne ").lower()
hodnoty = []

for i in range(pocet_hodnot):
    hodnota = int(input(f"Zadej hodnotu {i + 1}. : "))
    hodnoty.append(hodnota)

if smer == "v":
    nejmensi = hodnoty[0]
    for hodnota in hodnoty:
        if hodnota < nejmensi:
            hodnoty.remove(hodnota)
            hodnoty.insert(0,hodnota)
            nejmensi = hodnota
    print(f"Serazeno vzestupne : {hodnoty}")
if smer == "s":
    nejvetsi = hodnoty[0]
    for hodnota in hodnoty:
        if hodnota > nejvetsi:
            hodnoty.remove(hodnota)
            hodnoty.insert(0,hodnota)
            nejvetsi = hodnota
    print(f"Serazeno sestupne : {hodnoty}")
