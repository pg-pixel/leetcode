'''
level=medium
topic= stacks
'''
class Solution:
    def __call__(self, asteroids:list[int])->list[int]:
        return self.asteroidCollision(asteroids)
    
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack)>1 and (stack[-2]>0 and stack[-1]<0):
                ast1, ast2 =stack.pop(), stack.pop()
                if abs(ast1)!=abs(ast2):
                    if abs(ast1)>abs(ast2):
                        stack.append(ast1)
                    else:
                        stack.append(ast2)

        return stack
    
asteroids_list=[
    [5,10,-5],
    [8,-8],
    [10,2,-5]
]

def driver():
    solver=Solution()
    for lst in asteroids_list:
        print(solver(lst)) 
        
if __name__=="__main__":
    driver()
