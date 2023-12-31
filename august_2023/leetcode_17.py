''' 
level = medium 
topic = backtracking 
''' 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {
            '2':['a', 'b', 'c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }

        ans = []

        if digits == '':
            return ans 


        def backtrack(index, result):
            if len(result)==len(digits):
                ans.append("".join(result))
                return 

            for alphabet in mapping[digits[index]]:
                result.append(alphabet) 
                backtrack(index+1, result)
                result.pop()

        backtrack(0, [])

        return ans

        