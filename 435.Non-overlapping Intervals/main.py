

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        stack = []
        count = 0
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                if stack[-1][0]<= interval[0] < stack[-1][1] :
                    count +=1
                    if stack[-1][1] < interval[1]:
                        continue
                    else:
                        stack.pop()
                        stack.append(interval)
                        continue

                else:
                    stack.append(interval)
        return count