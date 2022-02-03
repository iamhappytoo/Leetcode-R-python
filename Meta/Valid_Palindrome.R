ispalindrome <- function(string){
  strarr=unlist(strsplit(string,split=''))
  start=1
  post=length(strarr)
  flag=0
  while(start<post){
    if(strarr[start]==strarr[post]){
      start=start+1; post=post-1
    }else if(flag==0){
      if(strarr[start]==strarr[post-1]){
        post=post-1; flag=1
      }else if(strarr[start+1]==strarr[post]){
        start=start+1; flag=1
      }else{
        return(FALSE)
      }
    }else{
      return(FALSE)  
    }
  }
  return(TRUE)
}
string='abc'
ispalindrome(string)



###Another method###
ispalindrome <- function(string){
  strarr=unlist(strsplit(string,split=''))
  start=1
  post=length(strarr)
  flag=0
  if(ispalindromeutil(strarr)==TRUE){
    return(TRUE)
  }else{
    for(i in 1:length(strarr)){
      if(ispalindromeutil(strarr[-i])){
        return(TRUE)
      }
    }
    return(FALSE)
  }
}
ispalindromeutil <- function(strarr){
  len=length(strarr)
  for(i in 1:round(len/2)){
    if(strarr[i]!=strarr[len-i+1]){
      return(FALSE)
    }
  }
  return(TRUE)
}
