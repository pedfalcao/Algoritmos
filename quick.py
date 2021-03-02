def quicksort(array):
    if(len(array) > 1):
        pivo = 10
        indice = 0
        for i in range(len(array)-1):
            if(array[i+1] < pivo):
                indice += 1
                aux = array[i+1]
                array[i+1] = array[indice]
                array[indice] = aux
        print(array)
        aux = array[0]
        array[0] = array[indice]
        array[indice] = aux
        print(array)
        inicio = quicksort(array[:indice])
        fim = quicksort(array[indice+1:])
        inicio.append(array[indice])
        return inicio + fim
    return array


print(quicksort([90, 40, 20, 30, 10, 2, 3, 6, 100, 65, 12, 56, 13, 577, 1]))
