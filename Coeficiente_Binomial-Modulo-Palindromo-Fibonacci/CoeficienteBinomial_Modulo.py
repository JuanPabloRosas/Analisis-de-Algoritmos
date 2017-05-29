from math import log, exp
import sys

def CoefBinomial( n, k, Coef, base)
	if k > n-k:
		mayor = n
		menor = n-k
	else:
		mayor = n-k
		menor = k
	if Coef:
		fact1 = 1
		fact2 = 1
		while mayor != k:
			fact1 = fact1 * mayor
			mayor = mayor -1
		while menor != 0 :
			fact2= fact2 * menor
			menor = menor -1
		res = fact1 / fact2
	else:
		log1 = 0
		log2 = 0
		while mayor != k:
			log1 = log1 + log(mayor)
			mayor = mayor - 1
		while menor != 0 :
			log2= log2 + log(menor)
			menor = menor - 1
		for x in xrange(1,10):
			res =  exp((log1 - log2))
	return res
	
def Modulo(num, exp, mod):
	r = 1
	x = num
	while exp > 0:
		if exp % 2 == 1:
			r *= num
			r = r % mod
			num *= num
			num = num % mod
		exp >>= 1
		#print(exp)
	return r 

"""
x = int(sys.argv[1])
e = int(sys.argv[2])
m = int(sys.argv[3])
#print("Modulo",Modulo(x, e, m))
#print("Modulo2",x**e % m)
"""

print(CoefBinomial(9,7,3,2))

