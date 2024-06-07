#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n: int) -> int:
    """Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(n, int):
        return 0
    ops = 0
    clip = 0
    done = 1
    while done < n:
        if clip == 0:
            # First copy and paste
            clip = done
            done += clip
            ops += 2
        elif (n - done) % done == 0:
            # Copy and paste
            clip = done
            done += clip
            ops += 2
        else:
            # Paste
            done += clip
            ops += 1
    return ops
