#testing
import numpy as np
from tree import Tree, Node
from Tetris_Board import Board
from Tetris_Piece import PieceSet, Piece

from flask import Flask
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
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


	board.print_board()

	square = PieceSet(1)

	move = board.best_move(square)
	return str(move)


@app.route('/tetris-ai', methods=['POST'])
def calculate_best_move():

	req = request.get_json(force=True)
	board_status = req["board"]
	piece_num = req["piece"]

	board = Board(board_status)
	piece = PieceSet(piece_num)

	print(board.best_move(piece))

	return 'Something'


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8080 ,debug = True)





