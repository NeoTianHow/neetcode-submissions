class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate through every cell and store the corresponding
        # row, column, and 3×3 grid. If any key exists, the board
        # contains a duplicate.
        seen = set()

        for rowIdx in range(len(board)):
            for colIdx in range(len(board[rowIdx])):
                value = board[rowIdx][colIdx]

                if value == ".":
                    continue

                rowKey = (rowIdx, "r", value)
                colKey = (colIdx, "c", value)
                gridKey = (rowIdx // 3 * 3 + colIdx // 3, "g", value)

                if rowKey in seen or colKey in seen or gridKey in seen:
                    return False

                seen.add(rowKey)
                seen.add(colKey)
                seen.add(gridKey)

        return True

        # Pattern: Set
        # Time: O(n²)
        # Space: O(n²)