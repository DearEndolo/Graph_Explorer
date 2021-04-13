from GraphExplorer import Node, ConceptNode

class InstanceNode(Node):
	"""docstring for InstanceNode"""

	def __init__(self, name, attributs = dict()):
		super(InstanceNode, self).__init__(name, True)
		self.attributs = attributs.copy()
		
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
		if(not(type(node) == ConceptNode)):
			print("IntanceNodes have to inherit from ConceptNode")
		else:
			super().addExit(node)
