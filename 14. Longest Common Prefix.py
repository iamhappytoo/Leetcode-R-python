class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            
        def commpref(s1, s2):
            res = ""
            point = 0
            while point < min(len(s1),len(s2)) and s1[point] == s2[point]:
                    res += s1[point]
                    point += 1
                
            return res
        
        
        if len(strs) <= 1:
            return strs[0]
        else:        
            output = commpref(strs[0], strs[1])
            pt = 2
            while pt < len(strs) and output != "":
                output = commpref(output, strs[pt])
                pt += 1
            return output
