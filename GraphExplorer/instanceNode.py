from GraphExplorer import Node, ConceptNode, Relation

class InstanceNode(Node):
	"""docstring for InstanceNode"""

	def __init__(self, name, attributs = dict()):
		super(InstanceNode, self).__init__(name, True)
		self.attributs = attributs.copy()

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