class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        n = len(temperatures)
        arr = [0] * n
        for i in range(n-1,-1,-1):
            while monoStack and temperatures[monoStack[-1]] <= temperatures[i]:
                monoStack.pop()

            arr[i] = 0 if not monoStack else monoStack[-1] - i
            monoStack.append(i)
        return arr

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
