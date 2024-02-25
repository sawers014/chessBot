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
"""
TODO:
-ability to create treats;
-function to see checkmate in 1;
-ability to try and avoid pins;
"""
from possibleMoves import *     #import other functions

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

def isKingChecked(board, index):
    
    #board is the chessboard, index represent the index of the king
    moves=[]
    # array that will contain all the index of the possible moves of the opposing color,
    # if the king index IS in this array, then the king is indeed in check 
    

    #black king in check?
    if board[index]<0:
        for x in range(64):#cycle through the index of the array
            try:
                if board[x]>0: #we only want opposing color pieces.
                    moves.append(possibleMoves(board, x))
            except: continue
        #white king
    else:
        for x in range(64):#cycle through the index of the array
            try:
                if board[x]<0: #we only want opposing color pieces.
                    moves.append(possibleMoves(board, x))
            except: continue
        pass

    if any(index in sublist for sublist in moves):
        return True
        


def evaluate(board, turn):  
    # board is the chessboard, turn is a variable that is either True(White) or False(Black)
    x = 0
       
    for index in range(len(board)):  # its useful to cycle by index
        # its better to do, so we can understand what piece we are calculating.
        piece_value = board[index]

        row, col = divmod(index, 8) #its useful to get their position in here 

        # pos, is a variable that contain the arrays of possible moves of a piece
        pos = possibleMoves(board, index)

        # white/black knight 
        if piece_value == 2.9 or piece_value == -2.9:
            position = notation[index]  # localize Where a piece is
            if position[0] == "c" or position[0] == "d" or position[0] == "e" or position[0] == "f":
                # a knight should be valued more because it is in a central position
                # we use the multiplication because we dont know if the knight is white or black
                piece_value *= 1.1  
        
        # white bishop, rook, queen
        elif piece_value == 3 or piece_value==5 or piece_value==9:
            # we do this so that if the piece is more active (controls more square) it is valued more than an unactive piece
            piece_value +=  (0.05 * len(pos))  # we add the possible moves of that piece
       
        # black bishop, rook, queen
        elif piece_value == -3 or piece_value==-5 or piece_value==-9:
            piece_value -=  (0.05 * len(pos))
        
        elif piece_value == 1:  # White pawn

            if row==1:
                piece_value += 1.5 # promotion
            elif row==2:
                piece_value += 0.9 # almost promotion

            if index % 8 != 0:  # Check if not on the left edge
                if index - 9 >= 0 and board[index - 9] == 1:
                    piece_value += 0.1  #pawn chain
            
                    
            if (index + 1) % 8 != 0:  # Check if not on the right edge
                if index - 7 >= 0 and board[index - 7] == 1:
                    piece_value += 0.1

        elif piece_value == -1:  # Black pawn

            if row==8:
                piece_value -= 1.5 # promotion
            elif row==7:
                piece_value -= 0.9 # almost promotion    

            if index % 8 != 0:  # Check if not on the left edge
                if index + 7 < 64 and board[index + 7] == -1:
                    piece_value -= 0.1   
                    

            if (index + 1) % 8 != 0:  # Check if not on the right edge
                if index + 9 < 64 and board[index + 9] == -1:
                    piece_value -= 0.1

        # white king
        if piece_value==10:
           if isKingChecked(board, index):
                piece_value-=1
        elif piece_value==-10:  # black king
            if isKingChecked(board, index):
                piece_value+=1

        # we need to do this because we cant work with int because it is easier to evaluate some piece with
        # decimals based on their position on the board
        x = round(x, 1) + piece_value

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

print(evaluate(initialBoard, False))
