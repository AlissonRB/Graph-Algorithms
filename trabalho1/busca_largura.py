

class BuscaLargura:
    
    def busca_largura(self,grafo, s):
    #configurando todos os vertices
        
        visitados = [False] * grafo.qtdVertices()
        nivel = [float('inf')] * grafo.qtdVertices()
        antecessores = [None] * grafo.qtdVertices()

        #configurando vertice de origem
        visitados[s-1] = True 
        nivel[s-1] = 0

        #preparando a fila de visitas
        fila = []
        fila.append(s)

        #propagacao das visitas
        while len(fila) != 0:
            u = fila.pop(0)
            vizinhos = grafo.vizinhos(u)
            for v in vizinhos:
                if not visitados[v-1]:    
                    visitados[v-1] = True
                    nivel[v-1] = nivel[u-1] + 1
                    antecessores[v-1] = u
                    fila.append(v)
        return (nivel,antecessores)
        
    def imprimir(self,grafo,nivel):
        for i in range(max(nivel) + 1):
            print(i , end=": ")
            for j in range(grafo.qtdVertices()):
                if nivel[j] == i:
                    print(j+1, end=" ")
            print()