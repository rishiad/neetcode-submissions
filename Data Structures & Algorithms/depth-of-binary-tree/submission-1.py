# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [[root, 1]]
        visited = set()
        res = 0
        while stack:
            node, depth = stack.pop()
            res = max(res, depth)
            if node not in visited:
                visited.add(node)
                if node.left and node.left not in visited:
                    stack.append([node.left, depth + 1])
                if node.right and node.right not in visited:
                    stack.append([node.right, depth + 1])

        return res