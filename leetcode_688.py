'''
leel=medium
topic=graph, bfs
'''
from collections import defaultdict
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dx=[-2,-1,1,2,2,1,-1,-2]
        dy=[1,2,2,1,-1,-2,-2,-1]

        queue=defaultdict(int)
        queue[row,column]=1.00000
        p=1.00000
        for _ in range(k):
            p=0.00000 
            nxt_q=defaultdict(int)
            for (pos_x,pos_y),prob in queue.items():
                for i in range(8):
                    new_x=pos_x+dx[i]
                    new_y=pos_y+dy[i]
                    if new_x>=0 and new_x<n and new_y>=0 and new_y<n:
                        nxt_q[new_x,new_y]+=prob/8 
                        p+=prob/8 
            queue=nxt_q
        return p