from node import Node

class InstanceNode(Node):
	"""docstring for InstanceNode"""

	def __init__(self, name, attributs = dict()):
		super(InstanceNode, self).__init__()
		self.attributs = attributs.copy()


	def get(self, key):
		return self.attributs[key]

	def add(self, key, value):
		self.attributs[key] = value
		# return self.attributs[key] == value

	def addExit(self, node, weight = 1):
		if(not(type(node) == ConceptNode)):
			print("IntanceNodes have to inherit from ConceptNode")
		else:
			super().addExit(node)