class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                
                lo = j+1
                hi = n-1
                
                while lo < hi:
                    Sum = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if Sum < target:
                        lo += 1
                    elif Sum > target:
                        hi -= 1
                    else: 
                        res.append([nums[i],nums[j],nums[lo],nums[hi]])
                        hi -= 1
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
        return res
                    
