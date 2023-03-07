# import random
# import game
# import sys

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

import random
import numpy as np
import sys
import time
from itertools import product
import matplotlib.pyplot as plt

ROW_LENGTH = 4
STARTING_NUMBERS = 2
CHANCE_OF_TWO = 90
PLAYER_SCORE = 0
TOTAL_MOVES = 0
NUMBER_OF_RUNS = 7

POSSIBLE_MOVES = ["up", "right", "down", "left"]
DEPTH = 2
POSSIBLE_ARRANGEMENTS = product(POSSIBLE_MOVES, repeat=DEPTH)
TEMPLATE = [[0.135, 0.121, 0.102, 0.0999],
            [0.0997, 0.088, 0.076, 0.0724],
            [0.0606, 0.0562, 0.0371, 0.0161],
            [0.0125, 0.0099, 0.0057, 0.0033]]

BEST_DIRECTION = ""
BEST_SCORE = 0
BEST_GRID = None
PLT_SCORE = [[], [], [], []]


def generateTile():
    RANDOM_NUM = random.randint(1, 100)
    if RANDOM_NUM < CHANCE_OF_TWO:
        number = 2
    else:
        number = 4
    return number


def createGrid(dimensions):
    grid = [[0 for i in range(dimensions)] for j in range(dimensions)]
    for i in range(STARTING_NUMBERS):
        number = generateTile()
        grid[random.randint(0, ROW_LENGTH - 1)
             ][random.randint(0, ROW_LENGTH - 1)] = number
    displayGrid(grid)
    return grid


def displayGrid(*grids):
    for grid in grids:
        print(np.array(grid))


def evalgrid(grid):
    return np.sum(np.array(grid) * TEMPLATE)


def move(direction, grid, score):
    if direction == "left" or direction == "right":
        for i in range(ROW_LENGTH):
            if direction == "right":
                grid[i] = grid[i][::-1]
            for j in range(grid[i].count(0)):
                grid[i].append(grid[i].pop(grid[i].index(0)))

            for element in range(0, ROW_LENGTH - 1):
                if grid[i][element] == grid[i][element + 1]:
                    score += grid[i][element] * 2
                    grid[i][element] = grid[i][element] * 2
                    grid[i].remove(grid[i][element + 1])
                    grid[i].append(0)
            if direction == "right":
                grid[i] = grid[i][::-1]

        return grid, score

    else:
        collection = [grid[j][i]
                      for i in range(0, ROW_LENGTH) for j in range(0, ROW_LENGTH)]
        vGrid = [collection[i * ROW_LENGTH:((i + 1) * ROW_LENGTH)]
                 for i in range(ROW_LENGTH)]

        for i in range(ROW_LENGTH):
            if direction == "down":
                vGrid[i] = vGrid[i][::-1]
            for j in range(vGrid[i].count(0)):
                vGrid[i].append(vGrid[i].pop(vGrid[i].index(0)))
            for element in range(0, ROW_LENGTH - 1):
                if vGrid[i][element] == vGrid[i][element + 1]:
                    score += grid[i][element] * 2
                    vGrid[i][element] = vGrid[i][element] * 2
                    vGrid[i].remove(vGrid[i][element + 1])
                    vGrid[i].append(0)
            if direction == "down":
                vGrid[i] = vGrid[i][::-1]

        for row in range(ROW_LENGTH):
            for column in range(ROW_LENGTH):
                grid[row][column] = vGrid[column][row]

        return grid, score


def check(grid):
    gridArr = []

    for direction in POSSIBLE_MOVES:
        temp = [x[:] for x in grid]
        gridArr.append(move(direction, temp, PLAYER_SCORE))

    for potentialGrid in gridArr:
        if grid != potentialGrid[0]:
            return False
    return True


def updateGrid(grid, state):
    count = 0
    for i in range(ROW_LENGTH):
        count += grid[i].count(0)

    if not count:
        if check(grid):
            return grid, True

    if state == True:
        while True:
            row = random.randint(0, ROW_LENGTH - 1)
            column = random.randint(0, ROW_LENGTH - 1)
            if grid[row][column] == 0:
                grid[row][column] = generateTile()
                return grid, False
    return grid, False


def bestmove(grid, CURR_DEPTH, SET_OF_MOVES, currentscore):
    CURR_DEPTH += 1
    placeholder = [x[:] for x in grid]
    if CURR_DEPTH != DEPTH:
        for DIRECTION in POSSIBLE_MOVES:
            grid = move(DIRECTION, grid, currentscore)[0]
            SET_OF_MOVES.append(DIRECTION)
            # print(f"Depth {CURR_DEPTH}")
            # displayGrid(grid)
            if grid != placeholder:
                grid = updateGrid(grid, True)[0]
                bestmove(grid, CURR_DEPTH, SET_OF_MOVES, currentscore)

            SET_OF_MOVES.pop()
            grid = [x[:] for x in placeholder]
        return

    else:
        global BEST_SCORE
        global BEST_DIRECTION
        global BEST_GRID
        SCORE = evalgrid(grid)
        if BEST_SCORE < SCORE:
            BEST_SCORE = SCORE
            BEST_DIRECTION = SET_OF_MOVES[0]
            BEST_GRID = grid

        return
    return

# UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

# def find_best_move(board):
#     bestmove = -1

# 	# TODO:
# 	# Build a heuristic agent on your own that is much better than the random agent.
# 	# Your own agent don't have to beat the game.
#     bestmove = find_best_move_random_agent()
#     return bestmove

# def find_best_move_random_agent():
#     return random.choice([UP,DOWN,LEFT,RIGHT])

# def execute_move(move, board):
#     """
#     move and return the grid without a new random tile
# 	It won't affect the state of the game in the browser.
#     """

#     if move == UP:
#         return game.merge_up(board)
#     elif move == DOWN:
#         return game.merge_down(board)
#     elif move == LEFT:
#         return game.merge_left(board)
#     elif move == RIGHT:
#         return game.merge_right(board)
#     else:
#         sys.exit("No valid move")

# def board_equals(board, newboard):
#     """
#     Check if two boards are equal
#     """
#     return  (newboard == board).all()
