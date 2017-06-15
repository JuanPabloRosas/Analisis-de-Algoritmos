import random
import copy
import matplotlib.pyplot as plt
import networkx as nx

def crea_puzzle(num):
	puzzle = [[1,2,4],[5,0,3],[6,8,7]]
	random.shuffle(puzzle)
	random.shuffle(puzzle[random.randint(0,2)])
	return puzzle

def movimientos(puzzle, predecesor):
	hijos = []
	#OBTENER POSICION DEL 0
	if 0 in puzzle[0]:
		i = 0
		j = puzzle[0].index(0)

	elif 0 in puzzle[1]:
		i = 1
		j = puzzle[1].index(0)
	else:
		i = 2
		j = puzzle[2].index(0)
	"""
	print("PADRE")
	print("_________")
	print("%i %i %i" % (puzzle[0][0], puzzle[0][1], puzzle[0][2]))
	print("%i %i %i" % (puzzle[1][0], puzzle[1][1], puzzle[1][2]))
	print("%i %i %i" % (puzzle[2][0], puzzle[2][1], puzzle[2][2]))
	print("_________")
	"""
	
	#CREAMOS COPIAS DE LAS LISTA PARA GENERAR SUS HIJOS
	hijo1 = copy.deepcopy(puzzle)
	hijo2 = copy.deepcopy(puzzle)
	hijo3 = copy.deepcopy(puzzle)
	hijo4 = copy.deepcopy(puzzle)

	if j + 1 < len(hijo1[0]):
		#HIJO 1
		y = hijo1[i][j]
		hijo1[i][j] = hijo1[i][j+1]
		hijo1[i][j+1] = y
		"""
		print("HIJO 1")
		print("%i %i %i" % (hijo1[0][0], hijo1[0][1], hijo1[0][2]))
		print("%i %i %i" % (hijo1[1][0], hijo1[1][1], hijo1[1][2]))
		print("%i %i %i" % (hijo1[2][0], hijo1[2][1], hijo1[2][2]))
		print()
		#return hijo1
		"""
	if j - 1 >= 0:
		#HIJO 2
		y = hijo2[i][j]
		hijo2[i][j] = hijo2[i][j-1]
		hijo2[i][j-1] = y
		"""
		print("HIJO 2")
		print("%i %i %i" % (hijo2[0][0], hijo2[0][1], hijo2[0][2]))
		print("%i %i %i" % (hijo2[1][0], hijo2[1][1], hijo2[1][2]))
		print("%i %i %i" % (hijo2[2][0], hijo2[2][1], hijo2[2][2]))
		print()
		#return hijo2
		"""
	if i + 1 < len(hijo3):
		#HIJO 3
		y = hijo3[i][j]
		hijo3[i][j] = hijo3[i+1][j]
		hijo3[i+1][j] = y
		"""
		print("HIJO 3")
		print("%i %i %i" % (hijo3[0][0], hijo3[0][1], hijo3[0][2]))
		print("%i %i %i" % (hijo3[1][0], hijo3[1][1], hijo3[1][2]))
		print("%i %i %i" % (hijo3[2][0], hijo3[2][1], hijo3[2][2]))
		print()
		#return hijo3
		"""
	if i - 1 >= 0:
		#HIJO 4
		y = hijo4[i][j]
		hijo4[i][j] = hijo4[i-1][j]
		hijo4[i-1][j] = y
		"""
		print("HIJO 4")
		print("%i %i %i" % (hijo4[0][0], hijo4[0][1], hijo4[0][2]))
		print("%i %i %i" % (hijo4[1][0], hijo4[1][1], hijo4[1][2]))
		print("%i %i %i" % (hijo4[2][0], hijo4[2][1], hijo4[2][2]))
		print()
		#return hijo4
		"""

	if hijo1 != puzzle:
		if hijo1 != predecesor:
			hijos.append(hijo1)
	if hijo2 != puzzle:
		if hijo2 != predecesor:
			hijos.append(hijo2)
	if hijo3 != puzzle:
		if hijo3 != predecesor:
			hijos.append(hijo3)
	if hijo4 != puzzle:
		if hijo4 != predecesor:
			hijos.append(hijo4)

	return hijos

def BFS(puzzle,solucion):
	nivel = 0
	arbol = {nivel : puzzle}
	hijos = movimientos(puzzle,"null")
	nivel = nivel + 1
	arbol[nivel] = hijos
	cont = 0
	while nivel < 500:
		nivel = nivel + 1
		for i in hijos:
			hijos2 = movimientos(i,"null")
			if solucion in hijos:
				#print(hijos)
				return hijos,True
			if nivel not in arbol: 
				arbol[nivel] = hijos2
			else:
				arbol[nivel].append(hijos2)
		hijos[:] = []
		for j in hijos2:
				hijos.append(j)
		hijos2[:] = []
		cont = cont + 1
	#print("ARBOL: ", arbol)
	return arbol,False


def DFS_recursivo(puzzle, solucion, num,visitado,arbol,pred):

	print("recibe: ",puzzle) 
	arbol.append(puzzle)
	
	while arbol and (num < 200):
		num = num + 1
		nodo = arbol.pop(0)
		if nodo == solucion:
			return True
		predecesor = pred[str(nodo)]
		#print("padre : ", predecesor)
		hijos = movimientos(nodo, predecesor)

		for i in hijos:
			arbol.append(i)
			pred[str(i)] = str(nodo)
		if str(nodo) not in visitado:
			visitado.add(str(nodo))
			DFS_recursivo(nodo,solucion, num,visitado,arbol,pred)
	return visitado



cant = 0
solucion = [[1,2,4],[5,0,3],[6,8,7]]

print("Solucion: ",solucion)
for j in range(0,10):
	for i in range(0,10):
		puzzle = crea_puzzle(8)
		res,flag = BFS(puzzle,solucion)
		if flag:
			cant = cant + 1
		#print(".")
	print(j, " Cantidad: ",cant)
	print("Puzzle: ",puzzle)
promedio = cant / 10
print("Promedio: ",promedio)

"""
num = 0
visitado = set()
arbol = []
pred = {str(puzzle):"null"}
"""


#DFS_recursivo(puzzle, solucion, num, visitado, arbol, pred)
#print(pred)
#print(visitado)