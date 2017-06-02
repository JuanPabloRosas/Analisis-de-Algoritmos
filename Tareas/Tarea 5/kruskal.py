import random
from copy import deepcopy
from collections import defaultdict
from random import choice
import matplotlib.pyplot as plt
import networkx as nx

def inst_grafo_nodos(num_nodos):
	lista_ady = dict()
	file = open('instancia_grafo_nodos.txt', 'w')
	for i in range(0, num_nodos):
		lista_ady[i] = {}
		nodos_ady = random.randint(1, num_nodos)
		while(len(lista_ady[i]) < nodos_ady):
			nodo_ady = random.randint(0,num_nodos)
			if nodo_ady != i :
				#lista_ady[i][nodo_ady] = random.randint(1,100)
				lista_ady[i][nodo_ady] = random.expovariate(5)
		file.write(str(i) + ': ' + str(lista_ady[i]) + '\n')
	file.close()
	return lista_ady

def kruskal(Grafo):
	aristas = {}
	for nodo in Grafo:
		for arco in Grafo[nodo]:
			aristas[nodo,arco] = Grafo[nodo][arco] 
	cand = deepcopy(aristas)
	arbol = set()
	peso = 0
	comp = dict()
	while len(cand)>0:
		arista = min(cand.keys(), key = (lambda k: cand[k]))
		del cand[arista]
		(u,v) = arista
		c = comp.get(v,{v})
		if u not in c:
			arbol.add(arista)
			peso += aristas[arista]
			nuevo = c.union(comp.get(u, {u}))
			for w in nuevo:
				comp[w] = nuevo		
	print("Kruskal  Peso",peso,":",arbol)
	return arbol


def visitar_dfs_kruskal(lista, nodo, pred, visitado, secuencia):
	visitado.add(nodo)
	secuencia.append(nodo)	
	vecinos = lista[nodo]
	for k in vecinos:
		if k not in visitado:
			pred[k] = [nodo] 
			visitar_dfs_kruskal(lista, k, pred, visitado,secuencia)
	
		
	return (pred,secuencia)

def dfs_kruskal(arbol, grafo):
	graficar_peso(grafo)
	print(grafo)
	visitado = set()
	pred = {}
	secuencia =[]
	peso = 0
	lista = defaultdict(set)
	for u,v in arbol:
		lista[u].add(v)
		lista[v].add(u)
	visitar_dfs_kruskal(lista, choice(list((lista.keys()))), pred, visitado,secuencia)
	i = 0
	while i < len(secuencia)-1:
		nodo1 = secuencia[i]
		nodo2 = secuencia[i+1]
		if nodo1 in grafo:
			if nodo2 in grafo[nodo1]:			
				peso = peso + grafo[nodo1][nodo2]

		i = i + 1
		
	return (pred,secuencia,peso)

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

def graficar_arbol(arbol):
	G=nx.DiGraph()
	for i,j in arbol:
		G.add_edge(i,j)
	print("ARCOS: ",G.edges())
	
	#GAFO DIRIGIDO
	#nx.draw_circular(G, arrows=True, with_labels=True)
	nx.draw_spring(G, arrows=True, with_labels=True)

	#GRAFO NO DIRIGIDO
	#nx.draw_shell(G, arrows=False, with_labels=True)
	plt.savefig('Arbol.png')
	plt.show()


lista = inst_grafo_nodos(10)
arbol = kruskal(lista)
pred, secuencia, peso = dfs_kruskal(arbol,lista)
print("Arbol: ")
print(arbol)
graficar_arbol(arbol)
print("Predecesores: ")
print(pred)
print("Peso: ",peso, " secuencia: ",secuencia)
