import numpy as np
from Tetris_Piece import Piece

class Board:

	def __init__(self, state = []):

		if state == []:
			self.board_state = np.zeros(shape=(20, 10))
		else:
			self.board_state = state


	def possible_moves(self, piece):
		piece.print()

	def get_avg_height(self):
		h = [0,0,0,0,0,0,0,0,0,0]
		for (x,y), value in np.ndenumerate(self.board_state):
			if value == 1 and h[y] == 0:
				h[y] = 20-x
		return sum(h) / len(h)

	def heuristic(self):
		pass


	def update(self):
		temp = self.board_state
		ctr = 0

		#remove each row that has no 0's
		for i, row in enumerate(self.board_state):
			if 0 not in row:
				temp = np.delete(temp, i-ctr, 0)
				ctr += 1

		#add the lines back on top
		temp = np.concatenate(([[0,0,0,0,0,0,0,0,0,0]]*ctr, temp), axis = 0)

		self.board_state = temp

	def print_board(self):
		print(self.board_state)

	def update_board(self, new_board):
		self.board_state = new_board



