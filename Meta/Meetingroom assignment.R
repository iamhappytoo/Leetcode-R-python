getMaxmeeting<- function(arr){
  start=arr[,1]
  end=arr[,2]
  df <- as.data.frame(rbind(cbind(start,rep(1,length(start))),
                      cbind(end,rep(-1,length(start)))))
  colnames(df) = c("time","value")
  df=df[order(df$time),]
  cnt=0
  max=0
  for (i in 1:nrow(df)){
    cnt=cnt+df[i,2]  
    if (cnt>max){
      max=cnt
    }
  }
  return(max)
}
vec1=c(0,5,15)
vec2=c(30,10,20)
arr=cbind(vec1,vec2)
getMaxmeeting(arr)
