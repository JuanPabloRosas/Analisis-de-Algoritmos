import string
import random

def CNF(asign, inst):
	flag = False
	linea = inst.readline()[:-1]
	linea = linea.split(' ')
	if linea != asign:
		i = 0
		while i < len(linea):
			if(linea[i].find('!') == -1):
				i = i+1
				continue
				
			else:
				linea.pop(i)
				i = -1
			if linea == asign:
				flag = True
				break
	else:
		flag = True	
	return flag

def Lee():
	inst = open('Instancia.txt', 'r')
	inst.readline()
	asign = open('Asignacion.txt', 'r')
	for linea in asign:
		asign = linea[:-1].split(' ')
		res = CNF(asign, inst)
		#print(res)
		if(res == False):
			break
	return res


def gen_inst(num_elem, CNF):
	file = open('instancia_generada.txt', 'w')
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

def gen_asign(num_elem, CNF):
	file = open('asignacion_generada.txt', 'w')	
	file.close()


#print(Lee())
gen_inst(15,True)
