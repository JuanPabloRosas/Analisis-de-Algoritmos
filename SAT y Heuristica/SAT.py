import string
import random

def DNF(asign, inst):
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

def CNF(asign,inst):
	return True

def Lee():
	inst = open('Instancia.txt', 'r')
	sat = inst.readline()
	if sat == 'CNF':
		asign = open('Asignacion.txt', 'r')
		for linea in asign:
		asign = linea[:-1].split(' ')
		res = CNF(asign, inst)
		#print(res)
		if(res == False):
			break
	else:
		asign = open('Asignacion.txt', 'r')
		for linea in asign:
		asign = linea[:-1].split(' ')
		res = DNF(asign, inst)
		#print(res)
		if(res == False):
			break
	return res


def gen_inst(num_elem, CNF):
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

def gen_asign(CNF):
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

print(Lee())
#gen_inst(50,True)
#gen_asign(True)
