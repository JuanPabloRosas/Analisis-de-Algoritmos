def maquina_turing(cinta, s):
	Mt = dict()
	z = {'1' , '0'}
	t = 0
	p = 0

	Mt[(s , '1')] = (s, z , 'right')
	Mt[(s , '0')] = (s, z , 'right')

	#Sumar 1
	Mt[(s , ' ')] = (t, ' ' , 'left')
	Mt[(t , '1')] = (t, '0' , 'left')
	Mt[(t , '0')] = (t, '1' , 'stay')

	#Multiplicar por dos
	Mt[(t , ' ')] = (t, '0' , 'stay')

	#Par o Impar
	Mt[(s , ' ')] = (p, ' ' , 'left')
	Mt[(p , '1')] = (p, '0' , 'left')
	Mt[(p , '0')] = (p, '1' , 'left')

	if(cinta[s] in z):
		estado = Mt[(s , cinta[s])]
		if(estado[2] == 'right'):
			s = s + 1
			print("right")
		if(estado[2] == 'left'):
			s = s - 1
			print("left")
		return maquina_turing(cinta, s)

maquina_turing("11100 ", 0)
