class Tree:

	def __init__(self, r):

		self.root = r



class Node:

	def __init__(self, c = [], v = 0, b = []):

		self.children = c

		self.value = v

		self.board = b


	def generate_children(self, boards):
		for i in boards:
			#generate children
			pass

	def set_value(self, v):
		self.value = v

	def set_board(self, b):

		self.board = b


#testing

root = Node([], 1)

tree = Tree(root)