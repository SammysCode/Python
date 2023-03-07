import random
import game
import sys
import numpy as np
from itertools import cycle

from heuristicai_v1 import bestmove

# Samantha Bergdahl
'''
Combine the smallest tiles. First make the move random and then try with the moves to combine it LEFT (if its not possible to go left continue with the next),
UP (if it worked go back to LEFT, if not continue with next step), DOWN (-||-), RIGHT
'''

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def find_best_move(board):
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    move = 0
    newboard = execute_move(move, board)

    if find_min_pair(board) == "horisontal":
        move = 2  # L
        if board_equals(board, newboard) == True:
            move = 3  # R
    elif find_min_pair(board) == "vertical":
        move = 0  # U
        if board_equals(board, newboard) == True:
            move = 1  # D
    elif find_min_pair(board) == "no merge":

        moves = [2, 0, 1, 3]

        for m in moves:
            move = m
            newboard = execute_move(move, board)
            if board_equals(board, newboard) == False:
                return move
    else:
        print("Something is wrong")

    return move


def find_min_pair(board):
    """
        Get the position of all tiles which which has next to them a tile
        with the same value. A pair of tiles with same value only one of the
        tile is in the list.
        And no tile is in the list twice.
    """

    low_horisontal = []
    low_vertical = []
    print(board)
    for y in range(4):
        for x in range(4):
            if board[y][x] == 0:
                continue
            if x < 3:
                if board[y][x] == board[y][x+1]:
                    min_pair = board[y][x]
                    direction = "Horisontal"
                    low_horisontal.append(min_pair)
                    print(min_pair, direction)
                    continue
            if y < 3:
                if board[y][x] == board[y+1][x]:
                    min_pair = board[y][x]
                    direction = "Vertical"
                    low_vertical.append(min_pair)
                    print(min_pair, direction)

    # If there isn't vertical merges but horisontal
    if len(low_vertical) == 0 and len(low_horisontal) != 0:
        print("No possible merges vertical")
        low_horisontal = min(low_horisontal)
        print("H:", low_horisontal)
        return "horisontal"

    # If theres isn't horisontal but vertical merges
    elif len(low_horisontal) == 0 and len(low_vertical) != 0:
        print("No possible merges horisontal")
        low_vertical = min(low_vertical)
        print("V:", low_vertical)
        return "vertical"

    # If no merges possible
    elif len(low_vertical) == 0 and len(low_horisontal) == 0:
        print("No possible merges")
        return "no merge"

    # If theres both vertical and horisontal merges
    elif len(low_vertical) > 0 and len(low_horisontal) > 0:
        # setting the lowest tile
        low_horisontal = min(low_horisontal)
        low_vertical = min(low_vertical)
        print("V:", low_vertical)
        print("H:", low_horisontal)

        # When vertical had the lower tile
        if low_horisontal > low_vertical:
            print("Lowest tiles mergable is vertical:", low_vertical)
            return "vertical"

        # When Horisontal had the lower tile
        else:
            print("Lowest tiles mergable is hotisontal:", low_horisontal)
            return "horisontal"
    else:
        print("Something went wrong when finding the merging possibilities")


def get_empty_positions(board):
    '''
        Get all empty positions on the board.
    '''
    empty_positions = []
    for y in range(4):
        for x in range(4):
            if board[y][x] == 0:
                empty_positions.append((y, x))
    return empty_positions


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
    return (newboard == board).all()
