'''
level=medium 
topic=dp
'''

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

        cost_dp = [[0]*(m+1) for _ in range(n+1)] 

        for i in range(1, n+1):
            cost_dp[i][0] = cost_dp[i-1][0] + ord(s1[i-1])
        for i in range(1, m+1):
            cost_dp[0][i] = cost_dp[0][i-1] + ord(s2[i-1])

        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    cost_dp[i][j]=  cost_dp[i-1][j-1]
                else:
                    cost_dp[i][j] = min(cost_dp[i-1][j] + ord(s1[i-1]), cost_dp[i][j-1] + ord(s2[j-1]))

        return cost_dp[-1][-1]
                    
                        

