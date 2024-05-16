# Minimum Operations to Return to the Main Directory

## Problem Description

In the Leetcode file system, every time a user changes the directory, a log entry is created. These operations are defined as follows:

- `"../"` : Move up to the parent directory of the current folder. If already in the root directory, stay there.
- `"./"` : Remain in the current directory.
- `"x/"` : Move into the child directory named `x` (This directory always exists).

You are provided with a list of strings `logs` where `logs[i]` denotes the operation performed by the user at step `i`. Starting from the main directory, the operations specified in `logs` are executed sequentially.

Your objective is to return the minimum number of operations required to get back to the main directory after executing the given operations.

## Example

### Input
```python
logs = ["d1/", "d2/", "../", "d21/", "./"]
output = 2
```
