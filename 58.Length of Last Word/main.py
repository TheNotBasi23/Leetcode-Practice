class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                break
            else:
                counter+=1
        return counter
print(Solution().lengthOfLastWord("hello world  "))