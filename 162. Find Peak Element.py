class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i]  > nums[i+1]:
                return i
        
        return len(nums)-1
##O(n)

##iterative Binary search, O(logn)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        midflag = (left+right)//2
        while left < right:
            if nums[midflag] <= nums[midflag+1]:
                left = midflag + 1
            else:
                right = midflag
            midflag = (left + right)//2
        return midflag
