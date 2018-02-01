import numpy as np
from Tetris_Piece import PieceSet, Piece
import copy, math, time

class Board:

	def __init__(self, state = []):

		self.height = 20
		self.width = 10

		self.moves = 0
		self.latest_piece = None
		self.value = 0

		if len(state) == 0:
			self.board_state = np.zeros(shape=(20, 10))
		else:
			self.board_state = np.matrix(state)

		self.highest_pos = self.get_highest_pos()

	def best_move(self, piece_set):

		possible_moves = self.possible_moves(piece_set)

		score = []

		for board in possible_moves:
			score.append(board.value)

		print("Score:",max(score))
		print(possible_moves[score.index(max(score))].board_state)


		return possible_moves[score.index(max(score))]


	def possible_moves(self, piece_set):

		board_states = []
		pieces = []

		for piece in piece_set.get_shapes():
			for i in range(self.width - piece.width + 1):
				board_states.append(self.spawn_piece(i, piece))


		return board_states


	def spawn_piece(self, x, piece):

		child = Board(copy.deepcopy(self.board_state))
		board = child.board_state

		child.latest_piece = piece

		#first we get the max height
		m = 19 - max(self.highest_pos[x:x+piece.width])
		diff = []

		#checks if piece can go below
		if m < 19:
			for i in range(piece.width):
				diff.append(board[m+1, x+i] * piece.matrix[piece.height-1][i])
			if sum(diff) == 0:
				m += 1

				#check again
				if m < 19:
					for i in range(piece.width):
						diff.append(board[m+1, x+i] * piece.matrix[piece.height-2][i])
					if sum(diff) == 0:
						m += 1

		for i in range(piece.width):
			for k in range(piece.height):
				if piece.matrix[piece.height-1-k][i] == 1:
					board[m-k, x+i] = piece.matrix[piece.height-1-k][i]


		clears = child.update()

		child.value = child.heuristic()
		child.value += clears*100

		child.moves = x
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

			#checks if empty square is covered by above block
			if x > 0 and self.board_state.item((x,y)) == 0 and self.board_state.item((x-1,y)) == 1:
				holes += 1

			#cheks if surrounded
			if 1 <= y <= 8 and x > 0:
				if self.board_state.item((x,y-1)) == 1 and self.board_state.item((x,y+1)) == 1 and self.board_state.item((x-1,y)) == 1 and value == 0:
					holes += 5

		return holes

	def heuristic(self):
		holes_weight = -3
		avg_height_weight = -1
		max_height_weight = -1

		holes = self.get_nb_holes()
		avg_height = self.get_avg_height()
		max_height = max(self.highest_pos)

		return holes_weight * holes + avg_height_weight * avg_height + max_height_weight * max_height


	def update(self):
		
		ctr = 0

		#remove each row that has no 0's
		for i, row in enumerate(self.board_state):
			if 0 not in row:
				self.board_state = np.delete(self.board_state, i-ctr, 0)
				ctr += 1

		#add the lines back on top
		if ctr > 0:
			self.board_state = np.concatenate(([[0,0,0,0,0,0,0,0,0,0]]*ctr, self.board_state), axis = 0)

		self.highest_pos = self.get_highest_pos()

		return ctr


	def print_board(self):
		print(self.board_state)

	def set_board(self, new_board):
		self.board_state = copy.deepcopy(new_board)


