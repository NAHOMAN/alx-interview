#!/usr/bin/python3
"""Module to determine if a list of boxes contain keys to other boxes"""


def canUnlockAll(boxes):
    """Function to determine keys from list of boxes"""

    for key in range(1, len(boxes) - 1):
        visited = False
        for box_index in range(len(boxes)):
            visited = key in boxes[box_index] and key != box_index
            if visited:
                break
        if visited is False:
            return visited
    return True
