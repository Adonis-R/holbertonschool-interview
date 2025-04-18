#!/usr/bin/python3
"""Module to check if all lockboxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (list of list of int): Each box may contain keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or not boxes:
        return False

    visited = set()
    to_visit = [0]

    while to_visit:
        box = to_visit.pop()
        if box not in visited:
            visited.add(box)
            for key in boxes[box]:
                if isinstance(key, int) and 0 <= key < len(boxes):
                    to_visit.append(key)

    return len(visited) == len(boxes)
