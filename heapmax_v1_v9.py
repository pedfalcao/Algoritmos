def heap_max(l):
    n = int((len(l) // 2)-1)
    for i in range(n, -1,-1):
        heapify_max(l, i)

def heapify_max(l, i):
    e = dir_ou_esq(i, "e")
    d = dir_ou_esq(i, "d")
    if e < len(l) and l[e] > l[i]:
        m = e
    else:
        m = i
    if d < len(l) and l[d] > l[m]:
        m = d
    if m != i:
        l[i], l[m] = l[m], l[i]
        heapify_max(l, m)


def dir_ou_esq(i, c):
    if(c=="e"): #esquerda
        return 2 * i + 1
    elif(c=="d"): #direita
        return 2*i + 2

lista = [1,2,3,4,5,6,7,8,9] #lista já definida na questão
heap_max(lista)
print('o vetor resultante é:', lista)
