checkorder <- function(wordarr,order){
  order=unlist(strsplit(order,split=''))
  len=length(wordarr)
  for(i in 1:(len-1)){
    if(check(wordarr[i],wordarr[i+1],order)==0){
      return(FALSE)
    }
  }
  return(TRUE)
}
check <- function(word1,word2,order){
  word1arr = unlist(strsplit(word1,split=''))
  word2arr = unlist(strsplit(word2, split=''))
  curr=1
  while(curr<=min(length(word1arr),length(word2arr))){
    if(word1arr[curr]!=word2arr[curr]){
      ind1=which(order==word1arr[curr])
      ind2=which(order==word2arr[curr])
      if(ind1>ind2){
        return(0)
      }else{
        return(1)
      }
    }
    curr=curr+1
  }
  if(length(word1arr)>length(word2arr)){
    return(0)
  }else{return(1)}
}

words=c("hello","leetcode")
order = "hlabcdefgijkmnopqrstuvwxyz"
checkorder(words,order)
##ERROR:used return 0 instead of return(0), wrong. forgot to ensure the false when same prefix but longer one precedes shorter one.