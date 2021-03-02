'''
legenda:
d - qtd de dinheiro disponivel p/ contratacoes
n - qtd de jogadores disponiveis p/ contratacao
j, js = jogador, jogadores
p, ps = pontuacao, pontuacoes
c, cs = custo, custos
r = resultado
v = valor
'''

def dinamica(d, n, js, ps, cs):
    '''
    realiza o calculo de maneira dinamica
    '''
    k = [[(0, []) for i in range(d+1)] for i in range(n+1)] 
  
    for i in range(n+1):
        for c in range(d+1): 
            if i == 0 or c == 0: 
                k[i][c] = 0, []
            elif cs[i-1] <= c:
                s1 = (ps[i-1] + k[i-1][c-cs[i-1]][0], k[i-1][c-cs[i-1]][1] + [js[i-1]] + [cs[i-1]])
                s2 = k[i-1][c]
                k[i][c] = max(s1, s2, key=lambda item: item[0]) 
            else: 
                k[i][c] = k[i-1][c] 
  
    return k[n][d]  

def main():
    js = [] #nomes dos jogadores
    cs = [] #custos dos jogadores
    ps = [] #pontuacoes dos jogadores
    d = int(input())
    n = int(input())
    for i in range(n):
        j = input()
        j = j.split(';')
        js.append(j[0])
        cs.append(int(j[1]))
        ps.append(int(j[2]))
    r = dinamica(d, n, js, ps, cs)
    print(r[0])
    v = 0
    js = []
    for i in range(len(r[1])):
        if i%2 == 1:
            v+=r[1][i]
        else:
            js.append(r[1][i])
    print(v)
    for i in js:
        print(i)
        
if __name__ == '__main__':
     main()

