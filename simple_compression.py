"""Write a simple compression algorithm to change aaabbbcccaabbbbc into a3b3c3a2b4c1"""
def simple_compression(input_str):
    # This was my answer when I first learned Python
    # But this is a lot of code for something must have a simple solution!
    result = []
    current_letter = None
    count = 0
    for index, letter in enumerate(input_str):
        if not current_letter or current_letter == letter:
            current_letter = letter
            count += 1
        else:
            result.append(''.join([current_letter, str(count)]))
            current_letter = letter
            count = 1
        if index == len(input_str) - 1:
            result.append(''.join([current_letter, str(count)]))
    return ''.join(result)


# Second implementation after I learned more about Python.
from itertools import groupby

def simple_compression(input_str):
    return ''.join([k + str(len(list(g))) for k, g in groupby(input_str)])
