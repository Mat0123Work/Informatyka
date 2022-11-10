### Matura 2021 (maj)
### 65 -> 66
### 79 -> 80
### 90 -> 65

### (((liczba-65)+1)%26)+65

### 0 -> 1
### 14 -> 15
### 25 -> 0

### 
### Zad 4.1

tab=[ chr(x) for x in range(65, 91) ] # tablica liter od A do Z

# chr() <- ta funkcja robi z liczby (np. 65) literę (A)
# chr(65) -> A, chr(90) -> Z

# poniżej funkcja wykonująca polecenie, np. DOPISZ A dopisuje literę A do napisu
# w zmiennej 'polecenie' mamy polecenie wraz z parametrem tego polecenia
# może tam być np: DOPISZ Z, USUN 1, ZMIEN B itd.
# zmienna 'napis' to nasz utworzony do tej pory napis
def wykonaj_polecenie(polecenie, napis): 
    rozdzielenie=polecenie.split(" ")
    ### rozdzielenie ma taką strukturę:
    ### 0                   1
    ### [polecenie(jakieś), litera]
    if rozdzielenie[0]=="DOPISZ": # jeśli to nasze polecenie to polecenie 'DOPISZ'
        return napis+rozdzielenie[1] # to zwracamy z funkcji nasz napis, który mamy do tej pory + nowa litera
    if rozdzielenie[0]=="ZMIEN": # jeśli to nasze polecenie to polecenie 'ZMIEN'
        return napis[0:-1]+rozdzielenie[1] # to usuwamy ostatnią literę ze słowa (napis[0:-1] albo alternatywnie napis[:-1], bo to znaczy to samo) i dodajemy tą nową
    if rozdzielenie[0]=="USUN": # jeśli to nasze polecenie to 'USUN'
        return napis[0:-1]  # to po prostu zwracamy napis bez ostatniej litery (alternatywnie można napis[:-1])
    if rozdzielenie[0]=="PRZESUN": # jeśli to nasze polecenie to 'PRZESUN'
        for i in range (0,len(napis)): # to musimy przejść się przez cały napis i znaleźć literę do zamiany
            if napis[i]==rozdzielenie[1]: # jeśli trafimy na właściwą literę (która jest na pozycji i)
                x = ord(napis[i]) # zapisujemy do zmiennej x ord() od tej litery, czyli ta litera zapisana za pomocą inta
                # robimy przemapowanie (x-65), żebyśmy mieli te inty z zakresu [0;25], bo takie możemy "Zawijać"
                # potem dodajemy 1 (Bo chcemy mieć kolejną literę, A->B, C->D, Z->A itd.)
                # potem robimy modulo 26 (bo jak nie to możemy mieć tam 26, po powrocie do zakresu [65;90] dałoby nam 91, a powinno 65)
                # no i wracamy z zakresu [0;25] do zakresu [65;90]
                nowy_x = (((x-65)+1)%26)+65 
                # nowa_litera ma w sobie tą nową literę, ale w formie znaku (już nie inta)
                nowa_litera = chr(nowy_x)
                # no i 'siekamy' ten napis, czyli dzielimy go na lewą część (do tej litery co mamy zmienić)
                # i prawą część (po tej literze co mamy zmienić)
                # potem je sklejamy z tą nową literą w środku
                return napis[0:i] + nowa_litera + napis[i+1:]

def zad4_1():
    # tworzymy pusty napis (w poleceniu jest, że startowo napis jest pusty)
    napis=""
    # otwieramy plik do czytania z niego linijek
    with open("przyklad.txt", mode="r") as otwarty_plik:
        # dla każdej linijki z pliku wykonujemy:
        for linijka in otwarty_plik.readlines():
            # obcinamy znaki końca linii na końcu linijki
            linijka=linijka.strip("\r\n")
            # zapisujemy do zmiennej napis nowy napis, utworzony dzięki aktualnemu poleceniu
            # i wcześniej uzyskanemu napisowi
            napis=wykonaj_polecenie(linijka, napis)
    # wypisujemy wynik na ekran
    print(len(napis))


### Zad 4.2
def zad4_2():
    max_dlugosc=0 # To nam trzyma informacje jaka mamy ta maksymalna dlugosc (liczbowo)
    max_polecenie="" # a to jakie polecenie dało nam te maksymalna dlugosc
    aktualna_dlugosc=0 # jaka jest aktualna dlugosc dla tego polecenia to wlasnie przerabiamy
    aktualne_polecenie="" # jakie to polecenie wlasnie przerabiamy
    with open("przyklad.txt", mode="r") as otwarty_plik: # otwieramy plik zeby z niego czytac
        # dla każdej linijki z pliku wykonujemy:
        for linijka in otwarty_plik.readlines():
            # obcinamy znaki końca linii na końcu linijki
            linijka=linijka.strip("\r\n")
            # rozdzielamy te linijke z pliku na [0] -> polecenie [1] -> litera
            # ale my nie potrzebujemy tej litery, interesuja nastylko polecenia
            # dlatego od razu z tego wyciagamy tylko samo polecenie: linijka.split(" ")[0]
            # czyli w zmiennej polecenie jest teraz polecenie zapisane znakami: DOPISZ/ZMIEN itp.
            polecenie=linijka.split(" ")[0]
            # jesli aktualne nasze polecenie rozni sie od tego co wlasnie odczytalismy z pliku
            if (aktualne_polecenie!=polecenie):
                # to wtedy bedziemy zmianac nasze polecenie aktualne na te nowe z pliku, ale najpierw:
                # musimy sprawdzic czy to co uzyskalismy do tej pory nie jest przypadkiem 
                # lepsze niz to co mamy zapisane ajko maksymalne
                if (aktualna_dlugosc>max_dlugosc):
                    # jak tak, to zmieniamy te max dlugosc na to co znalezlismy do tej pory i max polecenie na nasze aktualne polecenie
                    max_dlugosc=aktualna_dlugosc
                    max_polecenie=aktualne_polecenie
                # a potem zmianiamy nasze aktualne polecenie na to co odczytalismy z pliku
                aktualne_polecenie=polecenie
                # no i resetujemy licznik na 1
                aktualna_dlugosc=1
            else: # aktualne_polecenie==polecenie
                # jak polecenie odczytane z pliku jest takie samo jak to co mamy aktualne,
                # to tylko zwiekszamy licznik
                aktualna_dlugosc+=1
        # na koniec, jak plik nam sie skonczy to jszcze trzeba sprawdzic czy przypadkiem to co czytalismy do konca pliku nie jest naszym maksimum
        # to w zasadzie ten sam if, ktory mamy w linijce 88
        if (aktualna_dlugosc>max_dlugosc):
            max_dlugosc=aktualna_dlugosc
            max_polecenie=aktualne_polecenie
    print(max_polecenie, max_dlugosc)


### Zad 4.3
def zad4_3():
    # musimy sobie utworzyc slownik, ktory bedzie nam zliczal wystapienia dla kazej litery
    # mozna to zrobic na 2 sposoby (conajmniej)
    # pierwszy sposób, wprost:
    # x = {}
    # for i in range(65, 91):
    #   x[chr(i)] = 0
    
    #alternatywnie (krócej, używając list comprehension):
    x = { chr(e):0 for e in range(65,91) }
    
    # otwieramy plik
    with open("przyklad.txt", mode="r") as otwarty_plik:
        # dla każdej linijki z pliku wykonujemy:
        for linijka in otwarty_plik.readlines():
            # obcinamy znaki końca linii na końcu linijki
            linijka=linijka.strip("\r\n")
            # tutaj znowu rozdzielamy polecenie od litery, ale teraz nie ucinamy tego do samego polecenia jak wczesniej
            polecenie=linijka.split(" ")
            # jesli nasze polecenie (czyli ten 0 element, bo na 1 elemencie jest litera) to dopisz
            if (polecenie[0]=="DOPISZ"):
                # w polecenie[1] jest litera
                # zalozmy, ze nasza linijka z pliku to DOPISZ H
                # to wtedy zmienna polecenie to będzie tablica, ktora wyglada tak:
                # ['DOPISZ', 'H']
                # jesli chcemy dla litery 'H' zwiększyć licznik, to wywołujemy element słownika x['H'], czyli x[polecenie[1]]
                # i zwiększamy wystapienie o 1, czyli += 1
                x[polecenie[1]] +=1
    # teraz szukamy najwiekszej ilosci wystapien, czyli jaka litera wystepowala najczesciej w 'DOPISZ'
    # na start max na 0
    max_dlugosc=0
    # litera, ktora wystepowala najczesciej
    max_litera=""
    # dla kazdego klucza (czyli litery) ze slownika x.keys() zwroci nam liste kluczy w slowniku,
    # czyli coś takiego: ['A', 'B', 'C', ... 'X', 'Y', 'Z']
    for litera in x.keys():
        # jesli wystapienie dla danej litery jest wieksze niz nasze dotychczas znalezione maximum
        if (x[litera]>max_dlugosc):
            # to zamianiamy nasze maksimum z tym znalezionym
            max_dlugosc=x[litera]
            max_litera=litera
    print(max_litera,max_dlugosc)

### Zad 4.4
# to zadanie ma dokładnie ten sam kod co zadanie 1. Rożnica jest oznaczona (*)
def zad4_4():
    # tworzymy pusty napis (w poleceniu jest, że startowo napis jest pusty)
    napis=""
    # otwieramy plik do czytania z niego linijek
    with open("przyklad.txt", mode="r") as otwarty_plik:
        # dla każdej linijki z pliku wykonujemy:
        for linijka in otwarty_plik.readlines():
            # obcinamy znaki końca linii na końcu linijki
            linijka=linijka.strip("\r\n")
            # zapisujemy do zmiennej napis nowy napis, utworzony dzięki aktualnemu poleceniu
            # i wcześniej uzyskanemu napisowi
            napis=wykonaj_polecenie(linijka, napis)
    # wypisujemy wynik na ekran
    #(*) tutaj jest zmiana. Tam było print(len(napis)), co chcieliśmy znać długośćutworzonego napisu
    # ale tutaj chcemy znać ten napis, więc po prostu wypisujemy napis
    print(napis)


### Wywołania:
print("Zad 4.1 wynik:")
zad4_1()
print("Mialo byc: 10")

print("Zad 4.2 wynik:")
zad4_2()
print("Mialo byc: DOPISZ")
print("Zad 4.3 wynik:")
zad4_3()
print("Mialo byc: U, 3")
print("Zad 4.4 wynik:")
zad4_4()
print("Mialo byc: ALANTURING")