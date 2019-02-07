
matica_A = [[2, 5, 8, -2, 8], [1,0, 0, 1, 8], [-5, 6, 8, 7, 4], [1, -9, -2, -1, 2], [1, 1, 1, 1, 1]]
matica_B = [[1, 2, 5, 8, 8], [6, 8, 4, 1, -2], [5, 8, -1, -2,-1], [-8, -7, 5, 5, 4], [2, 4, 5, 8, 4]]


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
        print("Matice nie je možné násobiť navzájom")
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


#spravnost_matice(matica_A)
#spravnost_matice(matica_B)
#spravnost_nasobenie(matica_A, matica_B)

vysledok = nasobenie_matic(matica_A, matica_B)
print(vysledok)