
notation = {
    0: "a8", 1:"b8", 2:"c8", 3:"d8", 4:"e8", 5:"f8", 6:"g8", 7:"h8",
    8: "a7",9: "b7",10:"c7",11:"d7",12:"e7",13:"f7",14:"g7",15:"h7",
    16:"a6",17:"b6",18:"c6",19:"d6",20:"e6",21:"f6",22:"g6",23:"h6",
    24:"a5",25:"b5",26:"c5",27:"d5",28:"e5",29:"f5",30:"g5",31:"h5",
    32:"a4",33:"b4",34:"c4",35:"d4",36:"e4",37:"f4",38:"g4",39:"h4",
    40:"a3",41:"b3",42:"c3",43:"d3",44:"e3",45:"f3",46:"g3",47:"h3",
    48:"a2",49:"b2",50:"c2",51:"d2",52:"e2",53:"f2",54:"g2",55:"h2",
    56:"a1",57:"b1",58:"c1",59:"d1",60:"e1",61:"f1",62:"g1",63:"h1"   
}
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


def possibleMoves(board, index):
    moves = []
    piece = board[index]

    if piece == 1:  # White pawn
        if board[index - 8] == 0:
            moves.append(index - 8)
            if board[index - 16] == 0 and index >= 48 and index <= 55:
                moves.append(index - 16)

    elif piece == -1:  # Black pawn
        if board[index + 8] == 0:
            moves.append(index + 8)
            if board[index + 16] == 0 and index >= 8 and index <= 15:
                moves.append(index + 16)

    elif piece == 5 or piece ==9:  # White rook or white queen (we will only calculate linear moves in this part)
        row, col = divmod(index, 8)
        # Horizontal moves to the right
        for i in range(col + 1, 8):
            if board[row * 8 + i] <=0:
                moves.append(row * 8 + i)

                if not board[row * 8 + i] < 0: 
                    break
            else:
                break

        # Horizontal moves to the left
        for i in range(col - 1, -1, -1):
            if board[row * 8 + i] <= 0:
                moves.append(row * 8 + i)
                if not board[row * 8 + i] < 0: 
                    break
            else:
                break

        # Vertical moves upward
        for i in range(row + 1, 8):
            if board[i * 8 + col] <= 0:
                moves.append(i * 8 + col)
                if board[i * 8 + col] < 0: 
                    break
            else:
                break

        # Vertical moves downward
        for i in range(row - 1, -1, -1):
            if board[i * 8 + col] <= 0:
                moves.append(i * 8 + col)
                if board[i * 8 + col] < 0:
                    break
            else:
                break

    return moves

print(possibleMoves(initialBoard, 56), "ass")  # Example: get possible moves for the piece at index 63 (h1)
