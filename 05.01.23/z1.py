n = 10
A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

w = 4

def szukaj_liczby(n,A):
    for i in range(0,n):
        if (A[i]%2==0):
            return A[i]

def szukaj_liczby2(n,A):
    lewa=0
    prawa= n-1
    while(lewa<prawa):
        srodek=(lewa+prawa)//2
        if (A[srodek]%2==0):
            prawa=srodek
        else:
            lewa=srodek+1
    return A[prawa]
