'''
level-medium
question is about finding max length subarray with atmost k occurence, so we have used sliding window here.
'''

class Solution:
    
    def __call__(self, answerKey:str, k: int)->int:
        return self.maxConsecutiveAnswers(answerKey, k)
    
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def window_atmost_(answerKey,k, symbol, counter_symbol):
            i,j, counter=0,0,k
            ans= 0
            while j<len(answerKey):
                if  answerKey[j]==symbol:
                    counter-=1 
                    if counter==0:
                        ans=max(ans, j-i+1)
                        break
                j+=1 
            if j==len(answerKey):
                ans = max(ans,len(answerKey))
            j+=1 
            while j<len(answerKey):
                if answerKey[j]==symbol:
                    while answerKey[i]==counter_symbol:
                        i+=1 
                    i+=1 
                    ans = max(ans, j-i+1)
                    j+=1
                else: 
                    ans = max(ans, j-i+1)
                    j+=1
            return ans

        return max(window_atmost_(answerKey,k,'T','F'), window_atmost_(answerKey,k,'F','T'))
    
string_list=[
    "TTFF",
    "TFFT",
    "TTFTTFTT"
]
k_list=[2,1,1]

solver=Solution()

for index, k in enumerate(k_list):
    print(solver(string_list[index],k))