import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        cleaned = re.sub(r'\s+', ' ', s)
        arr = cleaned.split(" ")
        arr.reverse()
        n = len(arr) - 1
        final = []
        for i, char in enumerate(arr):
            final.append(char)
            if i != n:

                final.append(" ")
        finalStr = "".join(final)
        return (finalStr)

Solution().reverseWords("  hello world  ")