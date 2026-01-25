from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        keyValue = image[sr][sc]
        if keyValue == color:
            return image
        n = len(image)
        m = len(image[0])

        initCoord = (sr,sc)
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        q = deque([initCoord])
        while q:
            item = q.popleft()
            image[item[0]][item[1]] = color

            newItems = [
                (item[0] + l , item[1] + r)
                for l,r in directions
                if 0 <= item[0] + l < n and 0 <= item[1] + r < m and image[item[0] + l][item[1] + r] == keyValue
            ]
            for newSpots in newItems:
                q.append(newSpots)


        return image

print(Solution().floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))