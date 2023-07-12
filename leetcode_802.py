'''
level=medium
topic=graph
concept= topological sort
logic:
1. If we travel from any node, we will either land on a terminal node(as no more node to travel) or we will get stuck in a loop.
2. We know terminal nodes are safe nodes. All the nodes which has direct connection only to terminal nodes are also safe nodes.
3. From point 2, we can say, recursively we can have more safe nodes if we check incoming edges of previous safe nodes.
4. But we can't go back(nodes are directed), so we will make a new graph(reverese of original) and apply topological sort on it and will mark the nodes whose indegree becomes zero.
5. topological sort will never mark nodes which are in loop. so marked/unmarked nodes will be same in case of original and new graph.
6. Hence all the marked nodes are our answer.
'''
from collections import deque 
class Solution:
    def __call__(self, graph: list[list[int]])->list[int]:
        return self.eventualSafeNodes(graph)
    
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n=len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0]*n 
        
        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                indegree[i]+=1 
                
        q=deque()
        
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                
        safe_nodes = [False]*n 
        
        while q:
            node =q.popleft()
            safe_nodes[node]=True 
            
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
                    
        ans=[]
        for i,value in enumerate(safe_nodes):
            if value:
                ans.append(i)
                
        return ans
    
graphs = [
    [[1,2],[2,3],[5],[0],[5],[],[]],
    [[1,2,3,4],[1,2],[3,4],[0,4],[]]
]

def driver():
    solver=Solution()
    for graph in graphs:
        print(solver(graph))
        
if __name__=='__main__':
    driver()
