
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        queens = []    # column chosen for each row

        def backtrack(row):
            if row == n:
                board = []
                for c in queens:
                    board_row = ['.'] * n
                    board_row[c] = 'Q'
                    board.append(''.join(board_row))
                result.append(board)
                return

            for col in range(n):
                if (col in cols or
                    row - col in diag1 or
                    row + col in diag2):
                    continue

                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                queens.append(col)

                backtrack(row + 1)

                # Backtrack
                queens.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result
