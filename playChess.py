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
-add ability to castle;
-add ability to ENPASSANT;
"""
from printBoard import *
from evaluate import *

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

def is_king_in_check_after_move(chessBoard, start, end):
    temp_board = chessBoard.copy()
    movePiece(temp_board, notation[start], notation[end])

    return isKingChecked(temp_board, end)


def movePiece(chessBoard, start, end):
    

    # we use this to get the array index from the notation (e4 =>> 36)
    start = list(notation.keys())[list(notation.values()).index(start)]
    end = list(notation.keys())[list(notation.values()).index(end)]

    row, col = divmod(end, 8)

    # we put the value(the piece) of the start in the square we have chosen
    chessBoard[end] = chessBoard[start]

    if chessBoard[end] == 1 or chessBoard[end] == -1 and row == 1 or row ==8: #promotion
        if chessBoard[end] == 1:
            chessBoard[end]=9
        else:
            chessBoard[end]=-9
    # and then we put an empty square where we started
    chessBoard[start] = 0


def bestMove(chessBoard):
    best_score = float('+inf')  
    best_move = None
    king_index=chessBoard.index(-10)    #its useful to save the black king index


    #if the black king is not in check we just want the best move
    for i in range(len(chessBoard)):

        if chessBoard[i] < 0:  # Check for black pieces
            piece_moves = possibleMoves(chessBoard, i)

            for move in piece_moves:
                temp_board_black = chessBoard.copy()
                movePiece(temp_board_black, notation[i], notation[move])
                #check if after moving that piece the black king is in check
                if isKingChecked(temp_board_black, temp_board_black.index(-10)):
                    continue    #we skip this move because the black king is in check 
                                
                # Simulate best white response
                best_white_score = float('-inf')

                for j in range(len(temp_board_black)):
                    if temp_board_black[j] > 0:  # Check for white pieces
                        white_piece_moves = possibleMoves(temp_board_black, j)
                        for white_move in white_piece_moves:        
                            #need to add a control on checks also for white
                            temp_board_white = temp_board_black.copy()
                            movePiece(temp_board_white, notation[j], notation[white_move])
                            try:
                                if isKingChecked(temp_board_white, temp_board_black.index(10)):
                                    continue    #we skip this move because the white king is in check 
                            except:
                                print("how did we get here?")        
                            white_score = evaluate(temp_board_white, True)

                            if white_score > best_white_score:
                                best_white_score = white_score

                # Evaluate the score for the current black move
                score = evaluate(temp_board_black, False) + best_white_score

                if score < best_score:
                    best_score = score
                    best_move = (notation[i], notation[move])

    if best_move==None: 
        print("game is lost for black, checkmate")
    return best_move

while True:
    # we will change the board during the execution but we'll use the same array to save memory
    printBoard(initialBoard)

    gameEnd=False   #variaviable to stop the game
    while True:
        
        try:    #we do it in a try-except because the user might type a wrong move
            # variables that store the position of a piece
            selected = input("\nSelect the square of a piece you are willing to move (only legal moves)(type 'stop' to end the game) ").lower()
            
            if selected=="stop": 
                gameEnd=True
                break #so the user can stop playing
                
            print("you can move to : " )
            mvs=possibleMoves(initialBoard, list(notation.keys())[list(notation.values()).index(selected)]) #list of possible moves for given piece location
            for y in mvs:
                print(notation[y], " " )

            moveTo = input("Enter where you want your piece to be placed ").lower()
            if list(notation.keys())[list(notation.values()).index(moveTo)]  in mvs:
        
                break    #if the user selected a valid move, we can end the loop
        except: #if the move is invalid we can just loop again 
            print("Invalid Move")
        
    if gameEnd: break    
     
    if is_king_in_check_after_move(initialBoard, list(notation.keys())[list(notation.values()).index(selected)], list(notation.keys())[list(notation.values()).index(moveTo)]): 
                    print("you just tried to run into a check, so you LOST")
                    break
    else:
        print("amogus")  
    
        
    movePiece(initialBoard, selected, moveTo)
    print("Now we have an evaluation of ", evaluate(initialBoard, True))

    # Black move
    best_move = bestMove(initialBoard)
    if best_move:
        print("Best move for Black:", best_move)
        movePiece(initialBoard, best_move[0], best_move[1])
        print("After black's move the evaluation is ", evaluate(initialBoard, False))
    else:
        print("No legal moves for Black. Game over.")
        break  # or add an appropriate exit condition
