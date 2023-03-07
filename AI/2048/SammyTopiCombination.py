import random

from numpy import broadcast_arrays

import game
import sys
import Expectimax_functions_show as e
# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def find_best_move(board):
    """
	Combination of Samanthas and Topis heuristic code
        """
    VerticalFavorUp = 0
    VerticalFavorDown = 0    
    HorizontalFavorLeft = 0
    HorizontalFavorRight = 0
    for y in range(4):
        for x in range(4):
            if board[y][x] == 0:
                continue
            if x < 3:
                # If board can merge horizontally well with tiles on the Left
                if board[y][x] == board[y][x+1]:
                    HorizontalFavorLeft=HorizontalFavorLeft+1
            if x > 3:
                # If board can merge horizontally well with tiles on the Right
                if board[y][x] == board[y][x-1]:
                    HorizontalFavorRight=HorizontalFavorRight+1
            if y < 3:
                # If board can merge vertically well with tiles Up.
                if board[y][x] == board[y+1][x]:
                    VerticalFavorDown=VerticalFavorDown+1
            if y > 3:
                # If board can merge vertically well with tiles Down.
                if board[y][x] == board[y-1][x]:
                    VerticalFavorUp=VerticalFavorUp+1

    var = [VerticalFavorUp, VerticalFavorDown,HorizontalFavorLeft, HorizontalFavorRight]
    #UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        # bestmove = random.choice([UP,DOWN,LEFT,RIGHT])
    bestmove = 2
    newboard = execute_move(bestmove,board)

    if VerticalFavorDown == 0 and VerticalFavorUp == 0 and HorizontalFavorLeft == 0 and HorizontalFavorRight == 0:
        bestmove=0
        moves = [2, 0, 1, 3]

        for m in moves:
            move = m
            newboard = execute_move(move, board)
            if board_equals(board, newboard) == False:
                return move                
    else:
        max_value=var.index(max(var))
        bestmove = int(max_value)

    return bestmove

    
def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")
		

def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  

