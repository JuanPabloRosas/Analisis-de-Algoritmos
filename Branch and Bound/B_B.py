import random
def trabajos():
	nodos = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
	return nodos

def branch_and_bound(nodos):
	marcados = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	i = random.randint(0,3)
	j = random.randint(0,3)
	for a in range(0,4):
		marcados[j][a] = 1
		marcados[a][i] = 1
	print("marcados: ", marcados)

	costo = nodos[j][i]
	print(nodos[j][i],"+ 0 = ", nodos[j][i])
	for x in range(0,3):
		menor = 1000
		for y in range(0,3):
			if marcados[x][y] != 1:
				if nodos[x][y] < menor:
					menor = nodos[x][y]
		for a in range(0,4):
			marcados[j][a] = 1
			marcados[a][i] = 1
		print(costo," + ",menor)
		costo = costo + menor 
						
			
	print("col:", i, " ren:",j," costo:", costo)
	return True




lista = trabajos()
branch_and_bound(lista)
