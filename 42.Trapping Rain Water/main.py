class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        nextGreatest = [-1 for char in height]
        mono = []
        for i in range(n - 1,-1,-1):
            while mono and height[i] > height[mono[-1]]:
                mono.pop()

            nextGreatest[i] = mono[-1] if mono else -1
            mono.append(i)
        beforeGreatest = [-1 for char in height]
        mono = []
        for i in range(n):
            while mono and height[i] > height[mono[-1]]:
                mono.pop()

            beforeGreatest[i] = mono[-1] if mono else -1
            mono.append(i)
        count = 0
        for i in range(n):
            print(f"bettween { height[beforeGreatest[i]] if beforeGreatest[i] != -1 else -1} and { height[nextGreatest[i]] if nextGreatest[i] != -1 else -1} ")
            minVal = min(height[beforeGreatest[i]] if beforeGreatest[i] != -1 else -1,height[nextGreatest[i]] if nextGreatest[i] != -1 else -1)
            curr = height[i]
            count += (minVal - curr) if minVal > curr else 0
            print("added ",(minVal - curr) if minVal > curr else 0)
        print(count)


Solution().trap(height = [4,2,0,3,2,5])