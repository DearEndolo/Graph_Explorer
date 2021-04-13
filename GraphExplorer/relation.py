class Relation(object):
	"""docstring for Relation"""

	def __init__(self):
		super(Relation, self).__init__()
		self.relations = dict()
		self.idINC = 1
		addRelation("ako")
		addRelation("isa")
		addRelation("instance")
		addRelation("part_of")
		addRelation("as_part")

	def add(self,name):
		if(not(self.exist(name))):
			print("This relation already exists.")
		else:
			self.relations[name] = self.idINC
			self.idINC = self.idINC + 1

	def get(self,name):
		if(not(self.exist(name))):
			print("This relation doesn't exist")
			return None
		else:
			return self.relations[name]

	def exist(self,name):
		return name in self.relations.keys()
