'''
level= Hard 
concept- Modified Kadane's algo 
TC = O(n(k^2))
SC = O(1)
'''

class Solution:
    def __call__(self, s:str)->int:
        return self.largestVariance(s)
    
    def largestVariance(self, s: str) -> int:
        count_arr = [0]*26 

        for char in s:
            count_arr[ord(char) - ord('a')]+=1 

        ans = 0 

        for i in range(26):
            for j in range(26):
                if i==j or count_arr[i]==0 or count_arr[j]==0:
                    continue 

                major = chr(i + ord('a'))
                minor = chr(j + ord('a'))
                major_count = 0
                minor_count = 0 
                __minors = count_arr[j]

                for ch in s:
                    if ch==major:
                        major_count+=1 
                    if ch==minor:
                        minor_count+=1
                        __minors-=1

                    if minor_count>0:
                        ans = max(ans, major_count-minor_count)

                    if major_count<minor_count and __minors >0:
                        major_count = 0 
                        minor_count = 0 
        return ans
    
def driver():
    string_input = [
        "aababbb",
        "abcde"
    ]
    solver = Solution()
    for s in string_input:
        print(solver(s))
        
if __name__ =='__main__':
    driver()
    
                 
        