''' 
level=medium 
topic=trees, dp
logic=create all posiblities of left side trees and right side trees and return a new tree with combinations of left trees and right trees
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        self.dp={0:[], 1:[TreeNode()]}
        def create(n):
            if n in self.dp:
                return self.dp[n]

            if n&1==0:
                self.dp[n]=[]
                return []

            ans = []

            for i in range(1,n,2):
                left_side  = create(i)
                right_side = create(n-i-1) 

                for l_tree in left_side:
                    for r_tree in right_side:
                        root = TreeNode(0, l_tree, r_tree)
                        ans.append(root)
            self.dp[n]=ans 
            return ans

        return create(n)
        