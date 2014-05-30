Fibonacci
=========

I think any software developer has been asked to write a function to computer *n*th fibonacci number in his or her career.

If a recent college graduate and functional programming enthusiast probably will answer in recursion:
```
def F(n):
    # Time O(2**n), Space O(n)
    if n < 2: return n
    else: F(n - 1) + F(n - 2)
```
Nice and clean. Problem is solved in two lines of code. Then the interviewer asks you to improve the time complexity. You probably will answer with iterative solution:
```
def F(n):
    # Time O(n), Space(n)
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
```
Much better performance indeed.

In the pre [Wolfram|Alpha] world, this answer is probably good enough. But in recent years, interviewers start asking how can you improve this further, say like O(1) for both Time and Space complexity. You are in shocked because you never heard of such thing. Then you are staring at the whiteboard and thinking how can this be done?!

After five to ten of minutes of struggle, the interviewer will stop you because you don't have the answer. Some not-so-nice interviewers will say go home and do some research and then turn you away. While others will show you this answer without any explanation on how they conjured up this solution:

```
import math

def F(n):
    # O(1) for both Time and Space, awesome!
	return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))
```

In my opinion, the ultimate solution is not a fair interview question for programmers. The interviewees have to memorize the formula or they will not be able to relate this to the golden ratio formula and start deriving from there to the solution in ten minutes or less. Perhaps I should speak only for myself.

[Wolfram|Alpha]:http://www.wolframalpha.com/