'''
level=medium
topic= dictionary and dp
ques- find longest subsequence length with given difference
'''
class Solution:
    def __call__(self, arr:list[int], diff:int)->int:
        return self.longestSubsequence(arr, diff)
    
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        longest = {}
        ans=1

        for num in arr:
            if num-difference in longest:
                longest[num]=longest[num-difference]+1
                ans=max(ans, longest[num])
            else:
                longest[num]=1
        return ans
    
diff_lst=[1,1,-2]
arr_lst=[
    [1,2,3,4],
    [1,3,5,7],
    [1,5,7,8,5,3,4,2,1]
]

def driver():
    solver=Solution()
    for i, diff in enumerate(diff_lst):
        print(solver(arr_lst[i],diff))
        
if __name__=='__main__':
    driver()