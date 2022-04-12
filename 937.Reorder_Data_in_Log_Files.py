class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit = 1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        
        return sorted(logs, key = get_key)
    
    
'''
Complexity Analysis

Let N be the number of logs in the list and MM be the maximum length of a single log.

Time Complexity: O(M⋅N⋅logN)

The sorted() in Python is implemented with the Timsort algorithm whose time complexity is O(N⋅logN).

Since the keys of the elements are basically the logs itself, the comparison between two keys can take up to O(M) time.

Therefore, the overall time complexity of the algorithm is O(M⋅N⋅logN).

Space Complexity: O(M⋅N)

First, we need O(M⋅N) space to keep the keys for the log.

In addition, the worst space complexity of the Timsort algorithm is O(N), assuming that the space for each element is O(1). Hence we would need O(M⋅N) space to hold the intermediate values for sorting.

In total, the overall space complexity of the algorithm is O(M⋅N+M⋅N)=O(M⋅N).
'''
