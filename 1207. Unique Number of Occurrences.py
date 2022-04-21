class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = collections.defaultdict()
        mydict1 = collections.defaultdict()
        for a in arr:
            mydict[a]=mydict.get(a,0)+1
            
        for i in list(mydict.values()):   
            if i in mydict1:
                    return False
            else:
                    mydict1[i] = 1

        return True
###Another solution
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = collections.defaultdict()
        mydict1 = collections.defaultdict()
        for a in arr:
            mydict[a]=mydict.get(a,0)+1

        return len(list(mydict.values())) == len(set(list(mydict.values())))
            
