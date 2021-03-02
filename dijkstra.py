def dijkstra(grafo, origem, fim):
    controle = {}
    dist_atual = {}
    no_atual = {}
    nao_visitados = []
    atual = origem
    no_atual[atual] = 0

    if origem not in grafo or fim not in grafo:
        return "inf"
    
    for vertice in grafo.keys():
        nao_visitados.append(vertice)  
        dist_atual[vertice] = float("inf")

    dist_atual[atual] = [0,origem] 

    nao_visitados.remove(atual)

    while nao_visitados:
        for vizinho, peso in grafo[atual].items():
             peso_calc = peso + no_atual[atual]
             if dist_atual[vizinho] == float("inf") or dist_atual[vizinho][0] > peso_calc:
                 dist_atual[vizinho] = [peso_calc,atual]
                 controle[vizinho] = peso_calc
                 
        if controle == {} : 
            break    
        min_vizinho = extrai_min(controle)
        atual = min_vizinho[0]
        no_atual[atual] = min_vizinho[1]
        nao_visitados.remove(atual)
        del controle[atual]

    if dist_atual[fim] is float("inf"):
        return "inf"
    else:
        caminho = retorna_caminho(dist_atual, origem, fim)
        return "Partindo de %s.\nA menor distância em quilômetros é de: %d" % (caminho, dist_atual[fim][0])

def extrai_min(controle):
    minimo = None
    for i in controle.keys():
        
        if minimo is None or minimo[1]>controle[i]:
            minimo = (i, controle[i])
    return minimo

def retorna_caminho(distancias,inicio, fim):
    if  fim != inicio:
        return "%s --> %s" % (retorna_caminho(distancias,inicio, distancias[fim][1]),fim)
    else:
        return inicio

def retorna_grafo():
    arq = open("distancias.txt", mode="r", encoding="utf-8-sig")
    ler_arq = arq.readlines()
    arq.close()
    grafo = {}

    for linha in ler_arq:
        linha = linha[:-1]
        linha = linha.split(", ")
        if linha[0] not in grafo.keys():
            grafo[linha[0]] = {}
        if linha[1] not in grafo.keys():
            grafo[linha[1]] = {}
            
        if linha[1] in grafo[linha[0]].keys():
            if grafo[linha[0]][linha[1]] > float(linha[2]):
                grafo[linha[0]][linha[1]] = float(linha[2])
        else:
            grafo[linha[0]][linha[1]] = float(linha[2])

        if linha[0] in grafo[linha[1]].keys():
            if grafo[linha[1]][linha[0]] > float(linha[2]):
                grafo[linha[1]][linha[0]] = float(linha[2])
        else:
            grafo[linha[1]][linha[0]] = float(linha[2])

    return grafo

def main():
    print("Seja bem-vindo!")
    grafo = retorna_grafo()
    continuar = True
    while continuar:
        origem = input("Digite a origem desejada: ")
        destino = input("Digite o destino desejado: ")
        resultado = dijkstra(grafo, origem, destino)
        if resultado is "inf":
            print("Não há rota entre essa origem e destino :(")
        else:
            print("O menor caminho passa pelas recpectivas cidades:", resultado)
        continuar = int(input("Opções:\n1- Continuar\n2- Sair\nDigite a opção desejada: "))
        while continuar<1 or continuar>2:
            continuar = int(input("Opção inválida, tente novamente! :(\nDigite a opção desejada: "))
        if continuar is 2:
            continuar = False
    print("Até mais! :)")
        
if __name__ == '__main__':
    main()


