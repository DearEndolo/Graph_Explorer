class Relation:
	"""docstring for Relation"""

	AKO = 1
	ISA = 2
	PART_OF = 3
	AS_PART = 4



	def __init__(self):
		super(Relation, self).__init__()
		self.relations = dict()
		self.idINC = 1
		self.add("ako")
		self.add("isa")
		self.add("part_of")
		self.add("as_part")

	def add(self,name):
		if(self.exist(name)):
			pass
			#print("This relation already exists.")
		else:
			#print(f"The relation {name} has been added.")
			self.relations[name] = self.idINC
			self.idINC = self.idINC + 1

	def get(self,name):
		if(not(self.exist(name))):
			#print("This relation doesn't exist")
			return None
		else:
			return self.relations[name]

	def exist(self,name):
		return name in self.relations.keys()

	def getAllRelations(self):
		return self.relations

	def getNameByValue(self, value):
		for k in self.relations.keys():
			if(self.relations[k] == value):
				return k