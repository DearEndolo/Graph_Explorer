from GraphExplorer import Node

class ConceptNode(Node):
	"""docstring for ConceptNode"""
	def __init__(self, name, attributs = dict()):
		super(ConceptNode, self).__init__(name, True)
		self.attributs = attributs.copy()


	def getAttr(self, key):
		return self.attributs[key]

	def addAttr(self, key, value):
		self.attributs[key] = value
		return self.attributs[key] == value

	def updateAttr(self, key, value):
		self.attributs[key] = value
