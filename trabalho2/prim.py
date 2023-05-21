from grafo import Grafo

#arvores geradoras minimas
class Prim:
    
    def algoritmo_prim(self, grafo):
        #G = (V, E, w)

        #seleciona um vertice do grafo
        vertice = list(grafo.vertices.keys())[0]

        #estrutura para antecessores
        antecessores = {}
        for chave, valor in grafo.vertices.items():
            antecessores[chave] = float("inf")
        
        #chave para cada vertice K
        chaves = {}
        for chave, rotulo in grafo.vertices.items():
            chaves[chave] = float("inf")
        
        chaves[vertice] = 0

        #definindo a estrutura de prioridades de chave minima Q

        while chaves:
            u = min(chaves, key=chaves.get)
            del  chaves[u]

            for v in grafo.vizinhos(u):
                peso = grafo.peso(u, v)

                if v in chaves and peso < chaves[v]:
                    antecessores[v] = u
                    chaves[v] = peso
        
        return antecessores
