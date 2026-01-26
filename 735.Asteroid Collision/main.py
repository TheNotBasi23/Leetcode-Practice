class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            if not stack:
                stack.append(aster)
            else:
                if stack[-1] > 0 and aster < 0:

                    while stack and stack[-1] < -aster and stack[-1] > 0:
                        stack.pop()
                    if not stack:
                        stack.append(aster)
                    else:
                        if stack[-1] == -aster:
                            stack.pop()
                        elif stack[-1] < 0:
                            stack.append(aster)
                else:
                    stack.append(aster)

        return stack
