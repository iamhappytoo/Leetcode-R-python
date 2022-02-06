countbin <- function(s){
  arr=as.numeric(unlist(strsplit(s,split='')))
  savedict = NULL
  i=1
  count=1
  while(i <= (length(arr)-1)){
    if(arr[i+1] == arr[i]){
      count=count+1
    }else{
      savedict=c(savedict,count)
      count=1
    }
    i=i+1
  }
  savedict = c(savedict, count)
  if(length(savedict)<=1){
    return(0)
  }
  sumarr=0
  for(i in 1:(length(savedict)-1)){
      sumarr = sumarr + min(savedict[i],savedict[i+1])
  }
  return(sumarr)
}

linearscan <- function(s){
  arr=as.numeric(unlist(strsplit(s,split='')))
  prev=0
  cur=1
  ans=0
  for(i in 2:length(arr)){
      if(arr[i-1]!=arr[i]){
          ans = ans + min(prev, cur)
          prev = cur
          cur = 1
      }else{
          cur=cur+1
      }
  }
  return(ans + min(prev, cur))
}

s = "00110011"
countbin(s)
linearscan(s)


###Python solution###not elegant###
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        arr = []
        flag = s[0]
        curr = 0
        amount = 0
        while curr < len(s):
            while curr < len(s) and s[curr] == flag:
                curr += 1
                amount += 1
            arr.append(amount)
            amount = 0
            if curr < len(s):
                flag = s[curr]
        arr.append(amount)
        total = 0
        for i in range(len(arr)-2):
            total += min(arr[i],arr[i+1])
            
        return total
        
###Python solution###elegant###
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = [1]
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                group.append(1)
            else:
                group[-1] += 1
        
        ans = 0
        for i in range(1,len(group)):
            ans += min(group[i-1],group[i])
        return ans
###Python solution###more elegant###
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
                
        return ans + min(prev, cur)
