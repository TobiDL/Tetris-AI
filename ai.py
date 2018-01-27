#testing
import numpy as np
from tree import Tree, Node
from Tetris_Board import Board
from Tetris_Piece import Piece


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
[0,0,1,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0]
])


#initialisation
board = Board(b)
root = Node([], 1, board)
tree = Tree(root)


board.print_board()

print(board.get_avg_height())

#y = Piece(tetris_shape[1])
#x.possible_moves(y)
