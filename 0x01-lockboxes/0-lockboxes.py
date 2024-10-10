#!/usr/bin/python3

def canUnlockAll(boxes):
    # The number of boxes
    n = len(boxes)

    # A set to keep track of opened boxes
    opened = set([0])  # Start with box 0 as it's already unlocked

    # Stack to manage keys, initialized with keys in box 0
    keys = boxes[0].copy()

    # Loop while we have keys to check
    while keys:
        key = keys.pop()  # Take a key from the stack

        # Only unlock the box if the key corresponds to a valid box
        # and the box hasn't been unlocked yet
        if key < n and key not in opened:
            opened.add(key)  # Open the box

            # Add all the keys from the newly opened box
            keys.extend(boxes[key])

    # Check if we've unlocked all boxes
    return len(opened) == n
