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

l = []
for i in range(20): #a quantidade de elementos é a_1 a a_20, por isso o range é 20
    l.append(2*(i+1)*(i+1)-10*(i+1)) #i+1 para que o range inicial seja 1 e não 0 
heap_max(l)
print('o vetor resultante é:', l)
