Problem Statement
=========

Write a function to print a 2ZD array (n x m) in spiral order (clockwise).
For example, consider the following input:
```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Then the output of your program should be:
```
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

---

Hm... If the 2D array is not empty, print the first element, which is the top row. Next, print the last elements of the remaining rows. Then... *paused, staring at the question and standing there in silence for I don't remember how long*.

Oh! We need to transform the remaning rows so the next numbers to be printed are on the top row. This is achieved by swapping rows with columns and then reversing them.

After I wrote out the solution, the hiring manager was like "creative solution! but it's hard to understand." Then I went on explaining what `zip` does to the 2D array which is the swapping part, then `reversed` the transformed array so that the next number to be printed is the first element in the first row, and finally convert it back to `list`.

It was like teaching cows to climb trees because oh that's right! He is not a programmer!