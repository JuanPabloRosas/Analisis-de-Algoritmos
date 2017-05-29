#TAREA 4 - RECORRIDOS Y CAMINOS EN GRAFOS
def lista_ady_prueba():
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

def arbol_dfs(lista_ady, nodo):
	visitado = {}
	pred = {}	
	for i in lista_ady:
		visitado[i] = 0
		pred[i] = [0]
	for j in range(nodo,len(lista_ady)):
		if (visitado[j] == 0):
			visitar_dfs(lista_ady, j, pred, visitado)
	return pred
			
def visitar_dfs(lista_ady, nodo, pred, visitado):
	visitado[nodo] = 1
	vecinos = lista_ady[nodo]
	for k in vecinos:
		if (visitado[k] == 0):
			pred[k] = [nodo] 
			visitar_dfs(lista_ady, k, pred, visitado)
	visitado[nodo] = 2
	return pred	 


lista = lista_ady_prueba()
print(lista)
print("Arbol BFS: ", arbol_bfs(lista,3))
print("BFS: ", bfs(lista,3))
print("Arbol DFS: ", arbol_dfs(lista,3))
