class Hash:
    def __init__(self):
        self.hash = self.inicio()

    def hash_function(self, n, i=0):
        chave = (2001*n+10*i)%1000
        return chave, i
    def inserir(self, n, i=0):
        chave, i = self.hash_function(n, i)
        if(self.hash[chave] is None):
            self.hash[chave] = n
        else:
            while self.hash[chave] is not None:
                i+=1
                chave, i = self.hash_function(n, i)
            self.hash[chave]= n
    def inicio(self):
        lista = []
        for i in range(1000):
            lista.append(None)
        return lista
    def retornar(self):
        return self.hash
            
array = Hash()
for i in range(1000):
    array.inserir(i+1)
print(array.retornar())
