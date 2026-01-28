from collections import deque
class RecentCounter:
    q = None
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        newItem = t
        self.q.append(newItem)
        while self.q and self.q[0] < newItem - 3000:
            self.q.popleft()
        return len(self.q)
