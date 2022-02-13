class Solution:
    def nextPermutation(self,nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        i = length-1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
            
        if i == 0:
            nums.sort()
            return nums

        i -= 1
        j = length - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        b = nums[i+1:]
        nums[i+1 : ] = b[::-1]

        
        return nums

      
      
###Line 13 if I use nums = nums[::-1], it will gives me error saying that nums=[3,2,1] does not generate [1,2,3] as output. Which is very weird. When I change it to nums.sort(),
###the error disappeared.
