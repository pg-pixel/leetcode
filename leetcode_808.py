'''
level = medium
topic = dp , mathematics
'''
class Solution:
    def soupServings(self, n: int) -> float:
        if n>=5000:
            return 1.0000 

        dp = defaultdict(dict)

        def cal(i,j):
            if i<=0 and j<=0:
                return 0.5 
            if i<=0:
                return 1.0 
            if j<=0:
                return 0 

            if i in dp and j in dp[i]:
                return dp[i][j]

            dp[i][j]=(cal(i-100,j)+cal(i-75,j-25)+cal(i-50,j-50)+cal(i-25,j-75))/4.0

            return dp[i][j]

        return cal(n,n)

         
        

