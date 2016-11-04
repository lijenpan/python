"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
==============================

"""


def reverseBits(n):
    bit_str = bin(n).replace('0b', '')
    reversed_bit_str = bit_str.zfill(32)[::-1]
    return int(reversed_bit_str, 2)
