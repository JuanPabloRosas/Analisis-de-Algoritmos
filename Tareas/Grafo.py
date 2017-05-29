import os, sys 
import random
import matplotlib.pyplot as plt
import networkx as nx
from copy import deepcopy
from collections import defaultdict
from random import choice
class Grafo:
	#TAREA 1 - REPRESENTACION DE GRAFOS
	def lista_ady_prueba(self):
		nodos={0:{1:12,6:16,8:2},
		1:{0:16,8:8,4:12,6:18,9:1},
		2:{4:12,6:8},
		3:{4:10,5:16,8:8},
		4:{1:4,2:6,3:10,5:18,9:2},
		5:{3:8,4:6},
		6:{0:2,1:4,2:1},
		7:{8:18,9:16},
		8:{0:6,3:14,7:1},
		9:{1:8,4:14,7:1}}
		return nodos
	
	def insertar_nodo(self, lista_ady, nodo):	
		if nodo in lista_ady:
			return False
		else:
			lista_ady[nodo] = {}
			return True		

	def eliminar_nodo(self, lista_ady, nodo):
		if nodo in lista_ady:	
			del lista_ady[nodo]
			for i in lista_ady:
				if nodo in lista_ady[i]:
					del lista_ady[i][nodo]
			return True
		else:
			return False

	def insertar_arco(self,lista_ady, nodo , nodo2, peso):
		if nodo in lista_ady:
			if nodo2 in lista_ady:	
				lista_ady[nodo][nodo2] = peso
				return True
			else:
				return False
		else:
			return False

	def eliminar_arco(self,lista_ady, nodo, nodo2):
		if nodo in lista_ady:			
			if nodo2 in lista_ady[nodo]:
				del lista_ady[nodo][nodo2]
				return True
			else:
				return False


	#TAREA 2 -GENERADORES DE INSTANCIAS

	def lista_ady_nodos(self, num_nodos):
		lista_ady = dict()
		file = open('instancia_grafo.txt', 'w')
		for i in range(0, num_nodos):
			lista_ady[i] = {}
			nodos_ady = random.randint(1, num_nodos)
			while(len(lista_ady[i]) < nodos_ady):
				nodo_ady = random.randint(0,num_nodos)
				if nodo_ady != i :
					lista_ady[i][nodo_ady] = random.randint(1,100)
			file.write(str(i) + ': ' + str(lista_ady[i]) + '\n')
		file.close()
		return lista_ady

		
	#TAREA 3 - HEURISTICA PARA SAT
	
	def CNF(asign, inst):
		flag = True
		linea = inst.readline()[:-1]
		linea = linea.split(' ')
		for i in range(0, len(linea)):
			print(asign[i] ,linea[i])
			if(linea[i].find('!') == -1):
				if(asign[i] == linea[i]):	
					flag = True
				else:
					flag = False
					break
			else:
				if(asign[i] == '0'):
					continue
				else:
					flag = False
					break
				
		return flag

	def Lee():
		inst = open('Instancia.txt', 'r')
		inst.readline()
		asign = open('Asignacion.txt', 'r')
		for linea in asign:
			asign = linea[:-1].split(' ')
			res = CNF(asign, inst)
			print(res)
			if(res == False):
				break
		return res


	def gen_inst(num_elem, CNF):
	
		file = open('gen_inst.txt', 'w')
		x = string.ascii_lowercase
	
		if(CNF):
			file.write('#CNF' + '\n')	
		else:	
			file.write('#DNF' + '\n')

		for i in range(0 , num_elem):
			linea = random.sample(x,3)
			j = random.randint(0,2)
			linea[j]= '!'+ linea[j]
			file.write(' '.join(linea) + '\n')	
		file.close()

	def gen_asign(num_elem):
		return True	

	#TAREA 4 - RECORRIDOS Y CAMINOS EN GRAFOS
	#GRAFOS BIPARTITOS CON BFS
	def bfs(lista_ady, nodo):
		actual = [nodo]
		nivel = 0
		niveles= {nodo: nivel}
		while len(actual) > 0:
			nivel += 1
			siguiente = []
			for integrante in actual:
				for vecino in lista_ady[integrante]:
					if vecino not in niveles:
						niveles[vecino] = nivel
						siguiente.append(vecino)
			actual = siguiente
		return niveles
	#LABERINTOS CON DFS
	def dfs(self,lista_ady,nodo):
		return True

	def arbol_dfs(lista_ady, nodo):
		visitado = {}
		pred = {}	
		for i in range(0, len(lista_ady)):
			visitado[i] = 0
			pred[i] = [0]
		for j in range(nodo,len(lista_ady)):
			if (visitado[j] == 0):
				visitar_dfs(lista_ady, j, pred, visitado)
		return pred
			
	def visitar_dfs(lista_ady, nodo, pred, visitado):
		visitado[nodo] = 1
		vecinos = lista_ady[nodo]
		#print("vecinos: ", vecinos)
		for k in range(0, len(vecinos)):
			if (visitado[vecinos[k]] == 0):
				pred[vecinos[k]] = [nodo] 
				visitar_dfs(lista_ady, vecinos[k], pred, visitado)
		visitado[nodo] = 2
		return pred	 

	def arbol_bfs(lista_ady, nodo):
		actual = [nodo]
		nivel = 0
		niveles= {nodo: nivel}
		pred = {nodo: ['NULL']}
		while len(actual) > 0:
			nivel += 1
			siguiente = []
			for integrante in actual:
				for vecino in lista_ady[integrante]:
					if vecino not in niveles:
						niveles[vecino] = nivel
						siguiente.append(vecino)
						pred[vecino] = [integrante]
			actual = siguiente
		return pred
		
		
	"""
	def arbol_binario():
		nodos={}
		nodo = input()
		indice = 0
		nodos[indice] = nodo
		print("nodo?")
		r = input()
		while(r == 1):
			indice = indice + 1
			if not indice in nodos:
				nodo = input()
				if(nodo < nodos[indice-1]):
					nodos[indice] = nodo		
			print("nodo?")
			r = input()
		print(nodos)
	"""

	def aristas(lista_ady):	
		archivo = open("aristas")
		for i in range(0,len(lista_ady)):
			for j in range(0,len(lista_ady[i])):
					nodo = (i,lista_ady[i][j])
					print(nodo)
				

	def camino(path,n1 ,n2):
		d=dict()
		file = open(path)
		for line in file:
			linea = line.splitlines()
			for z in linea:
				x = z[0]
				y = z[1]
				cx = d.get(x, {x})
				cy = d.get(y, {y})
				nuevo = cx | cy
				#nuevo = cx			
				for raza in nuevo:
					d[raza] = nuevo
					if (n1 in d) & (n2 in d):
						return True
		return False
	


	#TAREA 5 - FLUJOS Y ARBOLES DE EXPANSION	
	def kruskal(self,Grafo):
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
			#print(arista)
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


	def visitar_dfs_kruskal(self,lista, nodo, pred, visitado, secuencia):
		visitado.add(nodo)
		secuencia.append(nodo)	
		vecinos = lista[nodo]
		for k in vecinos:
			if k not in visitado:
				pred[k] = [nodo] 
				self.visitar_dfs_kruskal(lista, k, pred, visitado,secuencia)
		
		
		return (pred,secuencia)

	def dfs_kruskal(self,arbol, grafo):
		print("Grafo original: ",grafo)
		visitado = set()
		pred = {}
		secuencia =[]
		peso = 0
		lista = defaultdict(set)
		for u,v in arbol:
			lista[u].add(v)
			lista[v].add(u)
		self.visitar_dfs_kruskal(lista, choice(list((lista.keys()))), pred, visitado,secuencia)
		i = 0
		while i < len(secuencia)-1:
			nodo1 = secuencia[i]
			nodo2 = secuencia[i+1]
			if nodo1 in grafo:
				if nodo2 in grafo[nodo1]:			
					peso = peso + grafo[nodo1][nodo2]

			i = i + 1
		
		return (pred,secuencia,peso)
			
	 	
	
	#TAREA 6 - RAMIFICACIONES Y BUSQUEDAS PARA OPTIMIZACION
	#TAREA 7 - ALEATORIZACION
	#TAREA 8 - EXPERIMENTOS CON TRANSICIONES DE FASE

	#GRAFICAR
	def graficar(self,lista_ady):
		G=nx.DiGraph()
		for i in lista_ady:
			for j in lista_ady[i]:
				G.add_node(i)
				G.add_edge(i,j, label=lista_ady[i][j])
		print("ARCOS: ",G.edges())
		#nx.draw(G, pos)
		#nx.draw_networkx_edge_labels(G,pos,with_labels=True,font_size=7)
		#nx.draw_circular(G, arrows=True, with_labels=True)
		nx.draw_spectral(G, arrows=False, with_labels=True)
		#nx.draw_random(G, arrows=False, with_labels=True)
		#nx.draw_spring(G, arrows=True, with_labels=True)
		#nx.draw_shell(G, arrows=False, with_labels=True)
		#nx.draw_networkx(G,pos=None, arrows=False, with_labels=True)	
		plt.show()

	def graficar_peso(self,lista_ady):
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

		nx.draw(G, pos)
		node_labels = nx.get_node_attributes(G,'state')
		nx.draw_networkx_labels(G, pos, labels = node_labels)
		edge_labels = nx.get_edge_attributes(G,'state')
		nx.draw_networkx_edge_labels(G, pos, edge_labels)
		#plt.savefig('this.png')
		plt.show()
		

	"""
	lista = dict_lista_ady_prueba()
	print(lista)
	lista = lista_adyacencia_nodos(10)
	#lista_pred = arbol_bfs(lista, 0)
	#print("PREDECESORES:  ",lista_pred)
	#lista_pred2 = breadth_first_search(lista, 0)
	#print("NIVELES:  ",lista_pred2)
	graficar_peso(lista)

	"""
	#lista = lista_adyacencia_nodos(10)
	#camino = camino("/home/pabloide/Documentos/Algoritmos/Grafo/aristas2.txt", 2, 9)
	#print(camino)

