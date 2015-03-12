Congratulations NetSuite! You won the worst experience from Rackspace. Kudos to Pavel and the hiring manager.

Instructions
=========
- Thanks for your interest in NetSuite development!  Please complete the following questions. If you can't solve a problem completely, feel free to submit your best partial solution, together with a comment as to what is missing or what shortcomings you see with your solution.  We give partial credit!
- For SQL questions, you may use any dialect of SQL.  Preferred dialects are ANSI SQL and Oracle SQL.  You may wish to indicate the dialect you are using.
- For programming questions, Java is the preferred language.  However, you may also use another modern object-oriented language such as C++, Python, Ruby,JavaScript, C#, or Objective C, or a functional language such as Scheme, Haskell, Erlang, Scala, or OCaml.  Just let us know what you're doing.
- We'll be looking at everything.  Pretend you are writing production code. We'll take into account comments (if any), identifier names, and formatting. 
- Ideally the questions should be completed in 60 minutes. 


- Good luck!                                                                1.32


--------------------------------------------------------------------------------

QUESTION 1

Given a sorted array of integers, write a method to remove the duplicates.  Do
not use any classes from the java.util package, or the equivalent library for
your language.

Example: [ 1, 2, 3, 3, 3, 4, 4, 10, 13, 15, 15, 17 ] ->
         [ 1, 2, 3, 4, 10, 13, 15, 17 ]

A) Solution template:
```
    # Python implementation
    def remove_duplicates(values):
        return list(set(values))

    # But I think this is the answer you are looking for even
    # though not as elegant.
    def remove_duplicates(values):
        seen = set()
        seen_add = seen.add
        return [x for x in values if not (x in seen or seen_add(x))]
```
   Questions (answer these):
   ANSWERS BELOW ARE GIVEN BASED ON SECOND IMPLEMENTATION
   1. Did you write that as if you were writing production code? Yes.
   2. What assumptions does your implementation make about the input parameter? The input is given as list of sorted integers and new array is allocated.
   3. What is removeDuplicates(x).length, in your implementation? Given the input from the Example, it returns 8.
   4. Are you using all the information you have about the input array? I think so.
   5. What is the algorithmic complexity ("big O") of your function? O(n), O(1) for insertation and deletion.

B) Now implement your solution to A as a Java iterator that does not modify the source
   array, and returns only unique elements.  Write a concrete subclass of the
   interface java.util.Iterator; the interface is included below for convenience
   (see http://download-llnw.oracle.com/javase/6/docs/api/java/util/Iterator.html).
   You do not need to implement the optional remove() method.

   (For other languages, implement a generator or other equivalent construct.)

   Do not "cheat" by calling the removeDuplicates() you defined above. One benefit
   of iterators is that they can operate incrementally -- make your iterator
   only do the minimum work it needs to in each call to hasNext() or next().

    # Python implementation
    def remove_duplicate(values):
        seen = set()
        seen_add = seen.add
	for x in values:
	    if not (x in seen or seen_add(x)):
		yield x

   Questions (answer these):
   6. Does your implementation work for generic objects, numbers, or integers? Yes.
   7. If it does not work with objects, what would be required to make it work
      for generic objects? Not applicable.
   

--------------------------------------------------------------------------------

QUESTION 2

Given a non-negative real number a, its square root is a number x, such that x * x = a.
One way to compute a square root is via successive approximation, where one estimate
yields a better estimate.

For example, let's say you are trying to find the square root of 2, and you have
an estimate of 1.5. We'll say a = 2, and x = 1.5. To compute a better estimate,
we'll divide a by x. This gives a new value y = 1.333333... However, we can't just
take this as our next estimate (why not?). We need to average it with the previous
estimate. So our next estimate, xx will be (x + y) / 2, or 1.416666...

A) Write a function that takes a non-negative real number a, and an epsilon (a
   small real number), and returns an approximation of the square root of a.
```
    def square_root(a, epsilon):
        if a < epsilon:
            return 0
        x = 1.5
        while True:
            if abs(x * x - a) < epsilon:
                return x
            y = a / x
            x = (x + y) / 2
```
   Epsilon determines how accurate the approximation needs to be. The function
   should return the first approximation x it obtains that satisfies abs(x*x - a) < epsilon,
   where abs(x) is the absolute value of x.

   Questions (answer these):
   1. Why can't the next estimate, xx, be computed as a / x, where x is the
      previous estimate? If so then the next estimate after that is a / xx which is a/(a/x) = x, which creates infinite loop.
   2. What happens, in your implementation, if a = 0? It returns 0.
   3. What value does your program give for square_root(2, 1e-6)? 1.41421356237


--------------------------------------------------------------------------------
QUESTION 3

You are given two database tables, EMPLOYEES and BONUS, with the following
schema.  Data shown below should be considered example data; the actual table
will contain other data.

   EMPLOYEES                                       BONUS
   __________________________________________      _____________
   EMPID  NAME  SUPERVISOR  LOCATION   SALARY      EMPID  NBONUS
   ------------------------------------------      -------------
      34  Amy               NY         110000         17    5000
      17  Ben           34  TN          75000         10    2000
       5  Chris         34  TN          80000         34    5000
      10  Don            5  HI         100000      ...
   ...

A) Write a SQL statement to return the employee's name, supervisor's name and
   bonus of everyone who got a bonus greater than 1000.
# MySQL
```
select e.name as 'employee_name', b.nbonus as 'bonus', es.name as 'supervisor_name'
from employees e
left outer join employees es on e.supervisor = es.empid
left outer join bonus b on e.empid = b.empid
where b.nbonus > 1000;
```

B) Write a SQL statement to list the highest paid employee in each location.
   Ranking should be based on salary plus bonus.  Output should include employee
   name, salary, bonus, and total pay (salary plus bonus).
```
select e.name as 'employee_name', e.salary, b.nbonus as 'bonus', e.salary ifnull(b.nbonus, 0) as 'total_pay'
from employees e left outer join bonus b on e.empid = b.empid
where (location, e.salary + ifnull(b.nbonus, 0)) in (
    select e.location, max(e.salary + ifnull(b.nbonus, 0))
    from employee e left outer join bonus b on e.empid = b.empid
    group by location);
```

C) Given a NEW_SUPERVISOR table (columns: EMPID, SUPERVISOR), write an update
   statement that updates the supervisor of each employee with a new supervisor.
   The NEW_SUPERVISOR table is an incremental update, so employees not listed in
   the table must retain their existing supervisor.
```
update employee e left outer join new_supervisor ns on e.empid = ns.empid
set e.supervisor = ifnull(ns.supervisor, e.supervisor);
```
---

First of all, Pavel from NetSutie failed to send me the test at 8PM as agreed. He blamed on his Outlook broke down during his bedtime.
So I took the test the next morning and finished in 55 minutes. After I submitted my answers, Pavel followed up with a phone call asking
general HR questions such as why did I leave my last company and what kind of work interest me.

A couple hours later, Pavel got back to me and asked can I explain why I left my last company "in more detail" because the hiring manager asked.
I was like didn't we already talk about this?! But anyways, I'll say it again...

Next day Pavel replied back and said the hiring manager found my answers "not meeting his technical expectations". Then he said he hope
that it will not ruin my impressions of NetSuite so we can refresh our communication in the future. He then further asked for my feedback.
I told Pavel to share the hiring manager's feedbacks on my answers. What are particularly bad or unsatisfactory about them? I take pride in my profession and am open to constructive criticism.
Otherwise I can't help to think his decision was biased because he did make you ask me twice about why I left my last job "in more detail".

Pavel never reply back.