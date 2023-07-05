from grafo import Grafo
from edmondsKarp import EdmondsKarp
from hopcroftKarp import HopcroftKarp
from lawler import Lawler

#Edmonds-Karp
grafoA = Grafo()
grafoA.ler('instancias-teste/fluxo_maximo_aula.net')
edmonds_karp =  EdmondsKarp()
fluxo_max = edmonds_karp.edmonds_karp(grafoA)
print(f"Fluxo maximo: {fluxo_max:.2f}\n")

#Hopcroft-Karp
grafoB = Grafo()
grafoB.ler('instancias-teste/pequeno.net')
hopcroft_karp = HopcroftKarp()
emparelhamento, mate = hopcroft_karp.hopcroft_karp(grafoB)
print("emparelhamento maximo: ",emparelhamento)
print(f"mate {mate}\n")

#Coloracao - Lawler - nao concluido
# grafoC = Grafo()
# grafoC.ler('instancias-teste/cor3.net')
# lawler = Lawler()
# minina= lawler.lawer_algorithm(grafoC)

