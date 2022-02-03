gettimedict <- function(logs){
  timedict=matrix(rep(NA,3*length(logs)),ncol=3)
  count=1
  for(i in 1:length(logs)){
    arr=unlist(strsplit(logs[[i]],split=''))
    id=as.numeric(arr[1])
    if(arr[2]=='start'){
      start=arr[3]
      if(id %in% timedict[,1]){
        ind=which(timedict[,1]==id)
        timedict[ind,2]=min(start,timedict[ind,2])
      }else{
        timedict[count,c(1,2)]=c(id,start)
      }
    }else{
      end=arr[3]
      if(id %in%timedict[,1]){
        ind=which(timedict[,1]==id)
        timedict[ind,3]=max(end,timedict[ind,3])
      }else{
        timedict[count,c(1,3)]=c(id,end)
      }
    }
  }
  return(timedict)
}
exclusivetime <- function(logs){
  timedict=gettimedict(logs)
  summ=rep(0,max(timedict[,3])-min(timedict[,2]+1))
  timedict=as.data.frame(timedict)
  timedict=timedict[order(timedict$V2),]
  for(i in 1:(nrow(timedict)-1)){
    start=timedict[i,2]
    summ[start]=timedict[i,1]
    curr=start+1
    while(curr<timedict[i+1,2]){
      summ[curr]=timedict[i,1]
    }
  }
  id=timedict[i,1]
  summ[i]=timedict[i,1]
  curr=timedict[i,2]
  while(curr<=timedict[i,3]){
    summ[curr]=timedict[i,1]
    curr=curr+1
  }
  id=which(timedict[,3]==length(summ))
  while(curr<=length(summ)){
    summ[curr]=id
  }
  sortid=sort(timedict[,1])
  result=rep(0,length(unique(sortid)))
  for(i in 1:length(sortid)){
    result[i]=length(which(summ==sortid[i]))
  }
  return(result)
}


logs=as.list(c("0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"))
exclusivetime(logs)