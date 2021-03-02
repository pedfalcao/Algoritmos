def mergesort(array):
    if(len(array) <= 1):
        return array
    meio = len(array) // 2
    esq = mergesort(array[:meio])
    direi = mergesort(array[meio:])
    return merge(esq, direi)

def merge(esq, direi):
    esq.append(None), direi.append(None)
    i, j = 0, 0
    array = []
    while(i < len(esq) or j < len(direi)):
        if(esq[i] is None and direi[j] is None):
            return array
        elif(esq[i] is None):
            array.append(direi[j])
            j += 1
        elif(direi[j] is None):
            array.append(esq[i])
            i += 1
        elif(esq[i] < direi[j]):
            array.append(esq[i])
            i += 1
        elif(esq[i] > direi[j]):
            array.append(direi[j])
            j += 1
        else:
            array.append(esq[i])
            array.append(direi[j])
            i += 1
            j += 1

def main():
    n = int(input())
    v = input()
    v = v.split("|")
    v_int = []
    for i in v:
        v_int.append(int(i))
    print(mergesort(v_int))

if __name__ == '__main__':
    main()
    

        
