profit <- function(prices){
  prof=0
  minpr=prices[1]
  for(i in 2:length(prices)){
    if(prices[i]>minpr){
      prof=max(prof,prices[i]-minpr)
    }else{
      minpr=prices[i]
    }
  }
  return(prof)
}
prices=c(7,6,1,3,4)
profit(prices)
