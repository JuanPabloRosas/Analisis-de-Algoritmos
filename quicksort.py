import random
costo = 0
def quicksort(arr):
	global costo
	menor = list()
	mayor = list()
	if len(arr) > 3:
		#pivote = arr[len(arr)/2]
		pivote = arr[random.randint(0,len(arr)-1)]
		#print("pivote: ",pivote)
		#print("arr: ",arr)
		for i in range(0, len(arr)):
			if arr[i] <= pivote:
				menor.append(arr[i])
				costo = costo + 1
			else:
				mayor.append(arr[i])
				costo = costo + 1
	
	else:
		arr.sort()
		return arr
	costo = costo + 1
	return quicksort(menor) + quicksort(mayor)
	

def arr_dinamicos(secuencia):
	capacidad = 6
	llenado = 0	
	umbral_sup = capacidad - 1 
	umbral_inf = 2
	costo = 0
	print("secuencia: ",secuencia)
	for i in secuencia:
		if i == -1:
			llenado = llenado - 1
			#print("llenado: ", i ,"-", llenado)
			costo = costo + 1
			if llenado <= umbral_inf:
				costo = costo + (llenado*-1)
				if capacidad > 3:
					capacidad = capacidad / 2 
					umbral_sup = capacidad - 2 
				else:
					print("No hay capacidad")
					break
		else:
			llenado = llenado + 1
			#print("llenado: ", i ,"-", llenado)
			if llenado >= umbral_sup:
				capacidad = capacidad * 2
				costo = costo + llenado
				umbral_sup = capacidad - 2
		
	print("capacidad final: ",capacidad)
	print("llenado: ",llenado)
	print("umbral_sup: ",umbral_sup)
	print("umbral_inf: ",umbral_inf)
	
	return costo
			



#arr = [1,1,1,-1,-1,1,1,1,1,-1]
#arr = [1,1,1,1,1,1,1,1,1,1]
#arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
#print("costo: ",arr_dinamicos(arr))





arr0 = random.sample(range(0,100),99)
arr1 = random.sample(range(0,1000),999)
arr2 = random.sample(range(0,10000),9999)

#arr = list({12,4,43,35,53,15,1,7,8,19,47})	
#print(arr)

costo_suma = 0
for i in range(0, 10):
	arr = random.sample(range(0,100),99)
	quicksort(arr)
	#print(i ,",",costo)	
	costo_suma = costo_suma + costo	
	costo = 0
promedio = costo_suma /10
print(costo_suma, promedio) 

for i in range(0, 10):
	arr = random.sample(range(0,1000),999)
	quicksort(arr1)
	costo_suma = costo_suma + costo	
	costo = 0
promedio = costo_suma /10 
print(costo_suma, promedio)

for i in range(0, 10):
	arr = random.sample(range(0,10000),9999)
	quicksort(arr)
	costo_suma = costo_suma + costo	
	costo = 0
promedio = costo_suma /10 
print(costo_suma, promedio)

for i in range(0, 10):
	arr = random.sample(range(0,100000),99999)
	quicksort(arr)
	costo_suma = costo_suma + costo	
	costo = 0
promedio = costo_suma /10 
print(costo_suma, promedio)


#print(quicksort(arr2))
#print("costo: " ,costo)



