class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        left = 0
        right = 1
        while right < len(nums):
            if nums[right]==nums[left]:
                right += 1
            else:
                nums[left+1] = nums[right]
                left += 1
                
        return left + 1
