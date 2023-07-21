'''
level=medium
topic=dp
logic=LIS
'''
class Solution:
    def __call__(self, nums:list[int])->int:
        return self.findNumberOfLIS(nums)
    
    def findNumberOfLIS(self, nums: list[int]) -> int:
        length = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]>nums[j]:
                    if length[j]+1 >length[i]:
                        length[i]=length[j]+1 
                        count[i]=0
                    if length[j]+1 == length[i]:
                        count[i]+=count[j]

        maxi = max(length)
        ans=0 
        for i in range(len(nums)):
            if length[i]==maxi:
                ans+=count[i]

        return ans
    
nums_list=[
    [1,3,5,4,7],
    [2,2,2,2,2]
]

def driver():
    solver=Solution()
    for lst in nums_list:
        print(solver(lst))
        
if __name__=="__main__":
    driver()