'''
level =medium 
topic= binary search
'''

from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def calculator(speed):
            count=0
            for i in range(n):
                if i==n-1:
                    count+=dist[i]/speed
                else:
                    count+=(ceil(dist[i]/speed))

            return count

        
        n=len(dist)
        if n>=hour+1:
            return -1
        l=1 
        r= sum(dist)*100
        while l<r:
            mid=(l+r)//2 
            val= calculator(mid)

            if val<=hour :
                r = mid 
            else:
                l=mid+1

        return int(l)
