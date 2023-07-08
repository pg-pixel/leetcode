'''
level-Hard
########################################################################################################
You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

Divide the marbles into the k bags according to the following rules:

No bag is empty.
If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
The score after distributing the marbles is the sum of the costs of all the k bags.

Return the difference between the maximum and minimum scores among marble distributions.

1 <= k <= weights.length <= 105
1 <= weights[i] <= 109
########################################################################################################
we want to divide the array in k continuous part. Target is to get maximum distribution and minimum distribution.
we will have k-1 splits. Each split is nothing but sum of its neibhors. So we will have all pairs(splits).
We will sort it(greedy) and take k-1 maximum and minimum pairs.
'''
class Solution:
    def __call__(self,weights: list[int], k: int) -> int: 
        return self.putMarbles(weights, k)
    
    def putMarbles(self, weights: list[int], k: int) -> int:
        
        _n:int=len(weights)
        _pairs:list[int]=[0]*(_n-1)

        for i in range(_n-1):
            _pairs[i]=weights[i]+weights[i+1]

        _pairs.sort()
        _ans:int = 0 

        for i in range(k-1):
            _ans+= _pairs[_n-2-i]-_pairs[i]

        return _ans
 
def driver()->None:
    weight_lst=[
        [1, 3],
        [1,3,5,1]
        ]
    k_lst = [2,2]
    
    solver=Solution()
    for i,k in enumerate(k_lst):
        print(solver(weight_lst[i],k))
       
if __name__=='__main__':
    driver()