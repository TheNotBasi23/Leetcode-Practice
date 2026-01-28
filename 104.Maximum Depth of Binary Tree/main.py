class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(level,curr):

            if not curr.left and not curr.right:
                return level
            else:
                leftPath = level
                rightPath = level
                if curr.left:
                    leftPath = depth(level + 1, curr.left)
                if curr.right:
                    rightPath = depth(level + 1,curr.right)
                return max(leftPath,rightPath)
