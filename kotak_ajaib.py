def maxSum(matrix):

    # To find max val in first row
    res = -1
    for i in range(n):
        res = max(res, matrix[0][i])

    for i in range(1, n):

        res = -1
        for j in range(n):

            # When all paths are possible
            if (j > 0 and j < n - 1):
                matrix[i][j] += max(matrix[i - 1][j],
                                 max(matrix[i - 1][j - 1],
                                     matrix[i - 1][j + 1]))

            # When diagonal right is not possible
            elif (j > 0):
                matrix[i][j] += max(matrix[i - 1][j],
                                 matrix[i - 1][j - 1])

            # When diagonal left is not possible
            elif (j < n - 1):
                matrix[i][j] += max(matrix[i - 1][j],
                                 matrix[i - 1][j + 1])

            # Store max path sum
            res = max(matrix[i][j], res)
    return res


if __name__ == "__main__":
    n = 3
    # matrix = ([[6, 7, 4],
    #         [5, 5, 7],
    #         [6, 5, 6]])

    # matrix = ([[ 3, 1, 4],
    #         [ 4, 2, 7],
    #         [ 2, 5, 6]])

    matrix = ([[[] for i in range(3)] for i in range(3)])
    for i in range(3):
        for j in range(3):
            number = int(input("Please input  element of the matrixrix: "))

            if number in range(1,10):
                matrix[i][j] = number
            else:
                number = int(input("Please input  element of the Matrix between 1-9: "))
                matrix[i][j] = number
    print(maxSum(matrix))
