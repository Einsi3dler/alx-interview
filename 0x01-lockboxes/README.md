# Lockboxes Solution

This directory contains a Python solution to the Lockboxes problem. The solution is contained in the file `0-lockboxes.py`.

## Problem Description

In the Lockboxes problem, you are given `n` lockboxes represented as an array of lists. Each list contains keys to other lockboxes. The goal is to determine if all the lockboxes can be opened.

## Solution

The solution in `0-lockboxes.py` uses a depth-first search (DFS) algorithm to traverse the lockboxes. It starts with the first lockbox (lockbox 0) and uses the keys in each lockbox to open other lockboxes. If all lockboxes can be opened, the function returns `True`; otherwise, it returns `False`.