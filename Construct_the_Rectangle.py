class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math

        x = int(math.floor(math.sqrt(area)))

        while True:
            if((area/x)*x == area):
                W = x
                break
            else:
                x += -1
        
        L = area/W
        return([L,W])