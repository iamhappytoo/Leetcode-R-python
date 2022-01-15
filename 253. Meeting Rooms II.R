meetingrm <- function(arr){
  len=nrow(arr)
  arrnew <- as.data.frame(rbind(cbind(arr[,1],rep(1,len)), cbind(arr[,2], rep(-1,len))))
  arrnew <- arrnew[order(arrnew$V1),]
  maxmeeting = 0
  cumsum = 0
  for(i in 1:(2*len)){
    cumsum = cumsum + arrnew[i,2]
    maxmeeting = max(maxmeeting, cumsum)
  }
  return(maxmeeting)
}

meeting=rbind(c(0,30),c(5,10),c(15,20))
meetingrm(meeting)

##Another way in Python using min_heap
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_room = []
        
        intervals.sort(key = lambda x:x[0])
        heapq.heappush(free_room, intervals[0][1])
        
        for i in intervals[1:]:
            
            if free_room[0] <= i[0]:
                heapq.heappop(free_room)
                
                
            heapq.heappush(free_room,i[1])
        return len(free_room)
        
###Another solution with sorting:
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        used_rooms = 0
        
        start_timings = sorted(i[0] for i in intervals)
        end_timings = sorted(i[1] for i in intervals)
        
        L = len(intervals)
        
        end_pointer = 0
        start_pointer = 0
        
        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -=1
                end_pointer += 1
                
            used_rooms += 1
            start_pointer += 1
            
        return used_rooms
