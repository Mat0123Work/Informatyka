# zamiast pisać nwd z palca,
# można sobie użyć gcd z biblioteki math
# GCD - Greatest Common Divisor
from math import gcd

# przyklad tego co idzie zle jak nie damy "encoding" w funkcji open
#with open("test.txt", mode="r", encoding="utf-8") as file:
#    for line in file.readlines():
#        line = line.strip("\n\r")
#        print(line)

# funkcja licząca nwd dwóch liczb,
# algorytm wzięty z internetu
# można było też użyć funkcji 
# z biblioteki math: gcd
def nwd (a, b):
    while(b != 0):
        pom = b
        b = a%b
        a= pom
    return a

# funkcja licząca nwd dla listy liczb
def nwd_liczb (tablica):
    # jeśli mamy w tablicy jedną liczbę,
    # zwracamy tę liczbę (bo nwd dla jednej liczby to ta liczba)
    if len(tablica)==1:
        return tablica[0]
    # najpierw liczymy nwd dla dwóch liczb
    nwd_dla_liczb=nwd(tablica[0],tablica[1])
    
    # potem nwd dla tego co wyszło i trzeciej liczby,
    # potem nwd dla tego co wyszło i czwartej itd.
    for i in range(2, len(tablica)):
        nwd_dla_liczb=nwd(tablica[i], nwd_dla_liczb)
    
    # zwrot nwd na koniec
    return nwd_dla_liczb

nazwa_pliku = "przyklad.txt"

def zad4_3():
    # dwie linijki, któe otwierają plik i zapisują liczby z pliku do tablicy

    with open(nazwa_pliku ,mode='r') as file:
        tablica_liczb = [ int(x.strip("\r\n")) for x in file.readlines()] 

        #tablica_liczb = []
        #for linijka in file.readlines():
        #    linijka = linijka.strip("\r\n")
        #    tablica_liczb.append(linijka)

    # pierwsza liczba z tego maksymalnego ciągu
    first=0
    # długość tego maksymalnego ciagu
    dlugosc=0
    # nwd tego maksymalnego ciagu
    naj_liczba_calkowita=0
    # aktualny nwd jaki właśnie przetwrzamy w pętli
    aktualny_nwd=tablica_liczb[0]
    # tablica liczb, dla któej te nwd jest liczone
    tablica_aktualnych_liczb=[tablica_liczb[0]]
    # przechodzimy po elementach tablicy
    for i in range(1, len(tablica_liczb)):
        # najpierw probujemy dodac kolejna liczbe do naszej tablicy
        tablica_aktualnych_liczb.append(tablica_liczb[i])
        # i liczymy nwd dla tej tablicy z dodana liczba
        aktualny_nwd=nwd_liczb(tablica_aktualnych_liczb)

        # jesli sie zdarzylo tak, ze teraz nwd jest 1
        if aktualny_nwd==1:
            # to musimy wyrzucac liczby z tablicy do momentu az 
            # albo nwd będzie naprawione (Czyli bedzie czyms innym niz 1)
            # albo skonczy nam sie tablica, z ktorej chcemy wyrzucac elementy
            while aktualny_nwd==1 and len(tablica_aktualnych_liczb)>1:
                # obcinamy element z poczatku tablicy
                tablica_aktualnych_liczb = tablica_aktualnych_liczb[1:]
                # liczymy dla obcietej tablicy nwd
                aktualny_nwd = nwd_liczb(tablica_aktualnych_liczb)
        
        # jesli dlugosc maksymalnego ciagu jest mniejsza 
        # niz dlugosc naszej aktualnej tablocy rozpatrywanych liczb
        if dlugosc < len(tablica_aktualnych_liczb):
            # to podmieniamy wszystkie maksymalne wartosci na nowe
            dlugosc = len(tablica_aktualnych_liczb)
            first = tablica_aktualnych_liczb[0]
            naj_liczba_calkowita = aktualny_nwd

    # na koniec printujemy wszystko
    print(first)
    print(dlugosc)
    print(naj_liczba_calkowita)

zad4_3()
    




