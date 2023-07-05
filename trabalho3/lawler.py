class Lawler():

    def lawer_algorithm(self, grafo):
        X = [float('inf')] * (2 * grafo.qtdVertices())
        X[0] = 0
        S = list(range(2 * grafo.qtdVertices()))
        coloracao_minima = [-1] * grafo.qtdVertices()

        for s in S:
            G_O = []
            for u in S:
                for v in S:
                    if grafo.haAresta(u, v):
                        G_O.append((u, v))

            I = []
            for i in range(2 * grafo.qtdVertices()):
                if i not in S:
                    I.append(i)

            for i in I:
                if X[i + 1] < X[s]:
                    X[s] = X[i + 1]

            if coloracao_minima[s // 2] == -1:
                coloracao_minima[s // 2] = X[s]
        
        return coloracao_minima, max(coloracao_minima)
 