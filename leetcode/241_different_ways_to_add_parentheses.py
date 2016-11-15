"""
Given a string of numbers and operators, return all possible results from computing all the different possible
ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2

Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Output: [-34, -14, -10, -10, 10]
===============================
I was going to just do it with regex and then I saw this: https://discuss.leetcode.com/topic/19867/python-solution-52ms-with-simple-interpretation/4?show=48432
"""


def diffWaysToCompute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    return [a + b if c == '+' else a - b if c == '-' else a * b
            for i, c in enumerate(input) if c in '+-*'
            for a in diffWaysToCompute(input[:i])
            for b in diffWaysToCompute(input[i + 1:])] or [int(input)]
