from collections import Counter
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root: TreeNode, ps, count, target):
            if not root:
                return 0
            ps.append(ps[-1] + root.val)

            valid = 0
            if ps[-1] - target in count:
                valid += count[ps[-1] - target]
            count[ps[-1]] = count.get(ps[-1], 0) + 1
            leftValue = 0
            if root.left:
                leftValue += dfs(root.left, ps, count, target)
                count[ps[-1]] -= 1
                ps.pop()
            rightValue = 0
            if root.right:
                rightValue += dfs(root.right, ps, count, target)
                count[ps[-1]] -= 1
                ps.pop()

            return valid + leftValue + rightValue

        return dfs(root, [0], Counter([0]), targetSum)