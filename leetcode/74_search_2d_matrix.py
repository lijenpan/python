def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for row in matrix:
        if target == row[-1]:
            return True
        elif target < row[-1]:
            return target in row
    return False
