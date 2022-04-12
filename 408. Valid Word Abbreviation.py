class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pt1, pt2 = 0, 0
        while pt1 < len(word) and pt2 < len(abbr):
            if word[pt1].isalpha() and abbr[pt2].isalpha():
                if word[pt1] == abbr[pt2]:
                    pt1 += 1
                    pt2 += 1
                else:
                    return False
            else:
                if abbr[pt2] == '0':
                    return False
                else:
                    string = ""
                    while pt2 < len(abbr) and abbr[pt2].isnumeric():
                        string += abbr[pt2]
                        pt2 += 1
                    if pt1 + int(string)-1 >= len(word):
                        return False
                    else:
                        pt1 += int(string)
                
        if pt1 < len(word) or pt2 < len(abbr):
            return False
        
        return True
      
      
      
      
