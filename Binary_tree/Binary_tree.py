class nodo:
	def __init__(self,nodo):
		self.raiz = nodo
		self.left = None
		self.right = None
		
	def add(self , nodo):
		print("raiz:" , self.raiz)	
		if(nodo < self.raiz):
			if self.left is None:
				self.left = nodo
			else:
				if(nodo < self.left):
					nodo(self.left).left= nodo
				else:
					nodo(self.left)
					print("aadsfag")
					#self(self.right).right= nodo
		else: 
			if self.right is None:
				self.right = nodo
			else:
				if(nodo < self.right):
					nodo(self.right)
					self.left= nodo
	
		print("left:" , self.left)
		print("right:" , self.right)
				

raiz = nodo(15)
raiz.add(16)
raiz.add(13)
raiz.add(17)
raiz.add(14)
