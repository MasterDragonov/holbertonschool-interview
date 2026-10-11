def canUnlockAll(boxes):
    n = len(boxes)
    opened = {0}
    keys = list(boxes[0])
    while keys:
        key = keys.pop()
        if 0 <= key < n and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])
    return len(opened) == n
