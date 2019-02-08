#Úloha č. 12
####Dokumentácia k programu
#####Výpočet súčinu matíc
Zadanie: \
Na vstupe sú ľubovoľné dve matice A a B. Overte, či je možné
vzhľadom na ich rozmer, vykonať ich súčin a spočítať maticu C = A * B.

####Charakteristika programu
Program slúži na násobenie dvoch uživateľom zadaných matíc. Program overuje správnosť uživateľom zadanej matice, rovnako ako aj
to, či je možné matice vzájomne násobiť. V prípade že sú tieto podmienky splnené, program po svojom prebehnutí vypíše 
výslednu maticu.

#####Zadávanie matíc
Matice sa zadávajú do programu viacerými krokmi:
1. Uživateľ zadáva maticu A.
2. Uživateľ zadá počet riadkov matice A celým číslom.
3. Použivateľ postupne zadáva riadky matice A. Jadnotlivé bunky sú pritom oddelené medzerou. Keď sa ukončí zadávanie riadka, použivateľ stlačí kláves Enter.
4. Program skontroluje, či je na každom riadku matice rovnaký počet buniek a potom pokračuje s výzvou k použivateľovi, aby zadal maticu B (Pričom sa znova opakuje rovnaký postup zadávania aj pre túto maticu).

##### Výsledok programu
Výsledkom je vypísanie matice, vo formáte pythonovského zoznamu, zložený zo zoznamov. Každý samostatný zoznam predstavuje riadok matice a jednotlivé prvky vrámci tohto zoznamu predstavujú jednotlivé bunky.
Zoznamy sa vypisujú od vrchného riadku smerom k spodnému a v rámci riadku od ľavého prvku smerom k pravému.

##### Chybové ukončenia programu (podľa exit kódov)
1. Matica nespĺňa podmienku rovnakého počtu buniek vrámci všetkých riadkov matice.
2. Matice nie je možné násobiť navzájom.
3. Zadaný počet riadkov je neplatné číslo. Treba vkladať celé číslo.
4. Vrámci zadávaných riadkov je neplatné číslo, príp. čísla. Zadávajte celé, alebo desatinné čísla.\\
##Príklad spustenia programu + dáta
V prípade spustenia súboru "Riesenie_s_datami.py" sú už vrámci programu zadané dve matice o rozmeroch 5x5 (uložené v premenných podľa výstupného formátu), ktoré program násobí. Pre použivateľsky 
zadanú maticu je potrebné použiť program "Riesenie.py", kde je možné zadať ľubovoľnú vlastnú maticu pomocou návodu uvedeného vyššie.