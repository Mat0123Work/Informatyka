def Nperm(n, A):
    H = [0 for _ in range(0,n)]
    k = 0
    for elem in A:
        if(elem > n):
            k += 1
        elif(H[elem-1] != 0):
            k += 1
        else:
            H[elem-1] += 1
    return k

assert(Nperm(3, [1,3,1]) == 1)
assert(Nperm(4, [1,4,2,5])) == 1
assert(Nperm(5, [2,2,2,2,2])) == 4
assert(Nperm(4, [4,2,3,1])) == 0
assert(Nperm(6, [5,4,1,5,6,8])) == 2
assert(Nperm(6, [8,4,9,6,5,7])) == 3