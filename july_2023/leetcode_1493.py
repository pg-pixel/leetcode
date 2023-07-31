'''
level-medium
Aim is to find longest subarray for a binary array which has all 1 after deleting 1 element of the originl array.
Since subarrays are continuous part of the, we can use concept of prefix and suffix as pre computation of what we have before and after at a particular index.
Answer will be calculated at an index which has a zero.
'''

class Solution:
    def __call__(self, lst: list[int]) -> int :
        return self.longestSubarray(lst)
    
    def longestSubarray(self, nums: list[int]) -> int:
        zero_index_set=set()
        n=len(nums)

        if n==1:
            return 0

        prefix=[nums[0]]
        for i in range(1,n):
            if nums[i]==0:
                prefix.append(0)
                zero_index_set.add(i)
            else:
                prefix.append(prefix[-1]+1)

        if len(zero_index_set)==0:
            return n-1

        suffix=[0 for _ in range(n)]
        suffix[-1]=nums[-1]

        for i in range(n-2,-1,-1):
            if nums[i]==0:
                suffix[i]=0 
            else:
                suffix[i]=suffix[i+1]+1

        ans=0 
        for index in zero_index_set:
            if index==0:
                ans=max(ans,suffix[index+1])
            elif index==n-1:
                ans=max(ans, prefix[n-2])
            else:
                ans=max(ans, prefix[index-1]+suffix[index+1])

        return ans
        
        
input_set=[
    [1,1,0,1],
    [0,1,1,1,0,1,1,0,1],
    [1,1,1]
]

solver=Solution()

for my_input in input_set:
    print(solver(my_input))