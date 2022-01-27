##Time complexity: O(n+nlogn)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = nums[i]*nums[i]
        output.sort()
        return output

##Time complexity: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        result = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                square = nums[left]
                left += 1
            else:
                square = nums[right]
                right -= 1
            result[i] = square * square
        return result
