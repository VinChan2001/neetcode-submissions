class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0]*(cols+1) for i in range(rows+1)]

        for row in range(rows):
            for col in range(cols):
                current = matrix[row][col]

                left = self.prefix[row+1][col]
                top = self.prefix[row][col+1]
                overlap = self.prefix[row][col]

                self.prefix[row+1][col+1]=(current + left +top - overlap)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        big_rectangle = self.prefix[row2+1][col2+1]
        overlap_rectangle = self.prefix[row1][col1]

        top_rectangle = self.prefix[row2+1][col1]
        left_rectangle = self.prefix[row1][col2+1]

        return ((big_rectangle - top_rectangle - left_rectangle) + overlap_rectangle)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)