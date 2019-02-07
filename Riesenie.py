def spravnost_matice(matica):
    while True:
        dlzka = len(matica)
        for i in range(dlzka):
            if len(matica[0]) == len(matica[i]):
                continue
            else:
                print("Zle vložená matica. Vkladajte podľa vzoru uvedeného v dokumentácii.")
                quit(1)
        break


def spravnost_nasobenie(matica_a, matica_b):
    if len(matica_a[0]) == len(matica_b):
        return len(matica_b)
    else:
        print("Matice nie je možné navzájom násobiť")
        quit(2)


def nasobenie_matic(matica_a, matica_b):
    vyska_vysl = len(matica_a)
    sirka_vysl = len(matica_b[0])
    pocet_opakovani = spravnost_nasobenie(matica_a, matica_b)
    vysledok = 0
    sucin = []
    medzisucin = []
    for x in range(vyska_vysl):
        medzisucin = []
        for y in range(sirka_vysl):
            vysledok = 0
            for opakovanie in range(pocet_opakovani):
                vysledok += (matica_a[x][opakovanie] * matica_b[opakovanie][y])
            medzisucin.append(vysledok)
        sucin.append(medzisucin)
    return sucin


def vlozenie_matice(nazov):
    matica = []
    pocet_riadkov = int(input("Vložte počet riadkov matice {:s}: ".format(nazov)))
    print("Vkladajte riadky")
    for i in range(pocet_riadkov):
        zoznam = list(map(int, input().split()))
        matica.append(zoznam)
    spravnost_matice(matica)
    return matica

matica_A = vlozenie_matice("A")
matica_B = vlozenie_matice("B")
vysledok = nasobenie_matic(matica_A, matica_B)
print(vysledok)