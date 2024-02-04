class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []   #list of lists of integers making up the entire triangle
        if (numRows == 1):
            triangle.append([1])    
        elif (numRows == 2):
            triangle.append([1])
            triangle.append([1,1])
        else:
            i = 2
            j = 1
            element = 1
            row = [1]
            triangle.append([1])
            triangle.append([1,1])
            while (i < numRows):
                while (j < i):
                    element = (element * (i - j + 1))/j
                    row.append(element)
                    j += 1
                row.append(1)
                triangle.append(row)
                element = 1
                row = [1]
                i += 1
                j = 1
        return triangle