"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adj = {
            node: Node(node.val)
        }
        
        stack = [node]

        while stack:
            curr = stack.pop()
            for n in curr.neighbors:
                if n not in adj:
                    adj[n] = Node(n.val)
                    stack.append(n)
                adj[curr].neighbors.append(adj[n])

        return adj[node]