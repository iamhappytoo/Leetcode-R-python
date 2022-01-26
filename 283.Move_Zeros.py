class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt1 = 0
        pt2 = 0
        while pt1 < len(nums) and pt2 < len(nums):
            if nums[pt1] !=0:
                pt1 +=1
                pt2 +=1
            else:
                while pt2 < len(nums) and nums[pt2] == 0:
                    pt2 +=1
                if pt2 < len(nums):
                    nums[pt1] = nums[pt2]
                    nums[pt2] = 0
                    pt1 += 1
                
        return nums
