"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
==============================

"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = []
    for i in range(numRows):
        new_value = 1
        row = [new_value]
        for j in xrange(i):
            new_value = new_value * (i - j) * 1 / (j + 1)
            row.append(new_value)
        res.append(row)
    return res

if __name__ == "__main__":
    generate(10)
