class Graph(object):

	# Constructeur
	# Entrée : liste de noeud (facultatif, par défaut : liste vide)
	def __init__(self, set=[]):
		self.set = set

	# Procédure d'ajout de noeud au graphe
	def addNode(self, n):
		if(self.set == None):
			self.set = [n]
		else:
			self.set.append(n)

	# Fonction de récupération des noeuds du graphes
	# Sorties : liste de noeud
	def getNodeSet(self):
		return self.set