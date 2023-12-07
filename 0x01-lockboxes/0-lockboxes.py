#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    Returns True if all boxes can be opened, or False if otherwise
    """
    # Create a set to keep track of keys
    keys = set([0])

    # Iterate through keys until no more boxes can be opened
    while True:
        # Store the current set of keys
        current_keys = set(keys)

        # Iterate through the boxes
        for i, box in enumerate(boxes):
            if i in keys:
                # Add all keys in the current box to the set
                keys.update(box)

        # Break the loop if no new keys were added in the last iteration
        if keys == current_keys:
            break

    # Check if all boxes can be opened
    return all(i in keys for i in range(len(boxes)))
