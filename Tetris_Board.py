import numpy

class Board:

	def __init__(self):
		self.board = numpy.zeros(shape=(20, 10))


	def possible_moves(self, piece):
		piece.print()


	def print_board(self):
		print(self.board)

	def update_board(self, new_board):
		self.board = new_board



