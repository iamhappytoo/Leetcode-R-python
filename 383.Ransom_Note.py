##One solution using hashmap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myhash = {}
        for ch in magazine:
            myhash[ch] = myhash.get(ch, 0) + 1
        
        for ch in ransomNote:
            if myhash.get(ch,0) == 0:
                return False
            else:
                myhash[ch] -= 1
            
        return True

##Another solution using direct simulation
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            else:
                location = magazine.index(ch)
                magazine = magazine[:location]+magazine[location+1:]
        
        return True
      
