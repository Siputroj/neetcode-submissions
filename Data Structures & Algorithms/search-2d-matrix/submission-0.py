class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search through which row contains the range
        if len(matrix) != 1:

            start = 0
            end = len(matrix) - 1

            while start <= end:
                mid = start + ((end - start) // 2)
                if matrix[mid][0] > target:
                    end = mid - 1
                elif matrix[mid][-1] < target:
                    start = mid + 1
                else:
                    break        
            
            if start > end:
                return False
        else:
            mid = 0

        # once you get a row you do another binary in that row
        row = matrix[mid]
        start = 0
        end = len(row) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if row[mid] > target:
                end = mid - 1
            elif row[mid] < target:
                start = mid + 1
            else:
                return True

        return False

        