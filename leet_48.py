
# <---Rotate image--->



class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        store=copy.deepcopy(matrix)
        size=len(matrix)
        for i in range(size):
            for j in range(size):
                matrix[j][size-1-i]=store[i][j]


        """
        Do not return anything, modify matrix in-place instead.
        """
        