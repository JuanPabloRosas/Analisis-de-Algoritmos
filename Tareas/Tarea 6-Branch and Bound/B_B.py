import random

def trabajos_prueba():
	#Renglones: Trabajadores
	#Columnas: Trabajos
	#Unidades de tiempo que tarda el trabajador 'x' en realizar el trabajo 'y'
	nodos = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
	return nodos

def gen_trabajos(n):
	nodos = [[] for _ in range(n)]
	for x in range(n):
		for y in range(n):
				nodos[x].append(random.randint(0,100))
	return nodos

def evalua(nodos,columna,renglon):
	marcados = [columna]
	indice_i = 0
	indice_j = 0
	costo = nodos[renglon][columna]
	for x in range(0,len(nodos)):
		menor = 1000
		for y in range(0,len(nodos[x])):
			if x != renglon:
				if y not in marcados:
					if nodos[x][y] < menor:
						menor = nodos[x][y]
						indice_i = y
						indice_j = x
		if menor != 1000:
			costo = costo + menor
			marcados.append(indice_i)
						
	
	return costo,columna,renglon

def bb(nodos):

	renglon = random.randint(0,3)
	print("Renglon inicial: ", renglon)
	menor = 10000
	fo = 0
	while len(nodos) != 0:
		for columna in range(0,len(nodos)):
			costo_nodo,col,ren = evalua(nodos,columna,renglon)
			print("col:", col," ren:",ren, " costo: ",nodos[ren][col]," valor objetivo: ",costo_nodo)
			if costo_nodo < menor:
				menor = costo_nodo
				col2 = columna
				ren2 = renglon
		fo = fo + nodos[ren2][col2]
		print("Menor: costo: ",nodos[ren2][col2]," valor objetivo: ",menor)
		nodos.pop(ren2)
		for x in range(0,len(nodos)):
			nodos[x].pop(col2)
		renglon = len(nodos)-1
	print("Costo Optimo: ", fo)
	return True

#lista = trabajos_prueba()
#bb(lista)
lista2 = gen_trabajos(10)
bb(lista2)
