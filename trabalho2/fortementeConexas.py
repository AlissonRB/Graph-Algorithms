from grafo import Grafo

class ComponentesFortementeConexas:

    #grafo transposto basta inverter as arestas
    def componentes_fortemente_conexas(self, grafo):
    #recebe um grafo dirigido nao ponderado G = (V, A)

    #faz uma busca em profundidade sobre o grafo g 

        visitados, tempo_inicial, antecessores, tempo_final = self.algoritmo_16(grafo)

        #tempo_final é um dicionario = {vertice = tempo_final}
        #pega os vertice do grafo, e ordena de acordo com o tempo_final retornado

        #A- é um conjunto de arestas

        grafo_transposto = Grafo()
        grafo_transposto.vertices = grafo.vertices
        arestas_transposto = [(y, x) for x, y in grafo.arestas]
        grafo_transposto.peso = grafo.peso

        visitados_trasposto, tempo_inicial_transposto, antecessores_transposto, tempo_final_transposto = self.algoritmo_16_adaptado(grafo_transposto)

        return antecessores_transposto
    #passa so o grafo, pq como queremos visitar todos os 
    #vertices, o vertice inicial é arbitrario
    def algoritmo_16 (self, grafo): 
    
        #estrutura de arestas visitadas
        visitadas = {}
        for aresta in grafo.arestas:
            visitadas[aresta] = False
        
        #grafo.vertices =  {1: 'Universidade Federal de Santa Catarina',
        tempo_inicial = {}
        for chave, valor in grafo.vertices.items():
            tempo_inicial[chave] = float("inf")
        
        #estrutura do tempo final da visita
        tempo_final = {}
        for chave, valor in grafo.vertices.items():
            tempo_final[chave] = float("inf")

        #estrutura de antecessores de um vertice
        antecessores = {}
        for chave, valor in grafo.vertices.items():
            antecessores[chave]  = None
        
        #configurando tempo de inicio
        tempo = 0

        #escolhe um vertice aleatorio
        for vertice in grafo.vertices:
            if visitadas[vertice] == False:
                #DFS-Visit- algoritmo 17
                self.algoritmo_17(grafo,vertice,visitadas,tempo_inicial,antecessores,tempo_final, tempo)
        return (visitadas,tempo_inicial,antecessores,tempo_final)

    #vertices {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    #ordena os vertices de um dicionario de acordo com o tempo final
    def ordenar_decrescente(self,vertices: dict, tempo: dict):
        vertices_ordenados = {}
        maior = 0
        for chave, valor in vertices:
            if valor > maior:
                maior = valor

        while len(vertices) != 0:
            for chave, valor in vertices.items():
                if valor == maior:
                    vertices_ordenados

    #o vertice v nao é arbitrario, e definido pela ordem decrescente dos 
    # valores da estrutura de dados F(tempo_final)

    #linha 6 do algoritmo 16- unica mudanca
    def algoritmo_16_adaptado (self, grafo): 
    
        #estrutura de arestas visitadas
        visitadas = {}
        for aresta in grafo.arestas:
            visitadas[aresta] = False
        
        #estrutura de tempo inicial
        #para cada vertice no grafo o tempo é igual a infinito
        #essa estrutura so existe aqui nao na classe grafo
        #grafo.vertices =  {1: 'Universidade Federal de Santa Catarina',
        tempo_inicial = {}
        for chave, valor in grafo.vertices.items():
            tempo_inicial[chave] = float("inf")
        
        #estrutura do tempo final da visita
        tempo_final = {}
        for chave, valor in grafo.vertices.items():
            tempo_final[chave] = float("inf")

        #estrutura de antecessores de um vertice
        antecessores = {}
        for chave, valor in grafo.vertices.items():
            antecessores[chave]  = None
        
        #configurando tempo de inicio
        tempo = 0

        #escolhe um vertice em ordem decrescente
        for vertice in grafo.vertices:
            if visitadas[vertice] == False:
                #DFS-Visit- algoritmo 17
                self.algoritmo_17(grafo,vertice,visitadas,tempo_inicial,antecessores,tempo_final,tempo)
        
        return (visitadas,tempo_inicial,antecessores,tempo_final)

    #linha4: para cada arco sainte de vertic e
    def algoritmo_17 (self,grafo, vertice, visitados, tempo_inicial, antecessores, tempo_final, tempo):
        visitados[vertice - 1] = True
        tempo += 1
        tempo_inicial[vertice-1] = tempo

        #para cada vizinho do vertice, que tenha aresta saintes
        # se nao foi visitado ainda
        #antecessor do vizinho vai ser o vertice
        vizinhos = grafo.vizinhos(vertice)
        for vizinho in vizinhos:
            if visitados[vizinho] == False:
                antecessores[vizinho] = vertice
                self.algoritmo_17(grafo, vizinho, visitados, tempo_inicial, antecessores, tempo_final, tempo)
        tempo += 1
        tempo_final = tempo

        #chama novamente essa mesma funcao passando como vertice de origem esse vizinho, para fazer a busca em profundidade
    
    #vertices {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}
    def encontrar_componente_fortemente_conexas(self, grafo, antecessores):
        componentes = []
        visitados = []

        for vertice in grafo.vertice:
            if vertice not in visitados:
                componente = []
                while vertice is not None and vertice not in visitados:
                    componente.append(vertice)
                    visitados.append(vertice)
                    vertice = antecessores[vertice]
                if len(componente) > 1:
                    componente.append(componente)

        return componentes
