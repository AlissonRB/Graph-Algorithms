

class BellmanFord:

    def bellman_ford(self,grafo,s):
        # Inicialização
        distancias = {}
        predecessores = {}

        for v in grafo.vertices.keys():
            distancias[v] = float('inf')
            predecessores[v] = None

        distancias[s] = 0

        # Relaxamento das arestas
        for i in range(grafo.qtdVertices() - 1):
            for u, v in grafo.arestas:
                peso = grafo.peso(u, v)
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    predecessores[v] = u
                
                #essa verificacao a mais é para o algoritmo funcionar com grafo nao direcionado
                if distancias[v] + peso < distancias[u]:
                    distancias[u] = distancias[v] + peso
                    predecessores[u] = v

        # Verificação de ciclo de peso negativo
        for u, v in grafo.arestas:
            peso = grafo.peso(u, v)
            if distancias[u] + peso < distancias[v]:
                return False, None, None
        return True, distancias, predecessores
    
    def imprimir_caminhos(self, grafo, distancias, predecessores):
        for v in grafo.vertices:
                caminho = []
                destino = v
                while destino is not None:
                    caminho.append(destino)
                    destino = predecessores[destino]
                caminho.reverse()
                distancia = (distancias[v])

                if v == destino:
                    print(f"{v}: {v}; d=0")
                else:
                    print(f"{v}: {','.join(map(str, caminho))}; d={int(distancia)}")

        

        
        
        
 


