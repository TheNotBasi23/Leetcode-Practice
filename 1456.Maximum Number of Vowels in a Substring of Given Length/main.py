class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a":True,"e":True,"i":True,"o":True,"u":True}
        numVowels = 0
        leftPointer = -1
        n = len(s)
        rightPointer = k - 1
        maxVowels = 0
        for i in range(k):
            if s[i] in vowels:
                numVowels +=1
        while rightPointer < n -1:
            rightPointer +=1
            if s[rightPointer] in vowels:
                numVowels +=1
            leftPointer +=1
            if s[leftPointer] in vowels:
                numVowels -= 1
            maxVowels = max(maxVowels,numVowels)
        return maxVowels
print(Solution().maxVowels(s = "aeiou", k = 2))

