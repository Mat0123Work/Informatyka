### https://pl.spoj.com/problems/PP0501A/

# funkcja obliczajaca nwd dla dwoch liczb
# zrodlo: https://www.algorytm.edu.pl/algorytmy-maturalne/algorytm-eulkidesa.html
def nwd(a, b):
    while(b!=0):
        pom = b
        b = a%b
        a = pom
    return a

def main():
    # metoda input() pobiera liczbę z klawiatury
    # najpierw zapisujemy do t liczbę testow i konwertujemy ją na inta 
    # ( bo z klawiatury dostajemy stringa)
    t = int(input())
    # dopoki mamy testy do sprawdzenia
    while(t > 0):
        # input(), czyli pobieramy te dwie liczby oddzielone spacja z wejscia
        # a potem je rozdzielamy po tej pacji (split(" "))
        # wynik zapisujemy w zmiennej inpt
        inpt = input().split(" ")
        # teraz wrzucamy element 0 do a, element 1 do b
        # ale musimy je zmienić na inty, bo jak je rozdzialaliśmy
        # to to nadal sa stringi
        a = int(inpt[0])
        b = int(inpt[1])
        # printujemy wynik na ekran
        print(nwd(a,b))
        # zmniejszamy licznik testow
        t -= 1

# wywolujemy te funkcje main, zeby calosc zaczela dzialac
main()