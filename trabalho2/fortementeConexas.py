from grafo import Grafo


class ComponentesFortementeConexas:

    #grafo transposto basta inverter as arestas
    #recebe um grafo dirigido nao ponderado G = (V, A)
    def componentes_fortemente_conexas(self, grafo):
        
        #faz uma busca em profundidade sobre o grafo g 
        visitados, tempo_inicial, antecessores, tempo_final = self.algoritmo_16(grafo)

        grafo_transposto = self.criar_grafo_transposto(grafo)

        #vertices_ordenados = self.ordenar_vertices_decrescente(grafo_transposto, tempo_final)
        #print(vertices_ordenados)
        visitados_trasposto, tempo_inicial_transposto, antecessores_transposto, tempo_final_transposto = self.algoritmo_16_adaptado(grafo_transposto, tempo_final)

        return self.encontrar_componente_fortemente_conexas(grafo, antecessores_transposto)

    def criar_grafo_transposto(self, grafo):
        grafo_transposto = Grafo()
        grafo_transposto.vertices = grafo.vertices
        grafo_transposto.pesos = grafo.pesos

        for aresta in grafo.arestas:
            aresta_transposta = (aresta[1], aresta[0])
            grafo_transposto.arestas.append(aresta_transposta)
        
        return grafo_transposto

    def algoritmo_16(self, grafo): 
    
        #definindo as estruturas
        visitados = [False] * grafo.qtdVertices()
        tempo_inicial = [float('inf')] * grafo.qtdVertices()
        tempo_final = [float('inf')] * grafo.qtdVertices()
        antecessores = [None] * grafo.qtdVertices()

        #configurando tempo de inicio
        tempo = 0

        #escolhe um vertice aleatorio
        for u in grafo.vertices.keys():
            if not visitados[u -1]:
                #DFS-Visit- algoritmo 17
                self.algoritmo_17(grafo, u, visitados, tempo_inicial, antecessores, tempo_final, tempo)
        return (visitados, tempo_inicial, antecessores, tempo_final)

    #linha 6 do algoritmo 16- unica mudanca
    def algoritmo_16_adaptado(self, grafo, tempo_final_original): 
    
        #definindo as estruturas
        visitados = [False] * grafo.qtdVertices()
        tempo_inicial = [float('inf')] * grafo.qtdVertices()
        tempo_final = [float('inf')] * grafo.qtdVertices()
        antecessores = [None] * grafo.qtdVertices()
        
        #configurando tempo de inicio
        tempo = 0

        #escolhe um vertice em ordem decrescente
        while True:
                maior_tempo = max(tempo_final_original)
                indice_maior = tempo_final_original.index(maior_tempo)
                tempo_final_original[indice_maior] = -1
                if not visitados[indice_maior]:
                    #DFS-Visit- algoritmo 17
                    self.algoritmo_17(grafo,indice_maior,visitados,tempo_inicial,antecessores,tempo_final,tempo)
                
                continuar = False
                for num in tempo_final_original:
                    if num > -1:
                        continuar = True
                if continuar == False:
                    break
        return (visitados,tempo_inicial,antecessores,tempo_final)

    def algoritmo_17 (self,grafo, u, visitados, tempo_inicial, antecessores, tempo_final, tempo):
        visitados[u - 1] = True
        tempo += 1
        tempo_inicial[u-1] = tempo

        vizinhos = grafo.vizinhos(u)
        for vizinho in vizinhos:
            if not visitados[vizinho-1]:
                antecessores[vizinho-1] = u
                self.algoritmo_17(grafo, vizinho, visitados, tempo_inicial, antecessores, tempo_final, tempo)
        tempo += 1
        tempo_final[u -1 ] = tempo
    
    def encontrar_componente_fortemente_conexas(self, grafo, antecessores):
        componentes = []
        visitados = []

        for vertice in grafo.vertices:
            if vertice not in visitados:
                componente = []
                while vertice is not None and vertice not in visitados:
                    componente.append(vertice)
                    visitados.append(vertice)
                    vertice = antecessores[vertice-1]
                if len(componente) > 1:
                    componentes.append(componente)

        return componentes
