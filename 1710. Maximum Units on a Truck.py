class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: -x[1])
        sumunit = 0
        for num_box, unit in boxTypes:
            if num_box <= truckSize:
                sumunit += num_box * unit
                truckSize -= num_box
            else:
                sumunit += truckSize * unit
                break        
        return sumunit
        
##Another solution not using if else##
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        max_units = 0
        cur_size = 0
        for num_box, unit in boxTypes:
            max_units += unit * min(truckSize - cur_size, num_box)
            cur_size += min(truckSize - cur_size, num_box)
        return max_units
