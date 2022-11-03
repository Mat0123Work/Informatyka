### Matura 2021 (maj)
### 65 -> 66
### 79 -> 80
### 90 -> 65

### (((liczba-65)+1)%26)+65

### 0 -> 1
### 5 -> 6
### 10 -> 0

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
    print("Nie zrobione!")
    pass

### Zad 4.3
def zad4_3():
    print("Nie zrobione!")
    pass

### Zad 4.4
def zad4_4():
    print("Nie zrobione!")
    pass


### Wywołania:
print("Zad 4.1 wynik:")
zad4_1()
print("Mialo byc: 10")

## Te 

print("Zad 4.2 wynik:")
zad4_2()
print("Mialo byc: DOPISZ")
print("Zad 4.3 wynik:")
zad4_3()
print("Mialo byc: U, 3")
print("Zad 4.4 wynik:")
zad4_4()
print("Mialo byc: ALANTURING")