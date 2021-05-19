import random

computadora, oponente = 'x', 'o'

"""
Es la función que asigna el valor a cada uno de los estados del tablero

Devuelve (Entero):
La diferencia de las posibilidades de ganar de la computadora menos las
posibilidades de ganar del jugador. Las posibilidades se obtienen verificando
en que renglon, columna o diagonal puede generar una jugada ganadora en un futuro, es decir
si tenemos el siguiente tablero:
x.- Computadora
o.- Jugador

_  o  _
x  _  _
_  _  _
La comptadora tendría 6 posibilidades de ganar, si agregara las demás 'x' correspondientes.
_  o  _		x  o  _		x  o  _		_  o  x		_  o  _		_  o  x      
x  x  x		x  _  _		x  x  _		x  x  _		x  _  _		x  _  x
_  _  _		x  _  _		_  _  x		x  _  _		x  x  x		_  _  x
El jugador tendría de igual manera 6 posibilidades de ganar
o  o  o		_  o  _		_  o  _		_  o  o		_  o  o		o  o  _      
x  _  _		x  _  _		x  o  _		x  _  o		x  o  _		x  o  _
_  _  _		o  o  o		_  o  _		_  _  o		o  _  _		_  _  o
Por lo que el valor de ese estado sería 6 - 6 = 0

"""
def f_valor(t):
	j = 0
	o = 0

	# Renglones
	for renglon in range(3) :	
		if ((t[renglon][0] == '_' and t[renglon][1] == '_' and t[renglon][2] == '_') or 
			(t[renglon][0] == 'x' and t[renglon][1] == '_ 'and t[renglon][2] == '_') or 
			(t[renglon][0] == '_' and t[renglon][1] == 'x' and t[renglon][2] == '_') or 
			(t[renglon][0] == '_' and t[renglon][1] == '_' and t[renglon][2] == 'x') or 
			(t[renglon][0] == 'x' and t[renglon][1] == 'x' and t[renglon][2] == '_') or 
			(t[renglon][0] == '_' and t[renglon][1] == 'x' and t[renglon][2] == 'x')):	
			j = j + 1

	# Columnas
	for col in range(3) :
		if ((t[0][col] == '_' and t[1][col] == '_' and t[2][col] == '_') or
			(t[0][col] == 'x' and t[1][col] == '_' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == 'x' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == '_' and t[2][col] == 'x') or
			(t[0][col] == 'x' and t[1][col] == 'x' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == 'x' and t[2][col] == 'x')) :
			j = j + 1

	# Diagonales
	if ((t[0][0] == '_' and t[1][1] == '_'and t[2][2] == '_') or
		(t[0][0] == 'x' and t[1][1] == '_'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == 'x'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == '_'and t[2][2] == 'x') or
		(t[0][0] == 'x' and t[1][1] == 'x'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == 'x'and t[2][2] == 'x')) :
		j = j + 1

	if ((t[0][2] == '_' and t[1][1] == '_' and t[2][0] == '_') or 
		(t[0][2] == 'x' and t[1][1] == '_' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == 'x' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == '_' and t[2][0] == 'x') or
		(t[0][2] == 'x' and t[1][1] == 'x' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == 'x' and t[2][0] == 'x')) :
		j = j + 1

	#	OPONENTE
	# Renglones
	for renglon in range(3) :	
		if ((t[renglon][0] == '_' and t[renglon][1] == '_' and t[renglon][2] == '_') or 
			(t[renglon][0] == 'o' and t[renglon][1] == '_ 'and t[renglon][2] == '_') or 
			(t[renglon][0] == '_' and t[renglon][1] == '_' and t[renglon][2] == 'o') or 
			(t[renglon][0] == 'o' and t[renglon][1] == 'o' and t[renglon][2] == '_') or 
			(t[renglon][0] == '_' and t[renglon][1] == 'o' and t[renglon][2] == 'o')):	
			o = o + 1

	# Columnas
	for col in range(3) :
		if ((t[0][col] == '_' and t[1][col] == '_' and t[2][col] == '_') or
			(t[0][col] == 'o' and t[1][col] == '_' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == 'o' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == '_' and t[2][col] == 'o') or
			(t[0][col] == 'o' and t[1][col] == 'o' and t[2][col] == '_') or
			(t[0][col] == '_' and t[1][col] == 'o' and t[2][col] == 'o')) :
			o = o + 1

	# Diagonales
	if ((t[0][0] == '_' and t[1][1] == '_'and t[2][2] == '_') or
		(t[0][0] == 'o' and t[1][1] == '_'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == 'o'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == '_'and t[2][2] == 'o') or
		(t[0][0] == 'o' and t[1][1] == 'o'and t[2][2] == '_') or
		(t[0][0] == '_' and t[1][1] == 'o'and t[2][2] == 'o')) :
		o = o + 1

	if ((t[0][2] == '_' and t[1][1] == '_' and t[2][0] == '_') or 
		(t[0][2] == 'o' and t[1][1] == '_' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == 'o' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == '_' and t[2][0] == 'o') or
		(t[0][2] == 'o' and t[1][1] == 'o' and t[2][0] == '_') or
		(t[0][2] == '_' and t[1][1] == 'o' and t[2][0] == 'o')) :
		o = o + 1

	return(j-o)


"""
Funciona recursivamente suponiendo cuál será la jugada del contrincante, de acuerdo a una función de valor f_valor()
maximizando las posibilidades de ganar y minimizando las posibilidades del contrincante.

Devuelve (Entero)
El valor del mejor estado encontrado.
"""
def minimax(tablero, profundidad, Max):
	g = ganador(tablero)
	if((g == 0) or (g == 1)):
		return(f_valor(tablero))

	# Es el turno de la computadora
	if (Max) :
		best = -100000
		for i in range(3) :		
			for j in range(3) :			
				if (tablero[i][j] =='_') :
					tablero[i][j] = computadora
					puntos = max(best, f_valor(tablero))
					best = max(puntos, minimax(tablero, profundidad + 1, not Max))
					tablero[i][j] = '_'

	# Turno del oponente
	else :
		best = 100000
		for i in range(3) :		
			for j in range(3) :
				if (tablero[i][j] == '_') :
					tablero[i][j] = oponente
					puntos = min(best, f_valor(tablero))
					best = min(puntos, minimax(tablero, profundidad + 1, not Max))
					tablero[i][j] = '_'
	return best

"""
Identifica si alguien quién es el ganador , si contuamos jugando o si empatamos.

Devuelve (Entero):
0 .- si gana la computadora
1 .- si gana el jugador
2 .- si hubo un empate
-1.- si aún no se termina el juego
"""
def ganador(tablero):
	for renglon in range(3) :
		if(tablero[renglon][0] == 'x' and tablero[renglon][1] == 'x' and tablero[renglon][2] == 'x'):
			return 0
	for col in range(3) :
		if(tablero[0][col] == 'x' and tablero[1][col] == 'x' and tablero[2][col] == 'x'):
			return 0

	if((tablero[0][0] == 'x' and tablero[1][1] == 'x'and tablero[2][2] == 'x') or
		(tablero[0][2] == 'x' and tablero[1][1] == 'x' and tablero[2][0] == 'x')):
		return 0

	for renglon in range(3) :	
		if(tablero[renglon][0] == 'o' and tablero[renglon][1] == 'o' and tablero[renglon][2] == 'o'):
			return 1

	for col in range(3) :
		if(tablero[0][col] == 'o' and tablero[1][col] == 'o' and tablero[2][col] == 'o'):
			return 1

	if((tablero[0][0] == 'o' and tablero[1][1] == 'o'and tablero[2][2] == 'o') or
		(tablero[0][2] == 'o' and tablero[1][1] == 'o' and tablero[2][0] == 'o')):
		return 1

	if(not any('_' in t for t in tablero)):
		return 2

	return -1

"""
Función principal. Realiza el mejor movimiento encontrado por de la computadora con un algoritmo minimax
y espera a que el jugador realice su jugada. De esta forma iterativamente hasta que haya un ganador o 
se empate el juego

Devuelve (Entero):
0 .- si gana la computadora
1 .- si gana el jugador
2 .- si hubo un empate
-1.- si aún no se termina el juego
"""
def mejorMovimiento(tablero) :
	if(any('x' in t for t in tablero)):
		bestVal = -1000
		bestMov = (-1, -1)
		for i in range(3) :	
			for j in range(3):
				if (tablero[i][j] == '_'):
					tablero[i][j] = computadora
					movVal = minimax(tablero, 0, False)
					tablero[i][j] = '_'
					if (movVal > bestVal):			
						bestMov = (i, j)
						bestVal = movVal

		tablero[bestMov[0]][bestMov[1]] = computadora
		print()
		print('   0     1    2')
		print('0 ',tablero[0])
		print('1 ',tablero[1])
		print('2 ',tablero[2])
		print()
		g = ganador(tablero)
		if(g == 0):
			return 0
		if(g == 1):
			return 1
		if(g == 2):
			return 2
		flag = True
		while(flag):
			renglon = input('Ingresa un renglon:')
			columna = input('Ingresa una columna:')
			if(tablero[int(renglon)][int(columna)] == '_' ):
				flag = False
				tablero[int(renglon)][int(columna)] = oponente
			else:
				print("Ese lugar ya está marcado, elige otro...")
		print()
		print('    0      1     2')
		print('0 ',tablero[0])
		print('1 ',tablero[1])
		print('2 ',tablero[2])
		print()
		g = ganador(tablero)
		if(g == 0):
			return 0
		if(g == 1):
			return 1
		if(g == 2):
			return 2
	else:
		tablero[random.randint(0, 2)][random.randint(0, 2)] = computadora
		print()
		print('   0     1    2')
		print('0',tablero[0])
		print('1',tablero[1])
		print('2',tablero[2])
		print()
		flag = True
		while(flag):
			renglon = input('Ingresa un renglon:')
			columna = input('Ingresa una columna:')
			if(tablero[int(renglon)][int(columna)] == '_' ):
				flag = False
				tablero[int(renglon)][int(columna)] = oponente
			else:
				print("Ese lugar ya está marcado, elige otro...")
		print()
		print('   0     1    2')
		print('0',tablero[0])
		print('1',tablero[1])
		print('2',tablero[2])
		print()
	return -1


tablero = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]

gana=-1
while(gana < 0):
	gana = mejorMovimiento(tablero)
	if(gana == 0):
		print('Perdiste!!')
	if(gana == 1):
		print('Ganaste!!')
	if(gana == 2):
		print('Empate!!')
