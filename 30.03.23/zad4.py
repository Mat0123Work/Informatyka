nazwa_pliku = "przyklad.txt"


'''

with open("przyklad.txt", mode='r') as przykladowy_plik:
        for linijka in przykladowy_plik.readlines():
            print(linijka)
            print("asasdad")
            break
'''
'''
print(1, 2, 3, 4, sep="___", end="\n")
print(1, 2, 3, 4, sep="___", end="")
'''

def zad4_1():
    numer_wiersza=1
    with open(nazwa_pliku, mode='r') as przykladowy_plik:
        for linijka in przykladowy_plik.readlines():
            linijka=linijka.strip('\r\n')
            if numer_wiersza%40==0:
                print(linijka[9], end="")
            numer_wiersza+=1
    print()

zad4_1()

def ile_roznych_liter(slowo):
    powtorzone_litery = []
    for i in range(0,len(slowo)):
        if slowo[i] not in powtorzone_litery:
            powtorzone_litery.append(slowo[i])
    return len(powtorzone_litery)

def ile_roznych_liter_lepiej(slowo):
    powtorzone_litery = set()
    for i in range(0,len(slowo)):
        powtorzone_litery.add(slowo[i])
    return len(powtorzone_litery)

def ile_roznych_liter_2(slowo):
    return len(set([litera for litera in slowo]))


def zad4_2():
    licznik_max=0
    max_slowo=''
    with open(nazwa_pliku, mode='r') as przykladowy_plik:
        for linijka in przykladowy_plik.readlines():
            linijka=linijka.strip('\r\n')  
            ilosc_liter = ile_roznych_liter(linijka)
            if ilosc_liter>licznik_max:
                max_slowo=linijka
                licznik_max=ilosc_liter
    print(max_slowo,licznik_max)
zad4_2()               


def czy_oddalone_o_max_10(slowo):
    min_kod = ord("Z")  
    max_kod = ord("A")

    for litera in slowo:
        kod_litery = ord(litera)
        if(kod_litery < min_kod):
            min_kod = kod_litery
        if(kod_litery > max_kod):
            max_kod = kod_litery

    return abs(max_kod - min_kod) <= 10

def zad4_3():
    with open(nazwa_pliku, mode='r') as przykladowy_plik:
        for linijka in przykladowy_plik.readlines():
            linijka=linijka.strip('\r\n') 

            if(czy_oddalone_o_max_10(linijka)):
                print(linijka)

print("zad 3")
zad4_3()




