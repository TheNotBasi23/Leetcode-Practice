class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        stack = []
        for iterval in intervals:
            if not stack:
                stack.append(iterval)
            else:
                itemAtTop = stack.pop(-1)
                if itemAtTop[0] <= iterval[0] <= itemAtTop[1]:
                    newItem = [min(itemAtTop[0], iterval[0]),max(iterval[1], itemAtTop[1])]
                    stack.append(newItem)
                else:
                    stack.append(itemAtTop)
                    stack.append(iterval)
        return stack

