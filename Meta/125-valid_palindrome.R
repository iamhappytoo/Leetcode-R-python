ispalindrom <- function(str){
  str=tolower(str)
  strarr=unlist(strsplit(str,split=''))
  left=1
  right=length(strarr)
  while(left < right){
    if((strarr[left] %in%letters) &(strarr[right] %in%letters)){
      if(strarr[left]!=strarr[right]){
        return(FALSE)
      }else{
        left=left+1
        right=right-1
      }
    }
    if(!(strarr[left]%in%letters)){
      left=left+1
    }
    if(!(strarr[right]%in%letters)){
      right=right-1
    }
  }
  return(TRUE)
}
a='a1b2ca'
ispalindrom(a)