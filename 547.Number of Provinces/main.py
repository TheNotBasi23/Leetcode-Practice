from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = {}
        count = 0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            else:
                count +=1
                q = deque()
                q.append(i)
                visited[i] = True
                while q:
                    item = q.popleft()
                    nextItems = [j for j in range(len(isConnected[item])) if j not in visited and isConnected[item][j] == 1]
                    for element in nextItems:
                        visited[element] = True
                        q.append(element)
        return count


print(Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))

