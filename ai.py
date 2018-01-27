from Tetris_Piece import Piece
from Tetris_Board import Board

tetris_shape = [
	[[1, 1, 1],
	 [0, 1, 0]],

	[[0, 1, 1],
	 [1, 1, 0]],

	[[1, 1, 0],
	 [0, 1, 1]],

	[[1, 0, 0],
	 [1, 1, 1]],

	[[0, 0, 1],
	 [1, 1, 1]],

	[[1, 1, 1, 1]],

	[[1, 1],
	 [1, 1]]
]

x = Board()

x.print_board()

y = Piece(tetris_shape[1])
x.possible_moves(y)