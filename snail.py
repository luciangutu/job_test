def snail(snail_map):
    result = []
    row = len(snail_map) - 1
    col = len(snail_map[0]) - 1
    rowpos = colpos = 0

    while rowpos <= row and colpos <= col:
        for i in range(colpos, col + 1):
            result.append(snail_map[rowpos][i])
        rowpos += 1

        for i in range(rowpos, row + 1):
            result.append(snail_map[i][col])
        col -= 1

        if rowpos <= row:
            for i in range(col, colpos-1, -1):
                result.append(snail_map[row][i])
        row -= 1

        if colpos <= col:
            for i in range(row, rowpos-1, -1):
                result.append(snail_map[i][colpos])
        colpos += 1

    return result







array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array), expected)


array = [[1,2,3, 1],
         [4,5,6, 4],
         [7,8,9, 7],
         [7, 8, 9, 7]]
expected = [1,2,3,1,4,7,7,9,8,7,7,4,5,6,9,8]
print(snail(array), expected)

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array), expected)
