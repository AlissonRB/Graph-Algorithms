

class EdmondsKarp:

    def edmonds_karp(self, grafo):
        
        self.residual_network = self.create_residual_network(grafo)

        #retorna chaves dos vertices com rotulos 's' e 't'
        s, t = self.found_st(grafo)

        max_flow = 0

        path = self.breadth_first_search(grafo, s, t)
        while path != None:
            #Identificando a menor capacidade do caminho e adicionando-o ao fluxo atual
            menor = self.lower_capacity(path)

            max_flow = max_flow + menor

            #atualizando rede residual
            for i in range(len(path)- 1):
                u = path[i]
                v = path[i + 1]
                capacidade_atual = self.residual_network[(u, v)][0]
                nova_capacidade = capacidade_atual - menor
                self.residual_network[(u, v)][0] = nova_capacidade
                self.residual_network[(u, v)][1] += menor
            path = self.breadth_first_search(grafo, s, t)
        return max_flow

    def create_residual_network(self, grafo):
        residual_network = {}

        for aresta in grafo.arestas:
            u = aresta[0]
            v = aresta[1]
            #aresta direta
            forward_edge = grafo.peso(u, v)
            #aresta reversa
            backward_edge = 0
            capacidade = [forward_edge, backward_edge]

            residual_network[aresta] = capacidade
        return residual_network

    #busca em largura adaptada para Edmonds-Karp
    def breadth_first_search(self, grafo, s, t):
        visitados = {}
        antecessores = {}
        queue = []
        
        for v in grafo.vertices.keys():
            visitados[v] = False
            antecessores[v] = None
        
        visitados[s] = True
        queue.append(s)

        while len(queue) != 0:
            u = queue.pop(0)
            for v in grafo.vizinhos(u):
                if visitados[v] == False and self.residual_network[(u, v)][0] > 0:
                    visitados[v] = True
                    antecessores[v] = u
                    if v == t:
                        return self.construct_path(antecessores, s , t)
                    queue.append(v)        
        return None

    def construct_path(self, antecessores, s, t):
        caminho = [t]
        vertice = t

        while vertice != s:
            vertice = antecessores[vertice]
            caminho.append(vertice)
        caminho.reverse()
        #print("caminho: ", caminho)
        return caminho
    
    def found_st(self, grafo):
        s = None
        t = None

        for chave, valor in grafo.vertices.items():
            if valor == 's':
                s = chave
                break
        for chave, valor in grafo.vertices.items():
            if valor == 't':
                t = chave
                break
        if s is None or t is None:
            raise ValueError("Os vertices s e t não foram encontrados no grafo.\n")
        return s, t

    def  lower_capacity(self, caminho):
        menor_capacidade = float('inf')

        for i in range(len(caminho)- 1):
            u = caminho[i]
            v = caminho[i + 1]
            capacidade = self.residual_network[(u, v)][0]
            if capacidade < menor_capacidade:
                menor_capacidade = capacidade
        return menor_capacidade
