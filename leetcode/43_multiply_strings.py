"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.
==================================
This actually a practical question with known solution: Karatsuba Algorithm.

procedure karatsuba(num1, num2)
  if (num1 < 10) or (num2 < 10)
    return num1*num2
  /* calculates the size of the numbers */
  m = max(size_base10(num1), size_base10(num2))
  m2 = m/2
  /* split the digit sequences about the middle */
  high1, low1 = split_at(num1, m2)
  high2, low2 = split_at(num2, m2)
  /* 3 calls made to numbers approximately half the size */
  z0 = karatsuba(low1,low2)
  z1 = karatsuba((low1+high1),(low2+high2))
  z2 = karatsuba(high1,high2)
  return (z2*10^(2*m2))+((z1-z2-z0)*10^(m2))+(z0)

But let's solve this like a normal person.
"""


def multiply(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    arr = [0 for _ in range(len(num1)+len(num2))]
    for i in xrange(0, len(num1)):
        for j in xrange(0, len(num2)):
            arr[i+j] += int(num1[i]) * int(num2[j])
    ans = []
    for i in xrange(0, len(arr)):
        digit = arr[i] % 10
        carry = arr[i] / 10
        if i < len(arr)-1:
            arr[i + 1] += carry
        ans.insert(0, str(digit))
    while ans[0] == '0' and len(ans) > 1:
        del ans[0]
    return ''.join(ans)
