class Tree:

	def __init__(self, r):
		self.root = r


from Tetris_Board import Board

class Node:

	def __init__(self, c = [], v = 0, b = []):

		self.children = c

		self.value = v

		self.board = b


	def generate_children(self, boards):
		
		for board in boards:
			
			value = board.heuristic()
			newChild = Node([] , value, board)
			self.children.append(newChild)

		print("Generated "+len(boards)+" children.")

	def set_value(self, v):
		self.value = v

	def set_board(self, b):
		self.board = b


