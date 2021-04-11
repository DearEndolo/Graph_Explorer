from GraphExplorer import Node

class InstanceNode(Node):
	"""docstring for InstanceNode"""

	def __init__(self, name, attributs = dict()):
		super(InstanceNode, self).__init__()
		self.attributs = attributs.copy()

	def show(self):
		print("{"+self.name+":")
		for attr in self.attributs:
			print("\t"+attr+": "+self.attributs[attr])
		print("}")

	def getAttr(self, key):
		return self.attributs[key]

	def addAttr(self, key, value):
		self.attributs[key] = value
		# return self.attributs[key] == value

	def updateAttr(self, key, value):
		self.attributs[key] = value

	def addExit(self, node, weight = 1):
		if(not(type(node) == ConceptNode)):
			print("IntanceNodes have to inherit from ConceptNode")
		else:
			super().addExit(node)
