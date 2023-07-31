'''
level=Hard
concept- binary search(using inbuilt library bisect), DP
logic- More like 01 knapsack. But a little upgraded version.
1. We 1st sorted the events list on the basis of starting time(as we want to choose event which will fetch us max value)
sorting with end time will not work as we miss potential cases in choosing.
same goes with value as we cant track events overlapping properly.
2. we apply DP on the sorted events list.
3. We are travelling from last event to the 1st event and if choosing we reduce count of event visited.
TC=O(nklog(n))
SC=O(nk)
'''

from bisect import bisect_right
class Solution:
    def __call__(self, events:list[list[int]], k:int)->int:
        return self.maxValue(events, k)
    
    def maxValue(self, events: list[list[int]], k: int) -> int:
    
        events.sort()
        n=len(events)

        _max_val=[[0]*(n+1) for _ in range(k+1)]

        start_times = [start for start,end, value in events]

        for i in range(n-1,-1,-1):
            for j in range(1,k+1):
                new_i=bisect_right(start_times,events[i][1])# choosing a new index if we select curr event
                _max_val[j][i]=max(events[i][2]+_max_val[j-1][new_i], _max_val[j][i+1]) #choosing or not choosing

        return _max_val[k][0]
    
events_lst=[
    [[1,2,4],[3,4,3],[2,3,1]],
    [[1,2,4],[3,4,3],[2,3,10]],
    [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
]

k_list =[2,2,3]

def driver():
    solver=Solution()
    for i, k in enumerate(k_list):
        print(solver(events_lst[i],k))
        
if __name__=='__main__':
    driver()