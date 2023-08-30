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
                        s = board[i][x]
                        if s != '.':
                            col_set.add(s)
                            col_count += 1
                    if len(col_set) < col_count:
                        return False

                # do if top-left of sub_box
                if x % 3 == 0 and y % 3 == 0:
                    box_set = set()
                    box_count = 0
                    for i in range(3):
                        for j in range(3):
                            s = board[x + i][y + j]
                            if s != '.':
                                box_set.add(s)
                                box_count += 1
                    if len(box_set) < box_count:
                        return False

            if len(row_set) < row_count:
                return False

        return True
