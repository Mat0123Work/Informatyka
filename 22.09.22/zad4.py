# ----------------------- 4_1 -----------------------
def checkFirstAndLast(number: str):
    return True if(number[0] == number[-1]) else False

def zad4_1():
    counter = 0 # Licznik elementów, które mają pierwszą i ostatnią taką samą
    found_first = False # Czy znaleźliśmy już pierwszą taką liczbę?
    first_number = 0 # Pierwsza taka liczba, któa ma pierwszą i ostatnią taką samą
    with open("liczby.txt", mode="r", encoding="utf-8") as przykladFile: # Otwieramy plik do czytania
        for line in przykladFile: # Dla każdej linijki z pliku:
            line = line.strip("\n\r") # OBcinamy znaki \n\r na końcu wiersza
            if(checkFirstAndLast(line)): # Czy pierwszy i ostatni znak dla tej liczby jest taki sam
                if(not found_first): # Czy znaleziono już pierwszą taką liczbę
                    found_first = True # Znaleziono liczbę <- true
                    first_number = line # Zapisujemy tę liczbę
                counter += 1 # Zwiększamy licznik tych liczb
    return (counter, first_number) # Zwracamy wynik

print(zad4_1())

import math
# -------------------------------
def listOfPrimeFactors(number: int):
    result = [] # Zmienna, któa trzzyma nasz przyszły wynik
    for i in range(2, math.floor(math.sqrt(number)+1)): # Pętla (może być też od 2 do number), która sprawdza po kolei dzielniki
        while(number % i == 0): # Dopóki mogę dzielić przez tą liczbę
            result.append(i) # Dodaję do listyy wynikowej
            number /= i # Dzielę liczbę number
    return result # Zwracamy

def uniqueElements(ambigList: list): # def - definiujemy funkcję, uniqueElements - nazwa funkcji, ambigList - zmienna, ktrą trzeba podać do funkcji
    return list(set(ambigList)) # Usuwamy duplikaty (najpierw zmieniamy listę na zbiór żeby usunąc duplikaty, potem znowu na listę)

def zad4_2():
    max_factors = 0 # Ilość tych dzielników (powtarzających się) P: 5
    max_factors_number = 0 # Liczba, któa dałą tyle dzielników: 420

    max_factors_different = 0 # Ilość tych dzielników (unikalnych/niepowtarzających się) P: 4
    max_factors_different_number = 0 # Liczb, któa dała tyle dzielników: 420

    with open("liczby.txt", mode="r", encoding="utf-8") as przykladFile:
        for line in przykladFile:
            line = line.strip("\n\r")
            primeFactors = listOfPrimeFactors(int(line)) # Oblicz listę tych dzielników primeFactors = [2,2,3,5,7]
            if(len(primeFactors) > max_factors): # Jeżeli trafiliśmy w lepszą ilosć dzielników, to:
                max_factors = len(primeFactors) # Zaapisujemy tę liczbę dzielników
                max_factors_number = line # Oraz liczbę, któa nam to dała
            primeFactorsDiffrent = uniqueElements(primeFactors) # Usuwamy dyplikaty w primeFactors
            if(len(primeFactorsDiffrent) > max_factors_different): # Jeżeli trafilismy na lepszą ilość unikalnych dzielników
                max_factors_different = len(primeFactorsDiffrent) # Zapisujemy tę ilość dzielnikó unikalnych
                max_factors_different_number = line # Zapisujemy liczbę, która to dała
        return (max_factors_number, max_factors, max_factors_different_number, max_factors_different) # Zwracamy wynik



# ----------------------- 4_3 -----------------------
def dig(depth:int, number: int, numList: list[int]):
    if depth == 1:
        return [[number]]
    else:
        result = []
        for i in range(0, len(numList)):
            if numList[i] == number:
                continue
            if numList[i] % number == 0:
                goodCandidates = dig(depth-1, numList[i], numList)
                result = result + [[number] + elem for elem in goodCandidates]
        return result

def zad4_3():
    myList = []
    with open("liczby.txt", mode="r", encoding="utf-8") as przykladFile:
        myList = [int(elem.strip("\n\r")) for elem in przykladFile.readlines()]
    resultCounter = 0
    print("Dobre trojki:")
    for number in myList:
        result = dig(3, number, myList)
        if result:
            resultCounter += len(result)
            print(result)
    print(f"LEN = {resultCounter}")
    resultCounter = 0
    print("Dobre piatki:")
    for number in myList:
        result = dig(5,number,myList)
        if result:
            resultCounter += len(result)
            print(result)
    print(f"LEN = {resultCounter}")