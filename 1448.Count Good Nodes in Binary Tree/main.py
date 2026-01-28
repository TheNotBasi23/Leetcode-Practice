# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(root:TreeNode,maxSoFar):

            value = root.val
            valid = 0 if value < maxSoFar else 1
            maxSoFar = max(maxSoFar,value)

            return valid + (DFS(root.left,maxSoFar) if root.left is not None else 0)  + (DFS(root.right,maxSoFar)if root.right is not None else 0)

        return DFS(root,root.val)
