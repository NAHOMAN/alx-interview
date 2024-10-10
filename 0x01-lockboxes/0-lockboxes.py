#!/usr/bin/python3

def canUnlockAll(boxes):
    # The number of boxes
    n = len(boxes)
    
    # A set to keep track of opened boxes
    opened = set()
    
    # Start by opening the first box (box 0)
    opened.add(0)
    
    # Stack to manage keys, initialized with keys in box 0
    keys = boxes[0].copy()
    
    # Loop while we have keys to check
    while keys:
        key = keys.pop()  # Take a key from the stack
        
        if key < n and key not in opened:
            # Open the box if it hasn't been opened
            opened.add(key)
            
            # Add all keys from the newly opened box to the stack
            keys.extend(boxes[key])
    
    # If we opened all boxes, return True, else return False
    return len(opened) == n
