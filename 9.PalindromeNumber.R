# ispalin <- function(x){
#   s=unlist(strsplit(as.character(x),split=''))
#   if(length(s)==1){
#     return(TRUE)
#   }
#   ptst=1; edst=length(s)
#   while(ptst <edst){
#     if(s[ptst]!=s[edst]){
#       return(FALSE)
#     }else{
#       ptst=ptst+1
#       edst=edst-1
#     }
#   }
#   return(TRUE)
# }
#ispalin(-121)
##Followup check without converting to a string
ispalin <- function(x){
  if((x<0) | (x%%10==0 & x!=0)){
    return(FALSE)
  }
  reverse=0
  while(x>reverse){
    reverse=reverse*10+x%%10
    x=round(x/10)
  }
  return(x==reverse | x==round(reverse/10))
}
ispalin(-1121)
