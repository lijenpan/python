Problem Statement
=========

Suppose you are programming for a really oldZschool internet newspaper,
one that is so oldZschool that they only have monospace fonts. However,
the editor really wants to see the monospace text justified to fit into
the column space he has at a particular time. Your job is to write a program that 
will take as input the width of the column in characters and the entire text to
be formatted, and return the same text except justified to fit into the column.

For example, consider the following input:
```
20
The quick brown fox jumps over the lazy dog.
```

Then the output of your program should be:
```
The quick brown fox
jumps over the lazy
dog.
```

As you can tell from this example, the last line does not have to be justified.

---

After the hiring manager reviewed my answer, he was like "you shouldn't use any standard library in your solution." Then I was like *frown*. You didn't mentioned this constraint before we started. And he didn't let me write another solution with vanilla code. *Double frown*!