''' 
level=hard
topic=dp
'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        prefix = [1]
        suffix = [1 for _ in range(n)] 

        # prefix calculation
        for i in range(1, n):
            if s[i]==s[i-1]:
                prefix.append(1+prefix[-1])
            else:
                prefix.append(1)

        # suffix calculation 
        for i in range(n-2, -1, -1):
            if s[i]==s[i+1]:
                suffix[i]=suffix[i+1]+1 

        #dp = defaultdict(dict)
        '''
        @lru_cache(None)
        def calculator(i,j):
            if i>j:
                return 0
            
            if s[i]==s[j]:
                return 1+ calculator(i+suffix[i], j-prefix[j])
            else:
                return 1+ min(calculator(i+suffix[i], j), calculator(i, j-prefix[j])) 
        return calculator(0, n-1)
        '''

        @cache
        def calc(left, right): 
            if left >= right: 
                return 0
            best = calc(left + 1, right) + 1
            for index in range(left + 1, right + 1): 
                if s[left] == s[index]: 
                    best = min(best, calc(left, index - 1) + calc(index, right))
            return best
        return calc(0, n - 1) + 1
        '''
        dp = [[0 for _ in range(n)] for _ in range(n)] 

        for size in range(n):
            for i in range(n-size+1):
                j=i+size -1
                if s[i]==s[j]:
                    dp[i][j]= 1 + dp[i+suffix[i]][j-prefix[j]]
                else:
                    dp[i][j]= 1+ min(dp[i+suffix[i]][j], dp[i][j-prefix[j]] )

        return dp[-1][-1]
        '''
                