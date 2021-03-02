class Grafo:
    def __init__(self, arestas, tam, direcao):
        self.vertices = {}
        self.tam = tam
        self.direcao = direcao
        self.iniciar(arestas)
        for i in range(len(arestas)):
            if arestas[i][1] not in self.vertices:
                self.vertices[arestas[i][1]] = None

    def iniciar(self, arestas):
        for tupla in arestas:
            if tupla[0] == 0:
                if tupla[0] in self.vertices:
                    self.vertices[tupla[0]].append(tupla[1])
                else:
                    self.vertices[tupla[0]] = [tupla[1]]
                    
                if self.direcao == False:
                    if tupla[1] in self.vertices:
                        self.vertices[tupla[1]].append(tupla[0])
                    else:
                        self.vertices[tupla[1]] = [tupla[0]]
        for tupla in arestas:
            if tupla[0] != 0:
                if tupla[0] in self.vertices:
                    self.vertices[tupla[0]].append(tupla[1])
                else:
                    self.vertices[tupla[0]] = [tupla[1]]
                    
                if self.direcao == False:
                    if tupla[1] in self.vertices:
                        self.vertices[tupla[1]].append(tupla[0])
                    else:
                        self.vertices[tupla[1]] = [tupla[0]]
    def BSF(self):
        marca = len(self.vertices) * [False]
        anterior = len(self.vertices) * [-1]
        vertices = []
        for i in self.vertices:
            if marca[i] == False:
                vertices.append(i)
                marca[i] = True
                while len(vertices) > 0:
                    vertice = vertices[0]
                    del vertices[0]
                    if self.vertices[vertice] != None:
                        for x in self.vertices[vertice]:
                            if marca[x] == False:
                                marca[x], anterior[x] = True, vertice
                                vertices.append(x)
        return anterior

    def DSF(self):
        marca = len(self.vertices) * [False]
        anterior = len(self.vertices) * [-1]
        for i in self.vertices:
            if marca[i] == False:
                self.busca(i, marca, anterior)
        return anterior

    def busca(self, vertice, marca, anterior):
        marca[vertice] = True
        if self.vertices[vertice] != None:
            for adjacencia in self.vertices[vertice]:
                if marca[adjacencia] == False:
                    anterior[adjacencia] = vertice
                    self.busca(adjacencia, marca, anterior)


def main():
    direcao = input()

    if direcao=="NAO DIRECIONADO":
        direcao = False
    elif direcao=="DIRECIONADO":
        direcao = True
        
    tam = int(input())
    vertices= input()
    vertices_tup = []
    aux1, aux2 = "", ""

    for i in vertices:
        if i == "(" or i == " ":
            pass
        elif i == ")":
            vertices_tup.append((int(aux1[:-1]), int(aux2)))
            aux1, aux2 = "", ""
        else:
            if aux1 != "" and aux1[-1:] == ",":
                aux2+=i
            else:
                aux1+=i

    grafo = Grafo(vertices_tup, tam, direcao)
    print(grafo.DSF())
    print(grafo.BSF())

if __name__ == '__main__':
    main()


