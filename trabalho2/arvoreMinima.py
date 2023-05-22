       

#arvores geradoras minimas
class Prim:
    
    def algoritmo_prim(self, grafo):
        # Seleciona um vértice arbitrário como vértice inicial (raiz)
        r = next(iter(grafo.vertices))

        #definindo as estruturas
        antecessores = {v: None for v in grafo.vertices}
        # Valores de chave
        K = {v: float('inf') for v in grafo.vertices}  
        K[r] = 0

        # estrutura de prioridade de chave minima Q
        Q = set(grafo.vertices)

        while Q:
            u = min(Q, key=lambda v: K[v])  # Obtém o vértice com o menor valor de chave

            Q.remove(u)

            for v in grafo.vizinhos(u):
                peso_uv = grafo.peso(u, v)
                if v in Q and peso_uv < K[v]:
                    antecessores[v] = u
                    K[v] = peso_uv

        #calcula e printa o somatorio das arestas
        self.calcular_peso(antecessores, grafo)

        #printa as arestas da arvore geradora minima
        self.printar_arestas(antecessores)

        return antecessores
    
    def calcular_peso(self, predecessores, grafo):
        soma_arestas = 0
        for vertice, predecessor in predecessores.items():
            if predecessor is not None:
                soma_arestas += grafo.peso(predecessor, vertice)
        print(int(soma_arestas))
        return soma_arestas

    def printar_arestas(self, predecessores):
        arestas = []
        for vertice, predecessor in predecessores.items():
            if predecessor is not None:
                arestas.append(f"{predecessor}-{vertice}")
        print(" , ".join(arestas))