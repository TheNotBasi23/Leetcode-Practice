from calendar import firstweekday


from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        allLand = set([(i,j) for i in range(len(board)) for j in range(len(board[i])) if board[i][j] == "O"])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows = len(board)
        cols = len(board[0])
        if rows * cols != len(allLand):
            row = col = 0
            direction = "right"
            boundary = {
                "top" : 0,
                "right" : cols - 1,
                "bottom" : rows - 1,
                "left" : 0
            }
            for i in range(cols * 2 + (rows - 2) * 2):
                if (row,col) in allLand:
                    allLand.remove((row,col))
                    q = deque([(row,col)])
                    while q:
                        item = q.popleft()
                        potentialCandidates = [
                            (item[0] + l, item[1] + r) for l,r in directions if (item[0] + l, item[1] + r) in allLand
                        ]
                        for candidate in potentialCandidates:
                            q.append(candidate)
                            allLand.remove(candidate)
                if direction == "right":
                    if col == boundary["right"]:
                        direction = "bottom"
                        row +=1
                    else:
                        col +=1
                elif direction == "bottom":
                    if row == boundary["bottom"]:
                        direction = "left"
                        col -=1
                    else:
                        row +=1
                elif direction == "left":
                    if col == boundary["left"]:
                        direction = "top"
                        row -= 1
                    else:
                        col -= 1
                elif direction == "top":
                    if row == boundary["top"]:
                        direction = "right"
                        col +=1
                    else:
                        row -= 1

            arr = list(allLand)
            for l,r in arr:
                board[l][r] = "X"
Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])