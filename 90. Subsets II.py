class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums or len(nums) == 0:
            return results
        nums.sort()
        length = len(nums)
        subset = []
        self.subsetsHelper(nums, 0, subset, results, length)
        
        return results
    def subsetsHelper(self, nums, startIndex, subset, results, length):
            ##deep copy subset & put in results
            results.append(subset.copy())
            
            for i in range(startIndex, length):
                if i != 0 and nums[i] == nums[i - 1] and i > startIndex:
                    continue
                subset.append(nums[i])
                self.subsetsHelper(nums, i + 1, subset, results, length)
                subset.pop()
    
Time complexity: o(N*2^N), space complexity: O(N)
