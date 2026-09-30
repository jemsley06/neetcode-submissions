# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        
        def compare(node1, node2):
            if not node1 or not node2:
                if not node1 and not node2:
                    return True
                else:
                    return False
            left = compare(node1.left, node2.left)
            right = compare(node1.right, node2.right)
            if node1.val != node2.val or not left or not right:
                return False
            else:
                return True
        return compare(p, q)