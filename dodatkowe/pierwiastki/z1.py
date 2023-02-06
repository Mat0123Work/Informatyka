""" nazwa_pliku="potegi.txt"
def pierwiastek(a):
    while(a>=1):
        if (a ** 0.5 != 0):
            return True

def z1():
    liczba = 0
    open(plik, 'r', endocing="utf-8") as open_file
    line=line.strip("\n\r")
  if pierwiastek(int(line)):
     liczba += 1
 print z1 """

# poprawiony kod do zadania z pierwiwstkami

nazwa_pliku="potegi.txt"
def pierwiastek(a):
    return a ** 0.5

def z1():
    liczba = 0
    with open(nazwa_pliku, 'r', encoding="utf-8") as open_file:
        for line in open_file.readlines():
            line=line.strip("\n\r")
            pierw = pierwiastek(int(line))
            if(pierw == float(int(pierw))):
                liczba += 1
    return liczba

print(z1())