class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        stack = []
        for point in points:
            if not stack :
                stack.append(point)
            else:
                topValue = stack.pop()
                if topValue[0] <= point[0] <= topValue[1]:
                    stack.append((max(topValue[0],point[0]), min(topValue[1],point[1])))
                else:
                    stack.append(topValue)
                    stack.append(point)
        return (len(stack))

Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]])
