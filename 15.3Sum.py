class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                
                left = i + 1
                right = len(nums)-1
                while left < right:
                    Sum = nums[i] + nums[left] + nums[right]
                    if Sum > 0:
                        right -= 1
                    elif Sum < 0:
                        left += 1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1

        return res
