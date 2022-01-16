BS <- function(nums, target){
  len = length(nums)
  start = 1
  end = len
  while(start <= end){
    mid = ceilings((start + end) / 2)
    if (target < nums[mid]){
        end = mid - 1
    }
    if(target > nums[mid]){
        start = mid + 1
    }
    if(target == nums[mid]){
        return(mid-1)
    }
  }
  return(-1)
}
