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


def printBoard(board):  # this function prints a chessboard given as input
    index = 0
    for a in range(8):
        print("\n")
        for b in range(8):
            switch = {
                0: ' ',
                -1: '♟︎',
                1: '♙',
                -3: '♝',
                3: '♗',
                -2.9: '♞',
                2.9: '♘',
                -5: '♜',
                5: '♖',
                -9: '♛',
                9: '♕',
                -10: '♚',
                10: '♔'
            }

            # print the piece with a subdivision
            if (a + b) % 2 == 1:
                print("| \033[42;30m ", end="")
            else:
                print("| \033[30;47m ", end="")
            
            print(switch.get(board[index], "Invalid input"), "\033[49;0m ", end="")

            index += 1  # increase the index

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
