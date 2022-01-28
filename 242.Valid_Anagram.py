class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}
        for ch in s:
            mydict[ch] = mydict.get(ch,0) + 1
        
        for ch in t:
            if mydict.get(ch,0) == 0:
                return False
            else:
                mydict[ch] -=1
        for key in mydict:
            if mydict.get(key) > 0:
                return False
        return True
