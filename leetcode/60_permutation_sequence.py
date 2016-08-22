"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
==================================
You need the answer from Q31.

My answer from Q31 doesn't play nice. So wrote another version.
"""


def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    fac = [1]
    for i in xrange(1, n + 1):
        fac.append(fac[-1] * i)

    elegible = xrange(1, n + 1)
    per = []
    for i in xrange(n):
        digit = (k - 1) / fac[n - i - 1]
        per.append(elegible[digit])
        elegible.remove(elegible[digit])
        k = (k - 1) % fac[n - i - 1] + 1
    return "".join([str(x) for x in per])
