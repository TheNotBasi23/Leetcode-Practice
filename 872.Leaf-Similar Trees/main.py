# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:




        def genLeaves(root: Optional[TreeNode],arr):
            if root.left is None and root.right is None:
                arr.append(root.val)
            else:
                if root.left is not None:
                    genLeaves(root.left,arr)
                if root.right is not None:
                    genLeaves(root.right,arr)
                return



        leavesForOne = []
        leavesForTwo = []
        genLeaves(root1,leavesForOne)
        genLeaves(root2,leavesForTwo)

        if len(leavesForOne) != len(leavesForTwo):
            return False

        for l,r in zip(leavesForOne,leavesForTwo):
            if l != r:
                return False
        return True
