# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxpath = 0
        def subpath(node):
            nonlocal maxpath
            if not node:
                return 0
            l = subpath(node.left)
            r = subpath(node.right)
            if l + r > maxpath:
                maxpath = l + r
            m = max(l, r)
            return m + 1
        subpath(root)
        return maxpath
            