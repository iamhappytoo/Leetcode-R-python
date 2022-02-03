addstr <- function(str1,str2){
  strarr1=unlist(strsplit(str1,split=''))
  strarr2=unlist(strsplit(str2,split=''))
  len1=length(strarr1)
  len2=length(strarr2)
  if(len1<len2){ ##make sure len1>= len2
    arrtemp=strarr2
    strarr2=strarr1
    strarr1=arrtemp
  }
  outputarr=rep(0,len1+1)
  len=len1+1
  carry=0
  for(i in 1:len2){
    digit2=as.numeric(strarr2[len2-i+1])
    digit1=as.numeric(strarr1[len1-i+1])
    outputarr[len-i+1]=(digit2+digit1+carry)%%10
    carry=floor((digit2+digit1+carry)/10)
  }
  if(carry>0){
    outputarr[len-len2]=carry
  }
  ind=which(outputarr>0)
  outputarr=outputarr[ind]
  return(paste0(outputarr,collapse=''))
}
str1='12'
str2='23'
output=addstr(str1,str2)
print(output)