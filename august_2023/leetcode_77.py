''' 
level=medium
topic= backtarcking, but i used itertools

Later I will implement it with backtracking
''' 
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        def helper(ind, res):
            if len(res) == k:
                ans.append(res.copy())
                return 

            for num in range(ind, n+1):
                res.append(num)
                helper(num+1, res)
                res.pop()

        helper(1, [])

        return ans