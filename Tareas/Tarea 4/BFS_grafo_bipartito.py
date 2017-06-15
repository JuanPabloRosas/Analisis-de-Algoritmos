import random
def inst_grafo_nodos(num_nodos):
	lista_ady = dict()
	file = open('instancia_grafo_nodos.txt', 'w')
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

def lista_prueba_no_bipartito():
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

def lista_prueba_bipartito():
		nodos={0:{2:12,6:16},
		1:{2:16,3:8,4:18},
		2:{0:8, 1:10},
		3:{1:8, 5:8},
		4:{1:4},
		5:{3:8, 9:7},
		6:{0:2,7:1},
		7:{6:9,8:18,9:16},
		8:{7:1},
		9:{5:3,7:1}}
		return nodos


def bipartito(lista_ady):
	nodo = random.randint(0,len(lista_ady))
	actual = [nodo]
	nivel = 0
	niveles_par = {nodo: nivel}
	niveles_impar = {}
	while len(actual) > 0:
		nivel += 1
		siguiente = []
		for integrante in actual:
			for vecino in lista_ady[integrante]:
				if nivel % 2 == 0 and vecino not in niveles_par and vecino not in niveles_impar:
					if adyacente(vecino, lista_ady, niveles_par):
						return False
					niveles_par[vecino] = nivel
					siguiente.append(vecino)
				else:
					if vecino not in niveles_impar and vecino not in niveles_par:
						if adyacente(vecino, lista_ady, niveles_impar):
							return False
						niveles_impar[vecino] = nivel
						siguiente.append(vecino)
		actual = siguiente
	return True

def adyacente(nodo, lista_ady, niveles):
	for i in niveles:
		if nodo in lista_ady[i]:
			return True
	return False

lista = lista_prueba_no_bipartito()
#lista = lista_prueba_bipartito()
#lista = inst_grafo_nodos(5)
print(bipartito(lista))
