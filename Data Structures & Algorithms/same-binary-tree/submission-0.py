# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_p = set()
        visited_q = set()
        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if node_p and node_q == None or node_q and node_p == None:
                return False

            if node_p and node_p not in visited_p and node_q and node_q not in visited_q:
                visited_p.add(node_p)
                visited_q.add(node_q)

                if node_p.val != node_q.val:
                    return False
                
                if node_p.left not in visited_p and node_q.left not in visited_q:
                    stack_p.append(node_p.left)
                    stack_q.append(node_q.left)
                if node_p.right not in visited_p and node_q.right not in visited_q:
                    stack_p.append(node_p.right)
                    stack_q.append(node_q.right)

        return True