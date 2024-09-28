class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unit = {}
        cols = {}

        def hash(i: int, j: int) -> int:
            row, col = 0, 1
            while j >= 3:
                j -= 3
                col += 1
            while i >= 3:
                i -= 3
                row += 1
            return row * 3 + col

        # print(hash(0, 0))  # 1
        # print(hash(4, 4))  # 5
        for i, row in enumerate(board):
            map = {}
            for j, cell in enumerate(row):
                if cell == ".":
                    continue
                # check that col is vaild
                if j in cols:
                    if cell in cols[j]:
                        return False
                    else:
                        cols[j].append(cell)
                else:
                    cols[j] = [cell]
                # check that row is vaild
                if cell in map:
                    print("in map", map)
                    return False
                else:
                    map[cell] = j
                # check unit is valid
                key = hash(i, j)
                if key in unit:
                    if cell in unit[key]:
                        print("in unit", unit)
                        return False
                    else:
                        unit[key].append(cell)
                else:
                    unit[key] = [cell]
        return True
