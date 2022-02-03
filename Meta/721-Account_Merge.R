mergeaccount <- function(llist){
  visitedemail=NULL
  indarr=NULL
  emailGroup=list()
  for(i in 1:length(llist)){
    len=length(llist[[i]][])
    ind=i
    for(j in 2:len){
      if(!(llist[[i]][j] %in% visitedemail)){
        if(length(emailGroup)<ind){
          emailGroup[[ind]]=llist[[i]][j]
        }else{
          emailGroup[[ind]]=c(emailGroup[[ind]],llist[[i]][j])
        }
        visitedemail=c(visitedemail,llist[[i]][j])
        indarr=c(indarr,ind)
      }else{
        oldind=indarr[which(visitedemail==llist[[i]][j])]
        indarr[which(indarr==ind)]=oldind
        if(length(emailGroup)<ind | (length(emailGroup)>ind | is.null(emailGroup[ind]))){
          ind=oldind
        }else{
          emailGroup[[oldind]]=union(emailGroup[[oldind]],emailGroup[[ind]])
          emailGroup[[ind]]=NA
        }
      }
    }
  }
  nameemailGroup=format(emailGroup,llist)        
  return(nameemailGroup)
}
format <- function(emailGroup,llist){
  ##sort the record within each account
  ##insert the name before the email group at every record
  for(i in 1:length(emailGroup)){
    if(length(emailGroup[[i]])==0){
      next
    }
    emailGroup[[i]]=c(llist[[i]][1],sort(emailGroup[[i]]))
  }
  i=1
  while(i<=length(emailGroup)){
    if(length(emailGroup[[i]])==0){
      emailGroup[[i]]=NULL
    }else{
      i=i+1
    }
  }
  return(emailGroup)
}

account=as.list(c(list(c("John","johnsmith@mail.com","john_newyork@mail.com")),
                 list(c("John","johnsmith@mail.com","john00@mail.com")),
                 list(c("Mary","mary@mail.com")),
                 list(c("John","johnnybravo@mail.com"))))
mergeaccount(account)
