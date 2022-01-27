class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        Sum = sum(nums)
        if Sum < target:
            return 0
        else:
            n = len(nums)
            minlen = n
            left = 0
            right = 0
            while right < n and left < n:
                if sum(nums[left:(right+1)]) < target:
                    right += 1
                else:
                    minlen = min(minlen, right+1-left)
                    left += 1
            
            return minlen
                
