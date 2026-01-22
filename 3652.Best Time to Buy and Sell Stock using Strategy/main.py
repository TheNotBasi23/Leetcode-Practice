class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        initialProfits = 0
        for p,s in zip(prices,strategy):
            initialProfits += p * s
        alteringProfits = initialProfits
        leftPointer = 0
        rightPointer = k - 1
        for i in range(k//2):
            if strategy[i] == -1:
                alteringProfits += prices[i]
            elif strategy[i] == 1:
                alteringProfits -= prices[i]

        for i in range(k//2,k):
            if strategy[i] == 0:
                alteringProfits += prices[i]
            elif strategy[i] == -1:
                alteringProfits +=2 * prices[i]
        maxProfit = max(alteringProfits,initialProfits)

        n = len(prices)
        while rightPointer != n-1:
            rightPointer +=1
            if strategy[rightPointer] != 1:
                if strategy[rightPointer] == 0:
                    alteringProfits += prices[rightPointer]
                elif strategy[rightPointer] == -1:
                    alteringProfits += 2 * prices[rightPointer]


            if strategy[leftPointer] != 0:
                if strategy[leftPointer] == -1:
                    alteringProfits -= prices[leftPointer]
                elif strategy[leftPointer] == 1:
                    alteringProfits += prices[leftPointer]
            leftPointer +=1

            mid = leftPointer - 1 + k // 2
            alteringProfits -= prices[mid]
            maxProfit = max(alteringProfits,maxProfit)
        return maxProfit
temp = Solution()
print(temp.maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2))






