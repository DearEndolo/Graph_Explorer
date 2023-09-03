class Queue:
	
	# Constructeur
	# Entrée : liste (facultative, par défaut : liste vide)
	def __init__(self, queueList = []):
		# Représentation de la file en liste python
		self.queueList = queueList
		
	# Procédure d'enfilage
	# Entrée : element
	def stack(self, a):
		if(self.isEmpty()):
			self.queueList = [a]
		else:
			self.queueList.append(a)

	# Fonction de défilement 
	# Sortie : Plus ancien élement ajouté à la liste encore dans la liste
	def unstack(self):
		if(self.isEmpty()):
			return None
		obj = self.queueList[0]
		self.queueList.pop(0)
		return obj

	# Fonction qui vérifie si la file est vide
	# Sortie : True si vide, False sinon
	def isEmpty(self):
		return self.queueList == None or self.queueList == []