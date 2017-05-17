from random import random
from sys import argv

def gen_inst(num, nom):
	file = open(nom, 'w')
	for i in range(num):		
		file.write(' '.join([str(random()) for i in range(4)]) + "\n")
	file.close()

gen_inst(int(argv[1]), argv[2])

	
