'''
level=medium
technique=topological sort 
logic= if from topological sort, we are able to finish total corses provided, return true
'''
from collections import deque

class Solution:
    def __call__(self, course_count: int , pre_req: list[list[int]])->bool:
        return self.canFinish(course_count, pre_req)

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0]*numCourses 
        adj = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            curr, req = prereq 
            adj[req].append(curr)
            indegree[curr]+=1 
        
        q=deque()
        count=0
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            cur = q.popleft() 
            count +=1 
            for neigbhor in adj[cur]:
                indegree[neigbhor]-=1 
                if indegree[neigbhor]==0:
                    q.append(neigbhor) 

        if count==numCourses:
            return True 
        return False

course_count_list=[2,2]
pre_req_list=[
    [[1,0]],
    [[1,0],[0,1]]
]

def driver():
    solver=Solution()
    for i, count in enumerate(course_count_list):
        print(solver(count, pre_req_list[i])) 


if __name__=='__main__':
    driver()
        