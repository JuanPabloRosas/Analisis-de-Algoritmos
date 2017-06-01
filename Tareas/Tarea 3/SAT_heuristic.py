import random
import math
import string

# temp = 6 para 15 clausulas
# temp >= 22 para 20 clausulas
tempInicial = 20
factor = 0.999
iteraciones = 150

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

def simulated_annealing(instancia, asignacion):
	asign = open(asignacion , "r")
	asign.readline()
								#Solucion inicial
	sol = asign.readline()[:-1]
	sol = sol.split(' ')
	mejores_soluciones = {}
	mejor_solucion = ""
	clausulas = 0
	temp = tempInicial
	for iteracion in range(iteraciones):
		print("-------------------------------------------------------------------------------------------------------")
		print("ITERACION: ", iteracion, " TEMPERATURA: ", temp)
		#while temp > tempFinal:
								#Genera vecindario de la solucion
		vecinos = vecindario(sol,random.randint(1,11))
								#Toma un vecino aleatorio
		vecino = vecinos[random.randint(0,23)]
		
		vecino = vecino.split(' ')			#Evalua solucion inicial
		s1 = Evalua(sol, instancia)

		if s1 >= clausulas:
			clausulas = s1
			mejor_solucion = sol
								#Evalua vecino
		s2 = Evalua(vecino, instancia)
		if s2 > clausulas:
			clausulas = s2
			mejor_solucion = vecino

		print("SOL ACTUAL: ", sol, " VALOR= ", s1)
		print("VECINO:     ", vecino, " VALOR= ", s2)
		#print("Vecino satisface ", s2, " clausulas")
		
		if s1 <= s2:
			sol = vecino
			mejores_soluciones[vecino[0]+vecino[1]+vecino[2]+vecino[3]+vecino[4]] = s2
		else:
			e = s1 - s2
			ecu = math.exp(e / temp)
			rand = random.random() 
			if  1.5 < ecu:
				prGreen("SE ACEPTO LA SOLUCION PEOR: res = "+ str(ecu)+ " rand = "+ str(rand)+ " dif = "+ str(e)+ " temp = "+ str(temp))
				sol = vecino
			else:
				prRed("NO SE ACEPTO LA SOLUCION res = "+ str(ecu)+ " rand = "+ str(rand)+ " dif = "+ str(e)+ " temp = "+ str(temp) )
		temp = temp * factor
		print("-------------------------------------------------------------------------------------------------------")
	#print("Mejores soluciones: ", mejores_soluciones)
	#print("Mejores Soluciones: " ,sorted(mejores_soluciones, key = mejores_soluciones.__getitem__, reverse = True))
	print("-------------------------------------------------------------------------------------------------------")
	print(mejor_solucion, " satisface ", clausulas, " clausulas")

def Evalua(asign, instancia):
	inst = open(instancia,"r")
	cont = 0
	inst.readline()
	for linea in inst:
		linea = linea[:-1]
		linea = linea.split(' ')	
		if linea[0] != '':
			for i in range(0,2):
				if linea[i] in asign:
					cont = cont + 1
					break
	"""		
		else:
			cont = cont + 1
	"""
	return cont
	
def vecindario(solucion, mov):
	vecinos = []
	x = string.ascii_lowercase
	
	pos1 = x.index(solucion[0])
	pos2 = x.index(solucion[1])
	pos3 = x.index(solucion[2])
	pos4 = x.index(solucion[3])
	pos5 = x.index(solucion[4])
	pos6 = x.index(solucion[5])
	pos7 = x.index(solucion[6])
	pos8 = x.index(solucion[7])
	pos9 = x.index(solucion[8])
	pos10 = x.index(solucion[9])
	pos11 = x.index(solucion[10])

	for i in range(1,25):
		if mov == 1:
			if pos1 + i > 25:
				pos1 = (pos1 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else: 
				cadena = x[pos1 + i] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 2:	
			if pos2 + i > 25:
				pos2 = (pos2 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2 + i] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 3:
			if pos3 + i > 25:
				pos3 = (pos3 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3 + i]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 4:
			if pos4 + i > 25:
				pos4 = (pos4 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4 + i] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 5:
			if pos5 + i > 25:
				pos5 = (pos5 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5 + i]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 6:	
			if pos6 + i > 25:
				pos6 = (pos2 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6 + i] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 7:
			if pos7 + i > 25:
				pos7 = (pos3 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7 + i]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 8:
			if pos8 + i > 25:
				pos8 = (pos4 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8 + i] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 9:	
			if pos9 + i > 25:
				pos9 = (pos2 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9 + i]+ " " + x[pos10] + " " + x[pos11]
		elif mov == 10:
			if pos10 + i > 25:
				pos10 = (pos3 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10 + i] + " " + x[pos11]
		else:
			if pos11 + i > 25:
				pos11 = (pos4 + i) - 25
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11]
			else:
				cadena = x[pos1] + " " + x[pos2] + " " + x[pos3]+ " " + x[pos4] + " " + x[pos5]+ " " + x[pos6] + " " + x[pos7]+ " " + x[pos8] + " " + x[pos9]+ " " + x[pos10] + " " + x[pos11 + i]


		vecinos.append(cadena)
	return vecinos

simulated_annealing("instancia_SAT.txt", "asignacion_SAT.txt")
