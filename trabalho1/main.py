from grafo import Grafo
from busca_largura import BuscaLargura
from ciclo_euleriano import CicloEuleriano
from bellman_ford import BellmanFord

#ARQUIVOS:
#ContemCicloEuleriano.net
# SemCicloEuleriano.net
#fln_pequena.net

#criar uma instancia do objeto grafo
grafo = Grafo()

    #Exemplo de uso dos métodos do grafo
# grafo.ler('fln_pequena.net')
# print('Quantidade de vértices do grafo:', grafo.qtdVertices())
# print('Quantidade de arestas do grafo:', grafo.qtdArestas())
# print('Grau do vértice 9:', grafo.grau(9))
# print('Rótulo do vértice 2:', grafo.rotulo(2))
# print('Vizinhos do vértice 3:', grafo.vizinhos(3))
# print('Existe aresta entre os vértices 2 e 5?', grafo.haAresta(2, 5))
# print('Peso da aresta entre os vértices 1 e 2:', grafo.peso(1,2))
# print()

# #BUSCA EM LARGURA:
# grafo.ler('fln_pequena.net')
# busca = BuscaLargura()
# nivel, antecessor = busca.busca_largura(grafo, 7)
# busca.imprimir(grafo,nivel)
# print()

# #CICLO EULERIANO -- Implementação não foi bem sucedida
print("Ciclo Euleriano: ")
#grafo.ler('SemCicloEuleriano.net')
grafo.ler('ContemCicloEuleriano.net')
ciclo_euleriano = CicloEuleriano()
r, ciclo = ciclo_euleriano.ciclo_euleriano(grafo)
if r is False:
    print("0")
else:
    print("1")
    print(' '.join(map(str, ciclo)))
print("\n")

#BELLMAN-FORD
print("Bellman-Ford: ")
grafo.ler('fln_pequena.net')
bellman_ford  = BellmanFord()
boleano, distancia, predecessores = bellman_ford.bellman_ford(grafo, 1)
bellman_ford.imprimir_caminhos(grafo,distancia, predecessores)
