import os, sys 
import random
import matplotlib.pyplot as plt
import networkx as nx
from copy import deepcopy
from collections import defaultdict
from random import choice

def lista_ady_prueba():
	nodos={0:{1:12,6:16,8:2},
	1:{0:16,8:8,4:12,6:18,9:1},
	2:{4:12,6:8},
	3:{2:10,5:16,8:8},
	4:{1:4,2:6,3:10,5:18,9:2},
	5:{3:8,4:6},
	6:{0:2,1:4,2:1},
	7:{8:18,9:16},
	8:{0:6,3:14,7:1},
	9:{1:8,4:14,7:1}}
	return nodos
	
def insertar_nodo(lista_ady, nodo):	
	if nodo in lista_ady:
		return False
	else:
		lista_ady[nodo] = {}
		return True		

def eliminar_nodo(lista_ady, nodo):
	if nodo in lista_ady:	
		del lista_ady[nodo]
		for i in lista_ady:
			if nodo in lista_ady[i]:
				del lista_ady[i][nodo]
		return True
	else:
		return False

def insertar_arco(lista_ady, nodo , nodo2, peso):
	if nodo in lista_ady:
		if nodo2 in lista_ady:	
			lista_ady[nodo][nodo2] = peso
			return True
		else:
			return False
	else:
			return False

def eliminar_arco(lista_ady, nodo, nodo2):
	if nodo in lista_ady:			
		if nodo2 in lista_ady[nodo]:
			del lista_ady[nodo][nodo2]
			return True
		else:
			return False

	#GRAFICAR
def graficar(lista_ady):
	G=nx.DiGraph()
	for i in lista_ady:
		for j in lista_ady[i]:
			G.add_node(i)
			G.add_edge(i,j, label=lista_ady[i][j])
	print("ARCOS: ",G.edges())
	
	#GAFO DIRIGIDO
	#nx.draw_circular(G, arrows=True, with_labels=True)
	nx.draw_spring(G, arrows=True, with_labels=True)

	#GRAFO NO DIRIGIDO
	#nx.draw_shell(G, arrows=False, with_labels=True)
	plt.savefig('Grafo.png')
	plt.show()

def graficar_peso(lista_ady):
	G = nx.Graph()
	#AGREGAR ARCOS
	for i in lista_ady:
		for j in lista_ady[i]:
			peso = lista_ady[i][j]
			G.add_edge(i,j)
		
	print("Crea los Arcos")

	for v in G.nodes():
		G.node[v]['state']= v

	for n in G.edges_iter():
		G.edge[n[0]][n[1]]['state']='X'

	for i in lista_ady:
		for j in lista_ady[i]:
			peso = lista_ady[i][j]
			G.edge[i][j]['state']=peso

	pos = nx.spring_layout(G)

	nx.draw(G, pos, arrows=True)
	node_labels = nx.get_node_attributes(G,'state')
	nx.draw_networkx_labels(G, pos, labels = node_labels)
	edge_labels = nx.get_edge_attributes(G,'state')
	nx.draw_networkx_edge_labels(G, pos, edge_labels)
	plt.savefig('Grafo.png')
	plt.show()
		


#GRAFICAR
lista = lista_ady_prueba()
graficar(lista)
#graficar_peso(lista)

#INSERTAR,ELIMINAR ARISTAS
print("Eliminar Nodo, nodo = 2")
print(eliminar_nodo(lista,2))
graficar(lista)
print("Insertar Nodo, nodo = 2")
print(insertar_nodo(lista,2))
print("Insertar Arco, arco = (2,5) = 19")
print(insertar_arco(lista,2,5,19))
graficar(lista)