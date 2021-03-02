def kruskal(grafo):
    soma = 0
    nao_visitados = list(grafo.keys())
    arestas = lista_arestas(grafo)
    arestas_aux = arestas.copy()
    caminho = []
    
    while len(nao_visitados) != 0:
        menor = menor_aresta(arestas)
        arestas.remove(menor)
        if menor[0] in nao_visitados or menor[1] in nao_visitados:
            if menor[0] in nao_visitados:
                nao_visitados.remove(menor[0])
            if menor[1] in nao_visitados:
                nao_visitados.remove(menor[1])
            caminho.append((menor[0], menor[1]))
            soma += menor[2]


    while len(caminho) != len(grafo.keys()) - 1:
        menor = menor_aresta(arestas_aux)
        arestas_aux.remove(menor)
        p = particao(caminho, menor)
        if p:
            caminho.append((menor[0], menor[1]))
            soma += menor[2]
     
    return soma

def particao(caminho, menor):
    particoes = []
    for c in caminho:
        if particoes == []:
            particoes.append([c[0], c[1]])
        else:
            achei_0 = False
            achei_1 = False
            guarda_p0 = None
            guarda_p1 = None
            for p in range(len(particoes)):
                if achei_0 and achei_1:
                    pass
                elif c[0] in particoes[p]:
                    achei_0 = True
                    guarda_p0 = p
                elif c[1] in particoes[p]:
                    achei_1 = True
                    guarda_p1 = p
            if not achei_0 and not achei_1:
                particoes.append([c[0], c[1]])
            elif achei_0 and achei_1:
                if guarda_p0 != guarda_p1:
                    particoes.append(particoes[guarda_p0]+particoes[guarda_p1])
                    particoes.remove(particoes[guarda_p0])
                    if guarda_p0>guarda_p1:
                        particoes.remove(particoes[guarda_p1])
                    else:
                        particoes.remove(particoes[guarda_p1-1])
            elif achei_0:
                particoes[guarda_p0].append(c[1])
            else:
                particoes[guarda_p1].append(c[0])
         
    for p in particoes:
        if menor[0] in p and menor[1] in p:
            return False
        elif menor[0] in p:
            return True
        elif menor[1] in p:
            return True

def menor_aresta(lista):
    menor = None
    for aresta in lista:
        if menor == None or menor[2] > aresta[2]:
            menor = aresta
    return menor

def lista_arestas(grafo):
    arestas = []
    for v in grafo.keys():
        for i in grafo[v].items():
            arestas.append((v, i[0], i[1]))
    return arestas

def adiciona_aresta(grafo, aresta):
    if aresta[0] not in grafo.keys():
        grafo[aresta[0]] = {}
    if aresta[1] not in grafo.keys():
        grafo[aresta[1]] = {}

    if aresta[1] in grafo[aresta[0]].keys():
        if grafo[aresta[0]][aresta[1]] > int(aresta[2]):
            grafo[aresta[0]][aresta[1]] = int(aresta[2])
    else:
        grafo[aresta[0]][aresta[1]] = int(aresta[2])

    if aresta[0] in grafo[aresta[1]].keys():
        if grafo[aresta[1]][aresta[0]] > int(aresta[2]):
            grafo[aresta[1]][aresta[0]] = int(aresta[2])
       
    else:
        grafo[aresta[1]][aresta[0]] = int(aresta[2])
        
            
    return grafo    

def main():
    grafo = {}
    while True:
        try:
            aresta = input()
            if aresta != "":
                aresta = aresta.split(", ")
                grafo = adiciona_aresta(grafo, aresta)
        
        except:
            break
    resultado = kruskal(grafo)
    print(resultado)

if __name__ == '__main__':
    main()
