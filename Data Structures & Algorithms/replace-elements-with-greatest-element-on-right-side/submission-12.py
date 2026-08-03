class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            if len(arr[i:])>1:
                r = max(arr[i+1:])
                arr[i]=r
        
        arr[len(arr)-1]=-1
        return arr
        