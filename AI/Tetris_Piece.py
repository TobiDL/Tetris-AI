import numpy as np

class PieceSet:

    def __init__(self, piece_num):
        pieces = {
            0: self.straight_piece,
            1: self.L_piece,
            2: self.RL_piece,
            3: self.square_piece,
            4: self.squigly_piece,
            5: self.rev_squigly_piece,
            6: self.T_piece
        }

        self.diff_orientation = pieces[piece_num]()


    def get_shapes(self):
        #print(self.shapes)
        return self.shapes


    def straight_piece(self):
        s1 = Piece(
            [[1, 1, 1, 1]], 4, 1)

        s2 = Piece(
            [[1],
             [1],
             [1],
             [1]], 1, 4)


        return [s1, s2]

    def L_piece(self):
        l1 = Piece(
            [[1, 0],
             [1, 0],
             [1, 1]], 2, 3)

        l2 = Piece(
            [[0, 0, 1],
             [1, 1, 1]], 3, 2)

        l3 = Piece(
            [[1, 1],
             [0, 1],
             [0, 1]], 2, 3)

        l4 = Piece(
            [[1, 1, 1],
             [1, 0, 0]], 3, 2)

        return [l1,l2, l3, l4]

    def RL_piece(self):
        rl1 = Piece(
            [[0, 1],
             [0, 1],
             [1, 1]], 2, 3)

        rl2 = Piece(
            [[1, 0, 0],
             [1, 1, 1]], 3, 2)

        rl3 = Piece(
            [[1, 1],
             [1, 0],
             [1, 0]], 2, 3)

        rl4 = Piece(
            [[1, 1, 1],
             [0, 0, 1]], 3, 2)

        return [rl1, rl2, rl3, rl4]

    def square_piece(self):

        s = Piece(
            [[1, 1],
    	     [1, 1]], 2, 2)

        return s

    def squigly_piece(self):
        s1 = Piece(
            [[0, 1, 1],
             [1, 1, 0]], 3, 2)

        s2 = Piece(
            [[1, 0],
             [1, 1],
             [0, 1]], 2, 3)


        return [s1, s2]

    def rev_squigly_piece(self):
        rs1 = Piece(
            [[1, 1, 0],
             [0, 1, 1]], 3, 2)

        rs2 = Piece(
            [[0, 1],
             [1, 1],
             [1, 0]], 2, 3)


        return [rs1, rs2]

    def T_piece(self):
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

