# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if not subRoot:
            return True

        if self.sameTree(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()
            if not node_p and not node_q:
                continue
            
            if not node_p or not node_q or node_p.val != node_q.val:
                return False
            
            stack.append((node_p.right, node_q.right))
            stack.append((node_p.left, node_q.left))

        return True