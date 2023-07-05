from collections import deque

class HopcroftKarp:

    def hopcroft_karp(self, grafo):
        distancias = {}
        mate = {}

        for v in grafo.vertices.keys():
            distancias[v] = float('inf')
            mate[v] = None

        #tamanho do emparelhamento
        m = 0

        while self.bfs(grafo, mate, distancias):
            for x in grafo.vertices.keys():
                if mate[x] is None:
                    if self.dfs(grafo, mate, distancias, x):
                        m += 1
        return (m, mate)

    #breadth_first_search adptado: verifica caminho aumentante alternante
    def bfs(self,grafo, mate, distancias):
        queue = deque()

        for x in grafo.vertices.keys():
            if mate[x] is None:
                distancias[x] = 0
                queue.append(x)
            else:
                distancias[x] = float('inf')
        distancias[None] = float('inf')

        while queue:
            x = queue.popleft()
            if distancias[x] < distancias[None]:
                for y in grafo.vizinhos(x):
                    if distancias[mate[y]] == float('inf'):
                        distancias[mate[y]] = distancias[x] + 1
                        queue.append(mate[y])
        return distancias[None] != float('inf')

    #depth_first_search
    def dfs(self, grafo, mate, distancias, x):
        if x is not None:
            for y in grafo.vizinhos(x):
                if distancias[mate[y]] == distancias[x] + 1:
                    if self.dfs(grafo, mate, distancias, mate[y]):
                        mate[y] = x
                        mate[x] = y
                        return True
            distancias[x] = float('inf')
            return False
        return True

