class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                integer = ""
                while stack and stack[-1].isnumeric():
                    integer = stack.pop() + integer
                for _ in range(int(integer)):
                    stack.append(substr)
        return "".join(stack)

print(Solution().decodeString(s = "3[a]2[bc]"))
