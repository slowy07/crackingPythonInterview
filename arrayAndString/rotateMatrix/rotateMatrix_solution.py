def rotateMatrix(matrix):
    # Transpose the Matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Switch the row and column indices
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for r in range(len(matrix)):
        for i in range(len(matrix[r]) // 2):
            # oppI is the opposing index to i
            oppI = len(matrix[r]) - 1 - i
            matrix[r][i], matrix[r][oppI] = matrix[r][oppI], matrix[r][i]
