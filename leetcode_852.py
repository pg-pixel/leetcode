class Solution:
    def __call__(self, arr):
        return self.peakIndexInMountainArray(arr)
    
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        l=0 
        r=n

        while l<=r:
            mid=(l+r)//2 
            if (mid==n-1 or arr[mid]>arr[mid+1]) and (mid==0 or arr[mid]>arr[mid-1]):
                return mid 
            if arr[mid]>arr[mid+1] and arr[mid]<arr[mid-1]:
                r=mid-1 
            else:
                l=mid+1
                
arr_lst=[
    [0,1,0],
    [0,2,1,0],
    [0,10,5,2] 
]

def driver():
    solver=Solution()
    for lst in arr_lst:
        print(solver(lst))
        
if __name__=='__main__':
    driver()