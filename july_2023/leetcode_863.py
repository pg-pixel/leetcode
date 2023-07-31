'''
level=medium 
aim is to find all thhe nodes in a binary tree which are k  distance appart.
Logic= First Mark parent nodes and then apply bfs on the target node 
'''
from collections import deque

class TreeNode:
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        root.prev = None 
        def mark_parents(node):
            if node.left:
                left = node.left
                left.prev = node 
                mark_parents(node.left)
            if node.right:
                right = node.right 
                right.prev = node 
                mark_parents(node.right)
        mark_parents(root)
        visited = set()
        ans = []
        q= deque()
        q.append((target,0))
        visited.add(target)
        while q:
            curr, dist = q.popleft()
            if dist == k:
                ans.append(curr.val)

            if curr.left and dist<k and curr.left not in visited:
                q.append((curr.left, dist+1))
                visited.add(curr.left)
            if curr.right and dist<k and curr.right not in visited:
                q.append((curr.right, dist+1))
                visited.add(curr.right)
            if curr.prev and dist<k and curr.prev not in visited:
                q.append((curr.prev, dist+1))
                visited.add(curr.prev)
        return ans