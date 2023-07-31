''' 
level = medium
topic = greedy, divide and conquer
logic= power calculation
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def calculator(num, pow):
            if pow==0:
                return 1 
            elif pow==1:
                return num
            elif pow<0:
                return 1.0/calculator(num, -1*pow)

            if pow&1==1:
                #odd case 
                return num*calculator(num*num,(pow-1)//2)
            else:
                return calculator(num*num,pow//2)

        return calculator(x,n)

