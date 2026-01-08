def solve_8queens():
    board = [-1] * 8

    def safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == row - r:
                return False
        return True

    def place(row):
        if row == 8:
            matrix = []
            for r in range(8):
                row_list = [0] * 8
                row_list[board[r]] = 1
                matrix.append(row_list)
            print(matrix)
            return True   # stop after one solution

        for col in range(8):
            if safe(row, col):
                board[row] = col
                if place(row + 1):
                    return True
        return False

    place(0)

solve_8queens()
