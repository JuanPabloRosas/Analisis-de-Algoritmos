import random
import string 

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

def inst_grafo_completo(num_nodos):
	lista_ady = dict()
	file = open('instancia_grafo_completo.txt', 'w')
	for i in range(0, num_nodos):
		nodo_ady = 0
		lista_ady[i] = {}
		nodos_ady = num_nodos - 1
		while(len(lista_ady[i]) < nodos_ady):
			if nodo_ady != i :
				lista_ady[i][nodo_ady] = random.randint(1,100)
			nodo_ady = nodo_ady + 1
		file.write(str(i) + ': ' + str(lista_ady[i]) + '\n')
	file.close()
	return lista_ady

def inst_grafo(num_nodos, num_arcos):
	lista_ady = dict()
	if num_arcos >= num_nodos - 1:	
		arcos = num_nodos
		while arcos != 0:
			for i in range(0,arcos):
				nodo_ady = random.randint(0,num_nodos)
				if i not in lista_ady: 
					lista_ady[i] = {}
				if nodo_ady != i :
					lista_ady[i][nodo_ady] = random.randint(1,100)
				else:
					lista_ady[i][num_nodos-1] = random.randint(1,100)
			num_arcos = num_arcos - arcos
			if num_arcos < num_nodos:
				arcos = num_arcos
	else:
		print("La cantidad de arcos crea un grafo disconexo!")
	return lista_ady

def inst_SAT(num_elem, CNF):
	file = open('instancia_SAT.txt', 'w')
	x = string.ascii_lowercase
	
	if(CNF):
		file.write('#CNF' + '\n')	
	else:	
		file.write('#DNF' + '\n')

	for i in range(0 , num_elem):
		linea = random.sample(x,3)
		j = random.randint(0,3)
		if j != 3:
			linea[j]= '!'+ linea[j]
		file.write(' '.join(linea) + '\n')	
	file.close()

def asign_SAT(CNF):
	file = open('asignacion_SAT.txt', 'w')	
	x = string.ascii_lowercase
	
	if(CNF):
		file.write('#CNF' + '\n')	
	else:	
		file.write('#DNF' + '\n')

	linea = random.sample(x,15)
	"""	
	j = random.randint(0,5)
	if j != 4:
		linea[j]= '!'+ linea[j]
	"""	
	file.write(' '.join(linea) + '\n')	
	file.close()


inst_grafo_nodos(10)
inst_grafo_completo(10)
lista = inst_grafo(10,25)
print(lista)
inst_SAT(10,True)
asign_SAT(True)
