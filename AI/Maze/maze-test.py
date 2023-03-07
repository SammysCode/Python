# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:46:35 2022

@author: Samantha
"""
ANY, UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3, 4

Allowed_Moves_for_Direction = {ANY: [(-1, 0), (0, 1), (1, 0), (0, -1)],
                               UP: [(-1, 0), (0, 1)],
                               RIGHT: [(0, 1), (1, 0)],
                               DOWN: [(1, 0), (0, -1)],
                               LEFT: [(0, -1), (-1, 0)], }

Direction_map = {(-1, 0): UP,
                 (0, 1): RIGHT,
                 (1, 0): DOWN,
                 (0, -1): LEFT}


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None, direction=ANY):
        self.parent = parent
        self.position = position
        self.direction = direction  # Starting point has no starting direction

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        if self.position == other.position and self.direction == other.direction:
            return True
        elif self.position == other.position and other.direction == ANY:
            return True
        else:
            return False


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node

    # Added the ANY direction for the start node
    start_node = Node(None, start, ANY)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = []
        moves = Allowed_Moves_for_Direction[current_node.direction]
        for new_position in moves:  # Adjacent squares

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) - 1) or node_position[1] < 0:
                continue

            # # MAKE SURE IT DOESNT TURN LEFT
            # if (new_position[0] == 0 and new_position[1] == 1) or (new_position[0] == 0 and new_position[1] == -1) or (new_position[0] == -1 and new_position[1] == 0) or (new_position[0] == 1 and new_position[1] == 0):
            #     continue
            # print("This is the new_position index 0: " +
            #       str(new_position[0]) + "\n This is the new_position index 1: " + str(new_position[1]))

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position,
                            Direction_map[new_position])

            # Append
            children.append(new_node)

        for child in children:

            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([open_node for open_node in open_list if child == open_node and child.f > open_node.f]) > 0:
                continue

            open_list.append(child)


def main():
    #        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],  # 1
            [0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0],  # 2
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],  # 4
            [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 6
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0],  # 7
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 8
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],  # 9
            [1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],  # 10
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]]  # 12

    start = (12, 9)
    end = (12, 2)

    #        0, 1, 2, 3, 4, 5, 6,
    maze1 = [[0, 0, 0, 0, 0, 0, 0],  # 0
             [0, 1, 0, 1, 0, 1, 0],  # 1
             [0, 0, 0, 0, 0, 0, 0],  # 2
             [1, 1, 0, 1, 0, 1, 1],  # 3
             [1, 1, 0, 1, 0, 1, 1],  # 4
             [1, 1, 0, 1, 0, 1, 1],  # 5
             [1, 1, 0, 1, 0, 1, 1]]  # 6

    start1 = (6, 4)
    end1 = (6, 2)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
