import numpy as np
from Tetris_Piece import PieceSet, Piece
import copy, math

class Board:

	def __init__(self, state = []):

		self.height = 20
		self.width = 10

		self.moves = 0

		if state == []:
			self.board_state = np.zeros(shape=(20, 10))
		else:
			self.board_state = np.matrix(state)

		self.highest_pos = self.get_highest_pos()


	def best_move(self, piece_set):

		possible_moves = self.possible_moves(piece_set)

		score = []

		for board in possible_moves:
			score.append(board.heuristic())

		return possible_moves[score.index(max(score))].moves


	def possible_moves(self, piece_set):

		board_states = []

		for piece in piece_set.get_shapes():
			for i in range(self.width - piece.width + 1):
				board_states.append(self.spawn_piece(i, piece))

		return board_states


	def spawn_piece(self, x, piece):
		
		child = Board(copy.deepcopy(self.board_state))
		board = child.board_state
	
		#first we get the max height
		m = 19 - max(self.highest_pos[x:x+piece.width])

		if False: #better check goes here
			pass
		else:
			for i in range(piece.width):
				for k in range(piece.height):
					board[m-k, x+i] = piece.matrix[piece.height-1-k][i]

		board = self.update(child)
		child.moves = x + math.floor(piece.width/2) - 5
		return child

	def get_highest_pos(self):
		h = [0,0,0,0,0,0,0,0,0,0]
		for (x,y), value in np.ndenumerate(self.board_state):
			if value == 1 and h[y] == 0:
				h[y] = 20-x
		return h

	def get_avg_height(self):
		return sum(self.highest_pos) / len(self.highest_pos)

	def get_nb_holes(self):
		holes = 0

		for (x,y), value in np.ndenumerate(self.board_state):
			if 1 <= y <= 8 and x > 0:
				if self.board_state.item((x,y-1)) == 1 and self.board_state.item((x,y+1)) == 1 and self.board_state.item((x-1,y)) == 1 and value == 0:
					holes += 1
		return holes

	def heuristic(self):
		return (-2 * self.get_nb_holes()) + (-1 * self.get_avg_height())


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

	def set_board(self, new_board):
		self.board_state = copy.deepcopy(new_board)


