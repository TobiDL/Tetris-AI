import numpy as np

class PieceSet:

    def __init__(self, piece_num):
        pieces = {0: straight_piece,
                  1: L_piece,
                  2: RL_piece,
                  3: square_piece,
                  4: squigly_piece,
                  5: rev_squigly_piece,
                  6: T_piece}

        self.diff_orientation = pieces[piece_num]()


    def get_shapes(self):
        #print(self.shapes)
        return self.shapes


    def straight_piece():
        shapes = [
            [[1, 1, 1, 1]],

            [[1],
             [1],
             [1],
             [1]]
        ]

        return shapes

    def L_piece():
        shapes = [
            [[1, 0],
             [1, 0],
             [1, 1]],

            [[0, 0, 1],
             [1, 1, 1]],

            [[1, 1],
             [0, 1],
             [0, 1]],

            [[1, 1, 1],
             [1, 0, 0]]
        ]

        return shapes

    def RL_piece():
        shapes = [
            [[0, 1],
             [0, 1],
             [1, 1]],

            [[1, 0, 0],
             [1, 1, 1]],

            [[1, 1],
             [1, 0],
             [1, 0]],

            [[1, 1, 1],
             [0, 0, 1]]
        ]

        return shapes

    def square_piece():

        return [[1, 1],
    	        [1, 1]]

    def squigly_piece():
        shapes = [
            [[0, 1, 1],
             [1, 1, 0]],

            [[1, 0],
             [1, 1],
             [0, 1]]
        ]

        return shapes

    def rev_squigly_piece():
        shapes = [
            [[1, 1, 0],
             [0, 1, 1]],

            [[0, 1],
             [1, 1],
             [1, 0]]
        ]

        return shapes

    def T_piece():
        t1 = Piece(
            [[1, 1, 1],
             [0, 1, 0]] , 3, 2)
 
         t2 = Piece(
            [[0, 1, 0],
             [1, 1, 1]] , 3, 2)    


        t3 = Piece(
            [[0, 1],
             [1, 1],
             [0, 1]] , 2, 3)

        t4 = Piece(
            [[1, 0],
             [1, 1],
             [1, 0]] , 2, 3)

        return [t1,t2,t3,t4]

class Piece:

    def __init__(self, matrix = [], w = 0, h = 0):

        self.matrix = matrix
        self.width = w
        self.height = h