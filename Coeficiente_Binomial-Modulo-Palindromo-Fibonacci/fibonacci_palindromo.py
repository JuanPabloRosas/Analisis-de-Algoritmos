
def fibonacci_recursivo(pos):
	actual = 1
	anterior = 0
	res = 0
	if pos == 1:
		print(0)
	elif pos == 2:
		res = actual + anterior
		print(res)
	else:
		pos = pos - 1
		res = actual + anterior
		anterior = actual
		actual = res
		print(res)
		return fibonacci_recursivo(pos)

def fibonacci_iterativo(pos):
        actual = 1
        anterior = 0
        res = 0
        y=2
        if(pos < 1):
                print(0)
        elif(pos == 1):
                res = actual + anterior
                print(res)
        else:
                print(0)
                print(1)
		#print(1)
                actual = 1 
                anterior = 0
                while(y < pos):
                        res = actual + anterior
                        anterior = actual
                        actual = res
                        print(res)
                        y = y + 1

def palindromo_recursivo(palabra):
	if len(palabra) < 2:
		return True
	if not (palabra[0] == palabra[-1]):
		return False
	return palindromo_recursivo(palabra[1:-1])
	
def palindromo_iterativo(palabra):
	x = 0
	longitud = len(palabra) - 1
	while(x < len(palabra)):
		if(palabra[x] == palabra[longitud]):
			flag = True
			longitud = longitud - 1
		else:
			flag = False
			break
		x = x + 1
	return flag

"""
if(palindromo_recursivo("saippuakauppias")):
	print("Es un palindromo  - recursivo")
else:
	print("No es un palindromo - recursivo")

"""
if(palindromo_iterativo("saippuakauppias")):
	print("Es un palindromo  - iterativo")
else:
	print("No es un palindromo - iterativo")

#print(palindromo_recursivo("saippuakauppias"))
#print(palindromo_iterativo("saippuakauppias"))
#fibonacci_iterativo(15)
#fibonacci_recursivo(15)

