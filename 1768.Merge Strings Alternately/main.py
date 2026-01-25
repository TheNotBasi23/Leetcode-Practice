from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = deque([char for char in word1])
        str2 = deque([char for char in word2])
        arr = []
        for i in range(max(len(word1),len(word2))):
            if str1:
                arr.append(str1.popleft())
            if str2:
                arr.append(str2.popleft())
        return "".join(arr)


print(Solution().mergeAlternately(word1 = "ab", word2 = "pqrs"))
