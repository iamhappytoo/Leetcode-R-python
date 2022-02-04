maxsub <- function(arr){
  if(length(arr)==1){
    return(sum(arr))
  }
  currentsub = arr[1]
  maxsubarr = arr[1]
  count=2
  while(count <= length(arr)){
    currentsub = max(arr[count], currentsub + arr[count])
    maxsubarr = max(maxsubarr, currentsub)
    count=count+1
  }
  return(maxsubarr)
}


nums = c(5,4,-1,7,8)
maxsub(nums)

###Another way divide and conqure 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        subarray = nums[0]
        for num in nums[1:]:
            subarray = max(num, subarray+num)
            maxsum = max(maxsum, subarray)
        
        return maxsum
