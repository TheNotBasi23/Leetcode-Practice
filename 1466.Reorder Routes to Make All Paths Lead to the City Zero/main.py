from collections import deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        valueSet = set([(i,j) for i,j in connections])
        myDict = {}
        for i,j in connections:
            if i in myDict:
                myDict[i].append(j)
            else:
                myDict[i] = [j]

            if j in myDict:
                myDict[j].append(i)
            else:
                myDict[j] = [i]

        finalArr = []
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        while q:
            item = q.popleft()

            nextItems = [j for j in myDict.get(item,[]) if j not in visited]
            for element in nextItems:
                visited.add(element)
                q.append(element)
                finalArr.append((item,element))

        ans = 0
        for e in finalArr:
            if e in valueSet:
                ans += 1
        return ans

