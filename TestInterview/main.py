import heapq
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        arr = [-num for num in nums]
        heapq.heapify(arr)
        heapq.heapify(nums)
        largestPositive = -heapq.heappop(arr)
        largestPositiveDoubleProduct = -heapq.heappop(arr) * -heapq.heappop(arr)
        largestNegativeDoubleProduct = heapq.heappop(nums) * heapq.heappop(nums)
        return max(largestPositive * largestPositiveDoubleProduct, largestPositive * largestNegativeDoubleProduct)

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        myDict = {}
        for word in words:
            myDict[word] = myDict.get(word, 0) + 1
        arrOfElements = [(myDict[key], key) for key in myDict]
        arrOfElements.sort(key = lambda x:(-x[0], x[1]))
        return [arrOfElements[i][1] for i in range(k)]
print(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 3))