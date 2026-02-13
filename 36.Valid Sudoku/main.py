class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSquareValidity(board,row,col):
            myDict = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != ".":
                        if board[i][j] in myDict:
                            return False
                        else:
                            myDict.add(board[i][j])
            return True





        for i in range(0,9,3):
            for j in range(0, 9, 3):
                valid = checkSquareValidity(board,i,j)
                if not valid:
                    return False

        for i in range(9):
            myDict = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in myDict:
                        return False
                    else:
                        myDict.add(board[i][j])

        for j in range(9):
            myDict = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in myDict:
                        return False
                    else:
                        myDict.add(board[i][j])
        return True
print(
    Solution().isValidSudoku(
        board=
        [["8", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    )
)


