# EQUIPO:
#Jose Anastacio Hernandez Saldaña
#Juan Pablo Rosas Baldazo
#######################################

from heapq import heappush, heappop
import bintrees as b

def lineas_de_barrer(archivo):
	heap = []
	cont = -1
	file = archivo.open(archivo,'r')
	sl = 0
	sr = 0
	puntos = {}
	for line in file:
		cont += 1
		v = line.split(' ')
		puntos[cont] = v 
		if v[0] <= v[2]:
			heappush(heap,(v[0],v[1],'C',cont,'-'))
			heappush(heap,(v[2],v[3],'F',cont,'-'))
		else:
			heappush(heap,(v[0],v[1],'F',cont,'-'))
			heappush(heap,(v[2],v[3],'C',cont,'-'))
	arbol = b.AVLTree()
	while len(heap) > 0:
		menor = heappop(heap)
		if menor[2] =='C':
			arbol[menor[1]] = menor
			try:			
				pred = arbol.prev_item(menor[1])
			except:
				pred = None
			if pred:
				cont1 = menor[3]
				cont2 = pred[3]
				ix,iy = interseccion(puntos[cont1][0],puntos[cont1][1],puntos[cont1][2],puntos[cont1][3],puntos[cont2][0],puntos[cont2][1],puntos[cont2][2],puntos[cont2][3])
			
				if ix > menor[0]:
					heappush(heap,(ix,iy,'i',pred[3],cont))

			try:			
				suc = arbol.succ_item(menor[1])
			except:
				suc = None
			if suc:
				cont1 = menor[3]
				cont2 = suc[3]
				ix,iy = interseccion(puntos[cont1][0],puntos[cont1][1],puntos[cont1][2],puntos[cont1][3],puntos[cont2][0],puntos[cont2][1],puntos[cont2][2],puntos[cont2][3])
				
				if ix > menor[0]:
					heappush(heap,(ix,iy,'i',pred[3],cont))

		if menor[2] == 'F':
			try:			
				pred = arbol.prev_item(menor[1])
			except:
				pred = None
			try:			
				suc = arbol.succ_item(menor[1])
			except:
				suc = None
				arbol.remove(menor)
			if pred is None and suc is None:
				cont1 = pred[3]
				cont2 = suc[3]

				ix,iy = interseccion(puntos[cont1][0],puntos[cont1][1],puntos[cont1][2],puntos[cont1][3],puntos[cont2][0],puntos[cont2][1],puntos[cont2][2],puntos[cont2][3])
				if ix > menor[0]:
					heappush(heap,(ix,iy,'i',pred[3],suc[3]))
		if menor[2] == 'i':
			i = menor[3]
			j = menor[4]

			print(menor)


def interseccion(xc1,yc1,xf1,yf1,xc2,yc2,xf2,yf2):
	m1 = (yf1-yc1)/(xf1-xc1)
	m2 = (yf2-yc2)/(xf2-xc2)

	b1 = yc1-(m1*xc1)
	b2 = yc2-(m2*xc2)

	x = ((m1*x1)+b1-b2)/m2

	y = (m2*xc2) + b2
	
	return x,y

	

