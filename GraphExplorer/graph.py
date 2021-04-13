from GraphExplorer import Queue, Stack,Relation


class Graph(object):

	# Constructeur
	# Entrée : liste de noeud (facultatif, par défaut : liste vide)
	def __init__(self, set=[]):
		self.set = set
		self.relation = Relation()

	# Procédure d'ajout de noeud au graphe
	def addNode(self, n):
		if(self.set == None):
			self.set = [n]
		else:
			self.set.append(n)

	# Procédure de suppression d'un noeud du graphe
	def deleteNode(self, node):
		node.deleteLinks()
		self.set.pop(self.set.index(node))


	# Fonction de récupération des noeuds du graphes
	# Sorties : liste de noeud
	def getNodeSet(self):
		return self.set

	def path_in_width(self, startingNode):
		queue = Queue()
		for node in self.getNodeSet():
			node.tree = None
			node.distance = None
			node.color = "white"
		#Pour tous les sommets -> mettre en blanc et arbo = None
		startingNode.distance = 0
		queue.stack(startingNode)
		startingNode.color = "grey"

		while not(queue.isEmpty()):
			node = queue.unstack()
			nextNodes = node.getExits()
			for nextNode in nextNodes:
				if nextNode.color == "white":
					queue.stack(nextNode)
					nextNode.color = "grey"
					nextNode.tree = node
					nextNode.distance = node.distance + 1
			nextNodes = node.getEntries()
			for nextNode in nextNodes:
				if nextNode.color == "white":
					queue.stack(nextNode)
					nextNode.color = "grey"
					nextNode.tree = node
					nextNode.distance = node.distance + 1
			node.color = "black"
		return self.tabNiveau()

	def deep_traversal(self, startingNode):
		nodeStack = Stack()
		for node in self.getNodeSet():
			node.marked = False
		startingNode.distance = 0
		nodeStack.stack(startingNode)
		while not(nodeStack.isEmpty()):
			node = nodeStack.unstack()
			if(not(node.marked)):
				node.marked = True
			for child in node.getEntries():
				if(not(child.marked)):
					child.distance = node.distance + 1
					nodeStack.stack(child)
			for child in node.getExits():
				if(not(child.marked)):
					child.distance = node.distance + 1
					nodeStack.stack(child)
		return self.tabNiveau()

	def __same_values_in_it(self, tab1, tab2):
		res = len(tab1) == len(tab2)
		if res:
			for var in tab1:
				res = res and var in tab2
		return res

	def maxNiveau(self):
		maxi = 0
		for node in self.getNodeSet():
			if node.distance > maxi:
				maxi = node.distance
		return maxi

	def tabNiveau(self):
		tab = list()
		for i in range(0,self.maxNiveau()+1):
			tab.append(list())
		for node in self.getNodeSet():
			tab[node.distance].append(node)
		return tab

	def dijkstra(self, startingNode):
		p = Graph()
		nodes = self.getNodeSet()
		for node in nodes:
			node.distance = None
		startingNode.distance = 0
		# On vérfie que les deux graphes ne possèdent pas les mêmes noeuds
		while not(self.__same_values_in_it(p.getNodeSet(), nodes)):
			nodeMinDistance = None
			# On choisit le noeud avec le moins de distance du graphe
			for node in nodes:
				if(node.distance != None and not(node in p.getNodeSet())):
					if (nodeMinDistance != None):
						if(node.distance < nodeMinDistance.distance):
							nodeMinDistance = node
					nodeMinDistance = node
			p.addNode(nodeMinDistance)
			# Pour chaque voisin du noeud on vérifie que sa distance ne s'est pas réduite ou on l'initialise
			for neighbour in nodeMinDistance.getEntries():
				if not(neighbour in p.getNodeSet()):
					if(neighbour.distance == None or neighbour.distance > (nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour))):
						neighbour.distance = nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour) # TODO - y faut recheck ça, ça ne marche pas dans tt les cas .

			for neighbour in nodeMinDistance.getExits():
				if not(neighbour in p.getNodeSet()):
					if(neighbour.distance == None or neighbour.distance > (nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour))):
						neighbour.distance = nodeMinDistance.distance + nodeMinDistance.getWeight(neighbour)
		return self.tabNiveau()

	def search(self, name):
		for node in self.getNodeSet():
			if node.getName() == name:
				return node
		return None

	def size(self):
		return len(self.set)

	def addRelation(self,name):
		self.relation.add(name)

	def getRelation(self,name):
		return self.relation.add(name)

	def existRelation(self, name):
		return self.relation.exist(name)

	def setRelation(self, rel):
		self.relation = rel