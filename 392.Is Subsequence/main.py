from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque([char for char in s])
        pointer = 0
        while pointer < len(t):
            if t[pointer] == q[0]:
                q.popleft()
            pointer +=1
            if not q:
                return True
        if q:
            return False
        else:
            return True

print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))