#!/usr/bin/python3
"""
Module for determining if all locked boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all locked boxes in a list of lists can be opened.

    Args:
        boxes (list of list of int): A list where each element is a list
            containing keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = {0}
    # Initialize the queue/stack with the keys found in the first box
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        # Verify the key corresponds to a valid box and hasn't been opened yet
        if 0 <= key < n and key not in opened:
            opened.add(key)
            # Add newly discovered keys to our search list
            keys.extend(boxes[key])

    # Check if the number of opened unique boxes matches the total box count
    return len(opened) == n
