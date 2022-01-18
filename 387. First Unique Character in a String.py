class Solution:
    def firstUniqChar(self, s: str) -> int:
        mydict = {}
        for i,c in enumerate(s):
            if c not in mydict:
                mydict[c]=[i,1]
            else:
                mydict[c][1]+=1
        for i,key in enumerate(s):
            if mydict[key][1]==1:
                return i
        return -1
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i,ch in enumerate(s):
            if count[ch]==1:
                return i
        return -1
