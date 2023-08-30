class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y, row in enumerate(board):
            row_set = set()
            row_count = 0
            for x, num in enumerate(row):
                # start row check
                if num != '.':
                    row_set.add(num)
                    row_count += 1

                # check columns starting from y = 0
                if not y:
                    col_set = set()
                    col_count = 0
                    for i in range(9):
                        if board[i][x] != '.':
                            col_set.add(board[i][x])
                            col_count += 1
                    if len(col_set) < col_count:
                        return False

                # do if top-left of sub_box
                if x % 3 == 0 and y % 3 == 0:
                    sub_box = [num, row[x + 1], row[x + 2], board[y + 1][x], board[y + 1][x + 1], board[y + 1][x + 2], board[y + 2][x], board[y + 2][x + 1], board[y + 2][x + 2]]

                    box_set = set()
                    box_count = 0
                    for s in sub_box:
                        if s != '.':
                            box_set.add(s)
                            box_count += 1
                    if len(box_set) < box_count:
                        return False

            if len(row_set) < row_count:
                return False

        return True
