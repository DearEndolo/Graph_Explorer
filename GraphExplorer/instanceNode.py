from GraphExplorer import Node, ConceptNode, Relation

class InstanceNode(Node):
	"""docstring for InstanceNode"""

	def __init__(self, name, attributs = dict()):
		super(InstanceNode, self).__init__(name, True)
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

	def existAttr(self, key):
		return key in self.attributs

	def getMarked(self):
		return self.marked
	def setMarked(self,value):
		self.marked = value

	def show(self, graph):
		print("{")
		print("\t"+self.name+":")
		for neighbour in self.getExits():
			if(self.getWeight(neighbour) == graph.getRelation("isa")):
				print("\tinherit from "+str(neighbour))
			else:
				print(f"\t{graph.getNameRelation(self,neighbour)} {str(neighbour)}")
		if(len(self.attributs) == 0):
			print("\t\thas no attributes.")
		for attr in self.attributs:
			print("\t\t"+attr+": "+self.attributs[attr])
		print("}")

	def getAttr(self, key):
		if(not(key in self.attributs.keys())):
			return None
		return self.attributs[key]

	def addAttr(self, key, value):
		self.attributs[key] = value
		# return self.attributs[key] == value

	def updateAttr(self, key, value):
		self.attributs[key] = value

	def addExit(self, node, weight = 1):
		super().addExit(node,weight)
		if(type(node) == InstanceNode and not(self in node.getExits())):
			node.addExit(self, weight)