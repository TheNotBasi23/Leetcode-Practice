class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack:
                if char != "*":
                    stack.append(char)

            else:
                if char == "*":
                    stack.pop()
                else:
                    stack.append(char)