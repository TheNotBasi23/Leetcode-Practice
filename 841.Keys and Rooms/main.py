from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        setOfAllRooms = set([i for i in range(n)])
        q = deque()
        q.append(0)
        visitedRooms = {}
        visitedRooms[0] = True

        while q:
            item = q.popleft()
            setOfAllRooms.remove(item)
            for element in rooms[item]:
                if element not in visitedRooms:
                    q.append(element)
                    visitedRooms[element] = True
        if setOfAllRooms:
            return False
        else:
            return True