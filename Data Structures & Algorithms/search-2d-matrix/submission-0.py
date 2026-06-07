class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        I think what we have to do is perform a binary search to get the
        correct row and then within the row do the correct column and then
        return True or False if we find a match or not
        
        Perform a binary search on the first number in the rows, in each
        given row perform a binary search on the columns?
        """
        m, n = len(matrix) - 1, len(matrix[0]) - 1

        l, r = 0, m
        
        while l <= r:
            middle = (l+r) // 2
            i, j = 0, n
            while matrix[middle][0] < target and i <= j:
                mid = (i+j) // 2
                if matrix[middle][mid] == target:
                    return True
                elif matrix[middle][mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            
            if matrix[middle][0] > target:
                r = middle - 1
            elif matrix[middle][0] < target:
                l = middle + 1
            else:
                return True
        return False