'''
level- medium
Aim is to find minimum length subarray with target sum.
Here we will use variable length sliding window
'''

class Solution:
    
    def __call__(self, target:int, nums:list[int])->int:
        return self.minSubArrayLen(target, nums)
    
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans=float('inf')
        n=len(nums)
        i,j=0,0 
        curr_sum=0

        while j<n:
            curr_sum+=nums[j]
            if curr_sum>=target: # hitting the first window
                ans= min(ans, j-i+1) 
                break 
            j+=1 

        if ans==float('inf'): # if still infinity, target not possible 
            return 0 

        while j<n: # varying the window again
            if curr_sum>=target: # reducing the window
                curr_sum -=nums[i]
                i+=1 
            else: # increasing the window
                j+=1 
                if j<n: # edge case if we are in the end.
                    curr_sum += nums[j]
                    
            if curr_sum>=target: # checking if we want the curr window to be in answer or not
                ans= min(ans, j-i+1)

            if i==j: # handling another edge case to vary the window
                if j==n-1:
                    j+=1
                else:
                    curr_sum=nums[j+1]
                    j+=1 

        return ans       
    
target_lst=[7,4,11]      
array_list=[
    [2,3,1,2,4,3],
    [1,4,4],
    [1,1,1,1,1,1,1,1]
]   
solver=Solution()
for index, target in enumerate(target_lst):
    print(solver(target, array_list[index]))