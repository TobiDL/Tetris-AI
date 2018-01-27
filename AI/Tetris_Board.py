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

	def get_nb_holes(self):
		holes = 0

		for (x,y), value in np.ndenumerate(self.board_state):
			if 1 <= y <= 8 and x > 0:
				if self.board_state.item((x,y-1)) == 1 and self.board_state.item((x,y+1)) == 1 and self.board_state.item((x-1,y)) == 1 and value == 0:
					holes += 1
		return holes

	def heuristic(self):
		return (-2 * get_nb_holes) + (-1 * get_avg_height)


	def update(self):
		temp = self.board_state
		ctr = 0

		#remove each row that has no 0's
		for i, row in enumerate(self.board_state):
			if 0 not in row:
				temp = np.delete(temp, i-ctr, 0)
				ctr += 1

		#add the lines back on top
		if ctr > 0:
			temp = np.concatenate(([[0,0,0,0,0,0,0,0,0,0]]*ctr, temp), axis = 0)

		self.board_state = temp

	def print_board(self):
		print(self.board_state)

	def update_board(self, new_board):
		self.board_state = new_board


y = Piece(1)

x = Board()

#y.get_shapes()

x.possible_moves(y)