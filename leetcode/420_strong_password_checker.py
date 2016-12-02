"""
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong,
assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to
make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
===============================
This is indeed hard to get it right.

Check for length, lower case, upper case, and number is easy. The difficult part is checking repeating character.
We can replace, delete, or add character. Replacing character is preferred because it's the minimum action to
resolve repeating character and upper/lower case issue.
"""


def strongPasswordChecker(s):
    """
    :type s: str
    :rtype: int
    """
    total_count = len(s)
    has_lower = any(c for c in s if c.islower())
    has_upper = any(c for c in s if c.isupper())
    has_digit = any(c for c in s if c.isdigit())

    type_count = bool(has_digit) + bool(has_lower) + bool(has_upper)

    clist = []
    li, lc = 0, (s[0] if s else None)
    for i, c in enumerate(s):
        if c != lc:
            clist.append((lc, li, i - 1))
            li, lc = i, c
    clist.append((lc, li, total_count - 1))

    repeats = [y - x + 1 for c, x, y in clist if y - x > 1]

    if total_count < 6:
        if max(repeats + [0]) == 5:
            return max(2, 3 - type_count)
        return max(6 - total_count, 3 - type_count)

    delete_count = max(total_count - 20, 0)

    heap = [(r % 3, r) for r in repeats]

    heapq.heapify(heap)
    while heap and total_count > 20:
        mod, r = heapq.heappop(heap)
        delta = min(mod + 1, total_count - 20)
        total_count -= delta
        heapq.heappush(heap, (2, r - delta))

    change_count = sum(r / 3 for mod, r in heap)

    return delete_count + max(change_count, 3 - type_count)
