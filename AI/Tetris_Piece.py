import numpy as np

class Piece:

    def __init__(self, shape):
        shapes = {0: straight_piece,
                  1: L_piece,
                  2: RL_piece,
                  3: square_piece,
                  4: squigly_piece,
                  5: rev_squigly_piece,
                  6: T_piece}

        # self.shape = np.empty((0))
        #
        # for shape in shapes[shape]():
        #     self.shape = np.append(self.shape, shape)

        self.shapes = shapes[shape]()


    def get_shapes(self):
        print(self.shapes)
        return self.shapes


def straight_piece():
    shapes = [
        [[1, 1, 1, 1]],

        [[1],
         [1],
         [1],
         [1]]
    ]

    # npa = np.empty((0))
    #
    # npa = np.append(npa, sh)

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
    shapes = [
        [[1, 1, 1],
         [0, 1, 0]],

        [[0, 1, 0],
         [1, 1, 1]],

        [[0, 1],
         [1, 1],
         [0, 1]],

        [[1, 0],
         [1, 1],
         [1, 0]]
    ]

    return shapes


# y = Piece(2)
#
# print(y.get_shapes()[0])