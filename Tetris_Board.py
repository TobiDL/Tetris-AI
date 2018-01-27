import numpy as np
from Tetris_Piece import Piece

class Board:

	def __init__(self, state = []):

		self.height = 20
		self.width = 10

		if state == []:
			self.board_state = np.zeros(shape=(20, 10))
		else:
			self.board_state = state


	def possible_moves(self, pieces):
		for piece in pieces.get_shapes():
			p_h, p_w = self.get_piece_info(piece)
			print(self.width + 1 - p_w)
			for i in range(0, self.width - p_w):
				pass


	def make_piece_fall(self):
		pass

	def is_piece_fallen(self):
		pass

	def is_piece_all_in(self):
		pass

	def get_piece_info(self, piece):
		height = len(piece)
		width = len(piece[0])
		return height, width

	def get_avg_height(self):
		h = [0,0,0,0,0,0,0,0,0,0]
		for (x,y), value in np.ndenumerate(self.board_state):
			if value == 1 and h[y] == 0:
				h[y] = 20-x
		return sum(h) / len(h)

	def heuristic(self):
		pass


	def update_board(self):
		for i, row in enumerate(self.board_state):
			if 0 not in row:
				np.delete()

	def print_board(self):
		print(self.board_state)

	def update_board(self, new_board):
		self.board_state = new_board


y = Piece(1)

x = Board()

#y.get_shapes()

x.possible_moves(y)
