

class Grafo:
    def __init__(self):
        self.vertices = {}
        self.arestas = []
        self.pesos = {}

    #retorna a quantidade de vertices
    def qtdVertices(self):
        return len(self.vertices)
    
    #retorna a quantidade de arestas
    def qtdArestas(self):
        return len(self.arestas)
    
    #retorna o grau do vertice v
    def grau(self, v):
        grau = 0
        for i in self.arestas:
            if i[0] == v or i[1] == v:
                grau += 1
        return grau

    #retorna o rotulo do vertice v
    def rotulo(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None
    
    #retorna os vizinhos do vertice v
    #para as arestas saintes
    def vizinhos(self, num_vertice):
        vizinhos = []
        for i in self.arestas:
            if i[0] == num_vertice:
                vizinhos.append(int(i[1]))
        return vizinhos
    
    #haAresta(u, v): se {u, v} ∈ E, retorna verdadeiro; se n˜ao existir, retorna falso;
    def haAresta(self, u, v):
        if (u,v) in self.arestas or (v, u) in self.arestas:
            return True
        else:
            return False
    
    #retorna o peso da aresta, senao existir retorna um valor infinito
    def peso(self, u, v):
        if (u, v) in self.pesos:
            return self.pesos[(u,v)]
        elif (v, u) in self.pesos:
            return self.pesos[(v,u)]
        else:
            return float('inf')

    def ler(self, arquivo):

        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            i = 1
            while linhas[i].strip() != '*arcs':
                indice = int(linhas[i].split()[0])
                rotulo = linhas[i].split()[1]
                self.vertices[indice] = rotulo
                i += 1
            i += 1

            while i < len(linhas):
                u, v, peso = map(float, linhas[i].split()[:3])
                aresta = (int(u),int(v))
                self.arestas.append(aresta)
                self.pesos[aresta] = peso
                i += 1

