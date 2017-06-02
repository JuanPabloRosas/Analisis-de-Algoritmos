import random
import math
from time import time

#problema de cluster maximisar el beneficio

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

tiempos = []
n = 10
num_nodos = 5

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

def initialSolution(nodos):
	c1 = []
	c2 = []
	for i in nodos:
		cluster = random.randint(1,2)
		if cluster == 1:
			c1.append(i)
		else:
			c2.append(i)

	s = {1:c1, 2:c2} 
	return s

def evalua(nodos, solucion):
	beneficio = 0
	for i in solucion:
		for j in solucion[i]:
			for k in solucion[i]:
				if j in nodos:
					if k in nodos[j]:
						#print(beneficio ,"+ [",j,"]","[",k,"]-", nodos[j][k], "=",beneficio + nodos[j][k] )
						beneficio = beneficio + nodos[j][k]
	return beneficio

def localSearch(nodos, solucion):
	vecindario = {}
	cont = 0
	sol = {}
	solucion_l = {}
	menor = 1000000
	copia1 = list(solucion[1])
	copia2 = list(solucion[2])
	for i in solucion[1]:
		for j in solucion[2]:

			item1 = i
			item2 = j

			indice1 = solucion[1].index(item1)
			indice2 = solucion[2].index(item2)

			

			copia1[indice1] = item2
			copia2[indice2] = item1

			sol[1] = copia1
			sol[2] = copia2
			
			ev = evalua(nodos,sol)
			if ev < menor:
				solucion_l = sol
			
			copia1 = list(solucion[1])
			copia2 = list(solucion[2])

			vecindario[cont] = sol
			cont = cont + 1 


	return solucion_l


def perturbation(solucion):
	cluster = random.randint(1,2)
	pos1 = random.randint(0,len(solucion[1])-1)
	pos2 = random.randint(0,len(solucion[2])-1)


	if cluster == 2:
		#print("Solucion [2]: ",solucion[2], " posicion: ", pos2 )
		if len(solucion[2]) > 1:
			item = solucion[2][pos2]
			solucion[2].remove(solucion[2][pos2])
			solucion[1].insert(pos1,item)
		else:
			#print("Solucion [1]: ",solucion[1], " posicion: ", pos1 )
			item = solucion[1][pos1]
			solucion[1].remove(solucion[1][pos1])
			solucion[2].insert(pos2,item)
	else:
		if len(solucion[1]) > 1:
			#print("Solucion [1]: ",solucion[1], " posicion: ", pos1 )
			item = solucion[1][pos1]
			solucion[1].remove(solucion[1][pos1])
			solucion[2].insert(pos2,item)
		else:
			item = solucion[2][pos2]
			solucion[2].remove(solucion[2][pos2])
			solucion[1].insert(pos1,item)

	return solucion

def ils():
	tiempo_inicial = time()
	lista = inst_grafo_nodos(10)
	#print(lista)
	sol = initialSolution(lista)
	beneficio = evalua(lista, sol)
	#print("solucion: ", sol, " beneficio: ", beneficio)
	cont = 0
	sol_final = {}
	while (cont < 1000):
		#print(cont)
		s_p = perturbation(sol)
		ev = evalua(lista,s_p)
		#print("solucion perturbada: ",s_p, " beneficio: ", ev) 
		s_l = localSearch(lista,s_p)
		ev = evalua(lista,s_l)
		#print("solucion busqueda local: ",s_l, " beneficio: ", ev)
		
		#Criterio de Aceptacion

		if ev > beneficio:
			beneficio = ev
			sol_final = s_l

		else:
			e = beneficio - ev
			#ecu = math.exp(e / 100)
			ecu = e/10000
			rand = random.random()
			#print(ecu)
			#prGreen("Ecuacion: " + str(ecu)+ "random: "+ str(rand))
			
			if rand < ecu:
				sol = s_l
				#prRed("Acepto solucion peor___________________________")

		cont = cont + 1

	#print("Beneficio Final:" , beneficio, "Solucion: ", sol_final)
	tiempo_final = time()
	tiempo_ejecucion = tiempo_final - tiempo_inicial
	return tiempo_ejecucion


for i in range(0,n):
	tiempos.append(ils())

promedio_tiempos = 0

for j in tiempos:
	suma_tiempos = promedio_tiempos + j

promedio_tiempos = suma_tiempos / n
print(promedio_tiempos)
