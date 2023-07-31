''' 
level = hard
topic = Binary search
'''

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l=1
        r=sum(batteries)//n
        while l<r:
            mid = r-(r-l)//2
            count = 0
            for cell in batteries:
                count+=min(cell,mid) 

            if count//n>=mid:
                l = mid 
            else:
                r = mid-1 
        return l 