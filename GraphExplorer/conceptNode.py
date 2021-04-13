from GraphExplorer import Node

class ConceptNode(Node):
	"""docstring for ConceptNode"""
	def __init__(self, name, attributs = dict()):
		super(ConceptNode, self).__init__(name, True)
		self.attributs = attributs.copy()
		self.color = None
		self.marked = False
		self.distance = None

	def getDistance(self):
		return self.distance
	def setDistance(self,value):
		self.distance = value

	def getColor(self):
		return self.color
	def setColor(self,value):
		self.color = value

	def getMarked(self):
		return self.marked
	def setMarked(self,value):
		self.marked = value

	def show(self,graph):
		print("{")
		print("\t"+self.name+":")
		for daron in self.getExits():
			print("\tinherit from "+str(daron))
		if(len(self.attributs) == 0):
			print("\t\thas no attributes.")
		for attr in self.attributs:
			print("\t\t"+attr+": "+self.attributs[attr])
		print("}")


	def getAttr(self, key):
		return self.attributs[key]

	def addAttr(self, key, value):
		self.attributs[key] = value
		return self.attributs[key] == value

	def updateAttr(self, key, value):
		self.attributs[key] = value
