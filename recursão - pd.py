class Item:
    def __init__(self, n, v, p):
        self.n = n
        self.v = v
        self.p = p

class Array:
    def __init__(self, i):
        self.__i = i
        self.__vs = []
        self.__ps = []
        self.__c = len(self.__i)

        for item in self.__i:
            self.__vs.append(item.v)
            self.__ps.append(item.p)
            
    def __len__(self):
        return self.__c
  
    def __iter__(self):
        return (item for item in self.__i)
  
    def __getitem__(self, ind):
        return self.__i[ind]


def solucao(array, m):
    def compara(s1, s2):
        if s1[0] < s2[0]:
            return s2
        return s1
  
    def melhor(array, m, i):
        if len(array) == 0 or i < 0:
            return (0, 0, tuple())
        elif array[i].p > m:
            return melhor(array, m, i - 1)
        else:
            p_s1 = melhor(array, m - array[i].p, i - 1)
            s1 = (
            p_s1[0] + array[i].v, 
            p_s1[1] + array[i].p,
            p_s1[2] + (array[i].n,)
            )
        s2 = melhor(array, m, i - 1)
        return compara(s1, s2)

    return melhor(array, m, len(array) - 1)

def solucao_dinamica(array, m):
    def compara(s1, s2):
        if s1[0] <s2[0]:
            return s2
        return s1
    
    if len(array) == 0:
        return (0, 0, tuple())
    

    r = [None] * len(array)
    j = [None]* len(array)
    s = [None] * len(array)

    for i in range(2, len(array)):
        p_s1 = r[i-2]
        print(p_s1)
        print(array[i].p)
        s1 = (p_s1[0] + array[i].p, p_s1[1] + (array[i].p,))
        s2 = r[i-1]
        r[i] = compara(s1, s2)

    return r[len(array) - 1]

js = []
v = int(input())
n = int(input())
for i in range(n):
    j = input()
    j = j.split(";")
    j = Item(j[0], int(j[2]), int(j[1]))
    js.append(j)

array = Array(js)
s = solucao(array, v)
print(s[0])
print(s[1])
for j in s[2]:
    print(j)

print(solucao_dinamica(array, v))
