#arquivo salvo
#recebe um grafo,imprime 0/1, e o ciclo se existir
class CicloEuleriano:
    def ciclo_euleriano(self,grafo):
        #algoritmo de hierholzer

        #estrutura de arestas visitadas 
        visitadas = {}
        for aresta in grafo.arestas:
            visitadas[aresta] = False

        #seleciona um vertice do grafo
        v = list(grafo.vertices.keys())[0]

        r, ciclo = self.buscar_subciclo_euleriano(grafo,v,visitadas)

        if r is False:
            return False, []

        return True, ciclo
    

    def buscar_subciclo_euleriano(self,grafo,v,visitados):
        ciclo = [v]
        t = v
        
        #procura uma aresta nao marcada
        while True:
            u = None
            ha_aresta = False

            for aresta, visitado in visitados.items():
                if v in aresta and not visitado:
                    ha_aresta = True
                    u = aresta[1] if aresta[0] == v else aresta[0]
                    visitados[aresta] = True
                    break

            if not ha_aresta:
                return False, []

            #adiciona o vertice v ao final do ciclo
            ciclo.append(u)
            
            if u == t:
                break
            
            v = u

        for i, a in enumerate(ciclo):
            for aresta, visitado in visitados.items():
                    if a in aresta and not visitado:
                        r2, ciclo2 = self.buscar_subciclo_euleriano(grafo,a,visitados)
                        if r2 is False:
                            return False, []
                        else:
                            index = ciclo.index(a)
                            ciclo = ciclo[:index] + ciclo2 + ciclo[index+1:]
                            break
    
        return True,ciclo
