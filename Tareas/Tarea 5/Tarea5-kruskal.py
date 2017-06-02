
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


def visitar_dfs_kruskal(lista, nodo, pred, visitado, secuencia):
	visitado.add(nodo)
	secuencia.append(nodo)	
	vecinos = lista[nodo]
	for k in vecinos:
		if k not in visitado:
			pred[k] = [nodo] 
			self.visitar_dfs_kruskal(lista, k, pred, visitado,secuencia)
	
		
	return (pred,secuencia)

def dfs_kruskal(arbol, grafo):
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


lista = lista_ady_nodos(10)
arbol = kruskal(lista)
pred, secuencia, peso = dfs_kruskal(arbol,lista)
print("Peso: ",peso, " secuencia: ",secuencia)
