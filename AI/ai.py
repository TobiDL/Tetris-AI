#testing
import numpy as np
from AI.tree import Tree, Node
from AI.Tetris_Board import Board
from AI.Tetris_Piece import Piece


b = np.matrix([
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0],
[1,1,1,1,0,1,1,1,1,1],
[1,1,1,1,1,1,0,1,1,1]
])


#initialisation
board = Board(b)
root = Node([], 1, board)
tree = Tree(root)

board.update()

board.print_board()

print(board.get_avg_height())

print(board.get_nb_holes())

#y = Piece(tetris_shape[1])
#x.possible_moves(y)

