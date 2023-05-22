
class OrdenacaoTopologica:
    
    def ordenacao_topologica(self, grafo):

        #definindo as estruturas
        visitados = [False] * grafo.qtdVertices()
        tempo_inicial = [float('inf')] * grafo.qtdVertices()
        tempo_final = [float('inf')] * grafo.qtdVertices()

        #configurando tempo de inicio    
        tempo = 0

        #criando lista para os vertices ordenados topologicamente
        vertices_ordenados = []

        for u in grafo.vertices.keys():
            if not visitados[u -1]:
                #DFS-Visit- algoritmo 17
                self.algoritmo19(grafo, u, visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados)

        self.printar_ordenacao(grafo, vertices_ordenados)
        return vertices_ordenados
    
    def algoritmo19(self, grafo, v,visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados):

        visitados[v -1] = True
        tempo += 1
        tempo_inicial[v-1] = tempo

        vizinhos = grafo.vizinhos(v)

        for vizinho in vizinhos:
            if  not visitados[vizinho -1]:
                self.algoritmo19(grafo, vizinho, visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados)
        
        tempo += 1
        tempo_final[v-1] = tempo

        #adiciona o vertice v no inicio da lista vertices_ordenados
        vertices_ordenados.insert(0, v)
    
    def printar_ordenacao(self,grafo, vertices_ordenados):
        for i, v in enumerate(vertices_ordenados):
            if i != len(vertices_ordenados) - 1:
                print(grafo.rotulo(v), "-> ", end='')
            else:
                print(grafo.rotulo(v))
        print()