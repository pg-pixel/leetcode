''' 
level = medium 
topic =  binary search
''' 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(lst, target):
            n=len(lst)
            l=0
            r=n-1
            while l<=r:
                mid = (l+r)//2 
                if lst[mid]==target:
                    return mid, True
                if lst[mid]<target and (mid==n-1 or lst[mid+1]>target):
                    return mid, False
                if lst[mid]>target:
                    r=mid-1 
                else:
                    l=mid+1 
            return l, False 

        # step 1-> get searching row 
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][0]) 

        target_row , flag = binary_search(row, target)


        if flag:
            return True 

        # step2 find ele in row
        position, flag = binary_search(matrix[target_row], target)

        return flag

        