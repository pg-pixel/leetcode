'''
level=medium
topic=sorting, greedy
logic: sorting intervals on the basis of end time. Then finding total intervals we can have as non ovrlapping and then subtract them from total intervals
'''
class Solution:
    def __call__(self, intervals:list[list[int]])->int:
        return self.eraseOverlapIntervals(intervals)
    
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count=0 
        start = float('-inf')
        for interval in intervals:
            if interval[0]>=start:
                count+=1 
                start = interval[1]

        return len(intervals)-count
    
intervals_list=[
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,2],[2,3]]
]

def driver():
    solver=Solution()
    for intervals in intervals_list:
        print(solver(intervals))
        
if __name__=='__main__':
    driver()