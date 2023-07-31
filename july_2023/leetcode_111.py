'''
level=easy
Aim is to find min depth in the binary tree
Approac=bfs(level order traversal)
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right 
         
class Solution:
    
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q= deque()
        start, end = root, root 
        q.append((start,1))

        while q:
            node, depth=q.popleft()
            if not node:
                continue 
            if not node.left and not node.right:
                return depth 
            q.append((node.left, depth+1))
            q.append((node.right, depth+1))

            if node==end:
                if q:
                    end=q[-1]
                    
