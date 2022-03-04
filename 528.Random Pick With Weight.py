import random
class Solution:

    def __init__(self, w: List[int]):
        self.data = w
        self.ratio = [sum(w[0:i+1]) for i in range(len(w))]
        self.Sum = sum(w)
    def pickIndex(self) -> int:
        num = random.random()*self.Sum
        return bisect.bisect_left(self.ratio, num)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
