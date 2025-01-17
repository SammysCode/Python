# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 23:20:16 2021

@author: tommi
"""
import random
import game
import sys

from itertools import chain

import Expectimax_functions_show as e

# Author:      chrn (original by nneonneo)
# Date:        11.11.2016
# Copyright:   Algorithm from https://github.com/nneonneo/2048-ai
# Description: The logic to beat the game. Based on expectimax algorithm.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3


def find_best_move(board):
    """
    find the best move for the next turn.
    """
    bestmove = -1
    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
    move_args = [UP, DOWN, LEFT, RIGHT]

    result = [score_toplevel_move(i, board) for i in range(len(move_args))]
    print("result", result)
    bestmove = result.index(max(result))

    for m in move_args:
        print("move: %d score: %.4f" % (m, result[m]))

    return bestmove


def score_toplevel_move(move, board):
    """
    Entry Point to score the first move.
    """
    newboard = execute_move(move, board)
    if board_equals(newboard, board):
        return 0

    return e.calculate_chance(newboard, 0, 3)


def execute_move(move, board):
    """
    move and return the grid without a new random tile 
    It won't affect the state of the game in the browser.
    """

    UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

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
