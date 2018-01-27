class Piece:

    def __init__(self, shape):
        shapes = {0: straight_piece,
                  1: RL_piece,
                  2: L_piece,
                  3: square_piece,
                  4: squigly_piece,
                  5: rev_squigly_piece,
                  6: T_piece}

        self.shape = shapes[shape]()


    def get_shape(self):
        print(self.shape)


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
