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
-add ability to move;
-add ability to castle;
-add ability to ENPASSANT;
-add ability to promote.
-add a control to end the game
"""
from print_board import *

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
def movePiece(start, end):
    start=list(notation.keys())[list(notation.values()).index(start)]   #we use this to get the array index from the notation (e4 =>> 36)
    end=list(notation.keys())[list(notation.values()).index(end)]
    initialBoard[end]=initialBoard[start]   #we put the value(the piece) of the start in the square we have chosen
    initialBoard[start]=0   # and then we put an empty square where we started
    

while True:

    printBoard(initialBoard)    #we will change the board during the execution but we'll use the same array to save memory
    
    selected=input("\nSelect the square of a piece you are willing to move (only legal moves) ")  #variables that stores the position of a piece
    moveTo=input("Enter where you want your piece to be placed ")
    movePiece(selected, moveTo)
    #add condition on endind the loop upon winning/losing/ making a tie
