''' 
level = medium
topic= backtracking
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtrack(result):
            if len(result) == len(nums):
                ans.append(result[:]) 
                return 

            for num in nums:
                if num not in result:
                    result.append(num)
                    backtrack(result)
                    result.pop()

        backtrack([])

        return ans