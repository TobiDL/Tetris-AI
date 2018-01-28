import numpy as np
from Tetris_Piece import PieceSet, Piece
import copy

class Board:

	def __init__(self, state = []):

		self.height = 20
		self.width = 10

		if state == []:
			self.board_state = np.zeros(shape=(20, 10))
		else:
			self.board_state = state

		self.highest_pos = self.get_highest_pos()



	def possible_moves(self, piece_set):

		board_states = []

		for piece in piece_set.get_shapes():
			for i in range(self.width - piece.width + 1):
				board_states.append(self.spawn_piece(i, piece))

		return board_states


	def spawn_piece(self, x, piece):
		
		temp = copy.deepcopy(self.board_state)

		#first we get the max height
		m = 19 - max(self.highest_pos[x:x+piece.width])

		if False: #better check goes here
			pass
		else:
			for i in range(piece.width):
				for k in range(piece.height):
					temp[m-k, x+i] = piece.matrix[piece.height-1-k][i]

		temp = self.update(temp)
		print(temp)
		return temp

	def get_highest_pos(self):
		h = [0,0,0,0,0,0,0,0,0,0]
		for (x,y), value in np.ndenumerate(self.board_state):
			if value == 1 and h[y] == 0:
				h[y] = 20-x
		return h

	def get_avg_height(self):
		return sum(self.highest_pos) / len(highest_pos)

	def get_nb_holes(self):
		holes = 0

		for (x,y), value in np.ndenumerate(self.board_state):
			if 1 <= y <= 8 and x > 0:
				if self.board_state.item((x,y-1)) == 1 and self.board_state.item((x,y+1)) == 1 and self.board_state.item((x-1,y)) == 1 and value == 0:
					holes += 1
		return holes

	def heuristic(self):
		return (-2 * get_nb_holes) + (-1 * get_avg_height)


	def update(self, t):
		temp = t
		ctr = 0

		#remove each row that has no 0's
		for i, row in enumerate(self.board_state):
			if 0 not in row:
				temp = np.delete(temp, i-ctr, 0)
				ctr += 1

		#add the lines back on top
		if ctr > 0:
			temp = np.concatenate(([[0,0,0,0,0,0,0,0,0,0]]*ctr, temp), axis = 0)

		return temp

	def print_board(self):
		print(self.board_state)

	def update_board(self, new_board):
		self.board_state = new_board


