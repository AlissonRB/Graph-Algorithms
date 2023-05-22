from grafo import Grafo
from fortementeConexas import ComponentesFortementeConexas
from ordenacaoTopologica import OrdenacaoTopologica
from arvoreMinima import Prim

#Alisson Rafael Barbosa 21104150

#ORDENACAO TOPOLOGICA
print("Ordenação Topológica: ")
grafoA = Grafo()
grafoA.ler('ordenacao.net')
ordenacao_topologica = OrdenacaoTopologica()
ordenacao = ordenacao_topologica.ordenacao_topologica(grafoA)

#Arvores Geradoras Minimas
print("Algoritmo de Prim: ")
grafoB = Grafo()
grafoB.ler('arvore-geradora.net')
arvore_minima = Prim()
arvore = arvore_minima.algoritmo_prim(grafoB)
print()

#COMPONENTES FORTEMENTE CONEXAS
grafoC = Grafo()
print ("Componentes Fortemente Conexas:")
grafoC.ler('exemplo1.net')
fortemente_conexas = ComponentesFortementeConexas()
componentes = fortemente_conexas.componentes_fortemente_conexas(grafoC)
print("componentes conexas:",componentes)
