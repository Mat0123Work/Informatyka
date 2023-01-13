# nazwa pliku, na ktorym pracujemy
nazwa_pliku="przyklad.txt"


# czy liczba jest potega trojki (sposobem 1, dzieleniem i resztą z dzielenia)
def czy_potega_trojki(liczba):
    while liczba>1:
        if liczba%3!=0:
           return False
        liczba /= 3
    return True

# tablica z potegami trojki
potegi_trojki = [3 ** i for i in range(0, 12)] 

# czy liczba jest potega trojki (sposobem 2, sprawdzaniem czy liczba nalezy do tablicy poteg trojki)
def czy_potega_trojki_2(liczba):
    return liczba in potegi_trojki


# zadanie 4_1
def z4_1():
    # licznik
    count=0
    # otwieramy plik
    with open (nazwa_pliku, 'r', encoding="utf-8") as otwarty_plik:
        # czytamy kazda linijke po kolei
        for line in otwarty_plik.readlines():
            # usuwamy z odczytanej linijki smieci na koncu (znaki konca wiersza itd)
            line=line.strip("\n\r")
            # sprawdzamy czy oczytana liczba jest potega trojki
            # musimy zrobic int(line), bo to co odczytalismy jest stringiem,
            # a funkcja czy_potega_trojki przyjmuje tylko inty
            if czy_potega_trojki(int(line)):
                # jesli tak, zwiekszamy licznik
                count+=1
    # na koncu zwracamy licznik (czyli ile bylo tych liczb, ktore sa potega trojki)
    return count

# drukujemy wynik funkcji 4_1
print(z4_1())

# rekurencyjna funkcja liczaca silnie
def silnia(liczba):
    if liczba <2:
        return 1
    return silnia(liczba-1)*liczba

# iteracyjna funkcja liczaca silnie
def silnia_iter(liczba):
    result = 1
    while(liczba > 0):
        result *= liczba
        liczba-=1
    return result

# bonus: jeszcze krotszy zapis tej rekurencyjnej silni
def silnia_krotko(liczba):
    return 1 if liczba < 2 else liczba*silnia_krotko(liczba-1)

# funkcja rozdzielajaca liczbe w stringu na liste jej cyfr: np."145" jest zmieniane na tablice [1,4,5]
def rozdzielenie(linijka):
    result = []
    for znak in linijka:
        result.append(int(znak))
    return result


# zadanie 4_2
def z4_2():
    # otwieramy plik
    with open (nazwa_pliku, 'r', encoding="utf-8") as otwarty_plik:
        # czytamy kazda linijke po kolei
        for line in otwarty_plik.readlines():
            # usuwamy z odczytanej linijki smieci na koncu (znaki konca wiersza itd)
            line=line.strip("\n\r")
            # rozdzielamy liczbe na jej cyfry
            rozdzielone = rozdzielenie(line)
            # musimy liczyc sume silni dla kazdej z liczb, wiec zaczynamy sume od 0
            suma = 0
            # dla kazdej cyfry naszej liczby
            for cyfra in rozdzielone:
                # liczymy silnie
                obliczona_silnia = silnia_iter(cyfra)
                # i dodajemy te silnie do sumy
                suma += obliczona_silnia
            # jesli po przejsciu tak wszystkich cyfr suma jest rowna liczbie
            if suma == int(line):
                # to ja drukujemy na ekran
                print(line)
    
# tutaj tylko wywolanie funkcji, bez printa
# to dlatego, ze ta funkcja z4_2 nic nie zwraca 
# (nie ma tam zadnego returna w kodzie)
# a jej wyniki sa drukowane przez sama funkcje 4_2
# jesli da sie tutaj też print, to wyprintuje sie na koncu "None"
z4_2()

