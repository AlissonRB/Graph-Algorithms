from grafo import Grafo

class ComponentesFortementeConexas:
    
    def ordenacao_topologica(self, grafo):
        #estrutura de arestas visitadas
        visitados = {}
        for aresta in grafo.arestas:
            visitados[aresta] = False
        
        #grafo.vertices =  {1: 'Universidade Federal de Santa Catarina',
        tempo_inicial = {}
        for chave, valor in grafo.vertices.items():
            tempo_inicial[chave] = float("inf")
        
        #estrutura do tempo final da visita
        tempo_final = {}
        for chave, valor in grafo.vertices.items():
            tempo_final[chave] = float("inf")

        tempo = 0

        #criando lista para os vertices ordenados topologicamente
        vertices_ordenados = []

        for vertice in grafo.vertices:
            if visitados[vertice] == False:
                self.algoritmo19(grafo, vertice, visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados)
        
        return vertices_ordenados
    
    def algoritmo19(self, grafo, vertice,visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados):

        visitados[vertice] = True
        tempo += 1
        tempo_inicial[vertice] = tempo

        #para cada vizinho do vertice
        #se vizinho nao foi visitado
        #chama o algoritmo19 para esse vizinho

        vizinhos = grafo.vizinhos(vertice)

        for vizinho in vizinhos:
            if visitados[vizinho] == False:
                self.algoritmo_19(grafo, vizinho, visitados, tempo_inicial, tempo_final, tempo, vertices_ordenados)
        
        tempo += 1
        tempo_final = tempo

        #adiciona o vertice v no inicio da lista vertices_ordenados
        vertices_ordenados.insert(0, vertice)