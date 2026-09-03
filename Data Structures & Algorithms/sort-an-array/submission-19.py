class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        
    
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2

        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        return self.merge(left, right)
    
    def merge(self, l, r):
        i,j =0,0
        res=[]
        while i<len(l) and j< len(r):
            if l[i]<r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        res.extend(l[i:])
        res.extend(r[j:])
        return res

        