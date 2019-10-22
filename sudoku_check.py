def done_or_not(board):
    good = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    col_list = []
    small_row_list = []
    row_list = []
    full_count = 0
    for x in range(len(board)):
        for y in range(len(board)):
            #  printing the rows: print(board[x][y])
            #  printing the columns: print(board[y][x])

            # print(board[x][y])
            # print(board[y][x])
            # input("Press Enter to continue...")

            # checking the smaller 3x3 boxes
            for i in range(3):
                for j in range(3):
                    small_row_list.append(board[i][j])
                    if len(small_row_list) == 9:
                        if set(good) != set(sorted(small_row_list)):
                            return "Try again!"
                        else:
                            small_row_list = []

            full_count += 1
            row_list.append(board[x][y])
            col_list.append(board[y][x])
            if full_count == 9:
                full_count = 0
                if (set(good) != set(sorted(col_list))) or (set(good) != set(sorted(row_list))):
                    return "Try again!"
                else:
                    col_list = []
                    row_list = []
    return "Finished!"


print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 5, 3]]))  # 'Finished!');

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                   , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                                   , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                                   , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                                   , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                                   , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                                   , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                                   , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                                   , [8, 7, 9, 6, 4, 2, 1, 3, 5]]))  # 'Try again!');
