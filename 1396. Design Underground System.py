class UndergroundSystem:

    def __init__(self):
        self.customtable = collections.defaultdict()
        self.routetable  = collections.defaultdict()
        self.numjourneytable = collections.defaultdict()
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customtable[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        tempName = self.customtable[id][0]
        length   = t-self.customtable[id][1]
        route   = tempName + '-' + stationName
        self.routetable[route]=self.routetable.get(route,0)+length
        self.numjourneytable[route]=self.numjourneytable.get(route,0)+1
        ##Better to delete the overwritten part to avoid slowly increasing 
        ##memory usage of the computer. How to remove it??
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        string = startStation + '-' + endStation
        return self.routetable[string]/self.numjourneytable[string]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
