class Stack(object):

	# Constructeur
	# Entrée : liste (facultative, par défaut : liste vide)
	def __init__(self, stack_tab = []):
		# Représentation de la pile en liste python
		self.stack_tab = stack_tab
	
	# Procédure d'empilage
	# Entrée : élement
	def stack(self, element):
		if(self.isEmpty()):
			self.stack_tab = [element]
		else:
			self.stack_tab.append(element)

	# Fonction de dépilage 
	# Sortie : Dernier élement ajouté à la liste
	def unstack(self):
		if(self.isEmpty()):
			return None
		return self.stack_tab.pop()

	# Fonction qui vérifie si la pile est vide
	# Sortie : True si vide, False sinon
	def isEmpty(self):
		return self.stack_tab == None or self.stack_tab == []