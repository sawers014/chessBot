"""
0 represent a empty square
1 represent a white pawn
-1 represent a black pawn
3 represent a white bishop
-3 represent a black bishop
2.9 represent a white knight
-2.9 represent a black knight
5 present a white rook
-5 represent a black rook
9 represent a white queen
-9 represent a black queen
10 represent THE white king
-10 represent THE black king
"""
def evaluate(board):
    x=0
    for y in board:
        x=round(x, 1) + y   #need to do this because we cant work with int because it is easier to evaluate some piece with 
                            #decimals based on their position on the board
        print("for now x is equal to ", x)
    return x

              #A   B   C  D  E   F  G    H
initialBoard=[-5,-2.9,-3,-9,-10,-3,-2.9,-5, #8
              -1,-1,  -1,-1, -1,-1,-1,  -1, #7
               0, 0,   0, 0, 0,  0, 0,   0, #6
               0, 0,   0, 0, 0,  0, 0,   0, #5
               0, 0,   0, 0, 0,  0, 0,   0, #4
               0, 0,   0, 0, 0,  0, 0,   0, #3
               1, 1,   1, 1, 1,  1, 1,   1, #2
               5, 2.9, 3, 9, 10, 3, 2.9, 5  #1
              ]
