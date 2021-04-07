from node import Node

class ConceptNode(Node):
	"""docstring for ConceptNode"""
	def __init__(self, name, attributs = dict()):
		super(ConceptNode, self).__init__(name, True)
		self.attributs = attributs.copy()


	def get(self, key):
		return self.attributs[key]

	def add(self, key, value):
		self.attributs[key] = value
		# return self.attributs[key] == value


