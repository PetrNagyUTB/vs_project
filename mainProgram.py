"""Hlavní program."""

# Import souboru functions.py
import functions

# Zadání vstupních hodnot uživatelem a uložení je do přoměnných
xA = input("Zadej x-ovou souřadnici bodu A: ")
yA = input("Zadej y-ovou souřadnici bodu A: ")
xB = input("Zadej x-ovou souřadnici bodu B: ")
yB = input("Zadej y-ovou souřadnici bodu B: ")
xC = input("Zadej x-ovou souřadnici bodu C: ")
yC = input("Zadej y-ovou souřadnici bodu C: ")

# Podmínka pro zkontrolování vstupních hodnot
if functions.souradniceJeCislo(xA, xB, xC, yA, yB, yC) == 1:
    "Předělání vstupních hodnot na čísla typu float"
    xA = float(xA.replace(',', '.'))
    yA = float(yA.replace(',', '.'))
    xB = float(xB.replace(',', '.'))
    yB = float(yB.replace(',', '.'))
    xC = float(xC.replace(',', '.'))
    yC = float(yC.replace(',', '.'))

    # Podmínka pro zkontolování jestli je daný objekt trojúhelník
    if functions.obsahTroj(xA, xB, xC, yA, yB, yC) != 0:
        "Výpis výsledných hodnot volaných ze souboru functions.py"
        print('\nPodle zadaných souřadnic bodů se jedná o trojúhelník.\n')
        print('Souřadnice jednotlivých bodů trojúhelníku:\n')
        print(f'A[{xA},{yA}]\nB[{xB},{yB}]\nC[{xC},{yC}]\n')
        print('Délky jednotlivých stran:\n')
        print(f'c=|AB|={functions.delkaStranyAB(xA, xB, yA, yB)}')
        print(f'a=|BC|={functions.delkaStranyBC(xB, xC, yB, yC)}')
        print(f'b=|AC|={functions.delkaStranyAC(xA, xC, yA, yC)}\n')
        print('Obvod a obsah zadaného trojúhelníku:\n')
        print(f'Obvod = {functions.obvodTroj(xA, xB, xC, yA, yB, yC)}')
        print(f'Obsah = {functions.obsahTroj(xA, xB, xC, yA, yB, yC)}\n')
        print('Informace o pravoúhlosti:')

        # Podmínka pro zkontrolování jestli je trojúhelník pravoúhlý
        if functions.zkPravouhlosti == 1:
            print('Trojuhelnik je pravoúhlý.')
        else:
            print('Trojúhelník není pravoúhlý')
    else:
        print('\nPodle zadaných souřadnic bodů se nejedná o trojúhelník.\n')
else:
    print('Do souřadnic jste nezadali číslo.')
