from collections import deque
class Solution(object):
    def tribonacci(self, n):
        q = deque([0,1,1])
        counter = 3
        if n < 3:
            return q[n]
        else:
            sum = q[0] + q[1] + q[2]
            while counter <= n:
                q.append(sum)
                sum += sum
                sum -= q.popleft()
                counter += 1
            return q[2]
print(Solution().tribonacci(25))
