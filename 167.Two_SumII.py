###Solution with hashtable.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hasha = {}
        for i, num in enumerate(numbers):
            hasha[num] = i
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hasha and hasha[complement] != i:
                return [i+1, hasha[complement]+1]
##Another solution with two pointers
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while True:
            Sum = numbers[left] + numbers[right] 
            if Sum == target:
                return [left+1, right+1]
            elif Sum < target:
                left += 1
            else:
                right -= 1
        
