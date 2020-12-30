# zero matrix

## question
The input is an N x N matrix where some of the items in the matrix are 0. If any of the items are 0, then set that item's entire row and column to 0s. Items that are not 0 will be represented by an integer.
```
Input - [
    [1,2,3,4],
    [5,0,7,8],
    [6,1,1,2],
    [2,3,4,0]
]

Output - [
    [1,0,3,4],
    [5,0,7,8],
    [6,0,1,2],
    [0,0,0,0]
]
```

## solution
Your inital thought might be to iterate through the matrix and set the row and column to 0 whenever you come across a 0. The issue with that, however, is that the original matrix may have multiple zeros. After we encounter the first 0, we'll come across another 0 and we won't know if that 0 was from the original matrix, or if it was created when we were adding 0's to the row and column of the first 0.

An easy way around this is to use two passes. When we encounter a 0 on the first pass, then we'll set the row and the column to None (if we encounter another zero, we will not set that to None, since we'll want to set that item's row and column to None later in the loop).

Then, we can have a second pass where we set all the items with None to 0.

```python
def zeroMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                setNone(matrix, r, c)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == None:
                matrix[r][c] = 0

def setNone(matrix, r, c):
    # set the row to None
    for i in range(len(matrix[r])):
        if matrix[r][i] != 0:
            matrix[r][i] = None

    # set the column to None
    for i in range(len(matrix)):
        if matrix[i][c] != 0:
            matrix[i][c] = None

    matrix[r][c] = None
```
